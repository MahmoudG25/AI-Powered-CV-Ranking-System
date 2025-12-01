import os
import json
from typing import List
from openai import OpenAI
from django.conf import settings
from recruiter.models import CandidateCV

client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)

def evaluate_candidates(job_title: str, job_requirements: str, candidates: List[CandidateCV]):


    cvs_data = []
    for cv in candidates:
        cvs_data.append({
            "id": cv.id,
            "existing_name": cv.candidate_name or "",
            "existing_email": cv.candidate_email or "",
            "text": (cv.full_text or "")[:15000],
        })

    prompt = f"""
You are an AI assistant helping a recruiter evaluate candidates.

JOB INFO:
- Job title: {job_title}
- Job requirements:
{job_requirements}

You are given a list of CVs as JSON.
For EACH CV you MUST:

1) Try to extract:
   - candidate_name
   - candidate_email
   (Use existing_name / existing_email if they look valid.)

2) Evaluate how well the CV matches the job (0–100, integer).

3) Return:
   - fit_score (0–100)
   - strengths: list of 3–6 short bullet points relevant to the job
   - gaps: list of missing/weak skills compared to the job requirements
   - summary: 2–4 lines describing suitability.

AFTER that:

4) Rank ALL candidates from strongest to weakest (based mainly on fit_score).
   For each rank, include a short text "reason" explaining why.

5) Generate a professional email for the TOP candidate ONLY:
   - Use formal English.
   - If candidate_name is available, address them by name in greeting.
   - Invite them to the next stage of the process.

VERY IMPORTANT:
Return ONLY VALID JSON with EXACTLY this structure:

{{
  "candidates": [
    {{
      "id": 1,
      "candidate_name": "string or null",
      "candidate_email": "string or null",
      "fit_score": 0,
      "strengths": ["..."],
      "gaps": ["..."],
      "summary": "..."
    }}
  ],
  "ranking": [
    {{
      "id": 1,
      "reason": "short reason"
    }}
  ],
  "email": {{
    "to_id": 1,
    "subject": "string",
    "body": "multi-line string"
  }}
}}

Here is the CVs data as JSON:
{json.dumps(cvs_data, ensure_ascii=False)}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    raw_output = response.choices[0].message.content


    cleaned = raw_output.strip()

    if cleaned.startswith("```"):
        lines = cleaned.splitlines()
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        cleaned = "\n".join(lines).strip()

    try:
        data = json.loads(cleaned)
    except json.JSONDecodeError:
        raise ValueError(f"Model did not return valid JSON. Raw output:\n{raw_output}")

    return data

