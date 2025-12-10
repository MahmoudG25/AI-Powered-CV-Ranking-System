from django.shortcuts import render , redirect
from .models import CandidateCV
from .ai.evaluator import evaluate_candidates
import PyPDF2
import os
from django.http import HttpResponse
from .ai.evaluator import evaluate_candidates

def upload_view(request):
    if request.method == "POST":
        job_title = request.POST.get("job_title")
        job_requirements = request.POST.get("job_requirements")

        files = request.FILES.getlist("cvs")

        if len(files) < 1 or len(files) > 5:
            return render(request, "recruiter/upload.html", { "error": "Please upload between 1 and 5 CVs." })
            

        saved_cvs = []
        for file in files:
            text = extract_text_from_file(file)

            cv_obj = CandidateCV.objects.create(
                original_file=file,
                full_text=text,
                candidate_name=None,
                candidate_email=None,
            )

            saved_cvs.append(cv_obj)

        ai_result = evaluate_candidates(
            job_title=job_title,
            job_requirements=job_requirements,
            candidates=saved_cvs
        )

        print("AI RESULT:", ai_result, type(ai_result))  

        return render(request, "recruiter/results.html", {
            "job_title": job_title,
            "job_requirements": job_requirements,
            "ai_result": ai_result,
        })

    return render(request, "recruiter/upload.html")



def extract_text_from_file(file):
    ext = file.name.lower()

    if ext.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text

    elif ext.endswith(".txt") or ext.endswith(".md"):
        return file.read().decode("utf-8", errors="ignore")

    else:
        return ""
