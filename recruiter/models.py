from django.db import models


class CandidateCV(models.Model):

  candidate_name = models.CharField(max_length=255 , null=True , blank=True)
  candidate_email = models.EmailField(max_length=255 , null=True , blank=True)
  # candidate_phone = models.CharField(max_length=255 , null=True , blank=True)
  # candidate_address = models.CharField(max_length=255 , null=True , blank=True)
  # candidate_city = models.CharField(max_length=255 , null=True , blank=True)
  # candidate_country = models.CharField(max_length=255 , null=True , blank=True)
  # candidate_zipcode = models.CharField(max_length=255 , null=True , blank=True)
  # candidate_education = models.CharField(max_length=255 , null=True , blank=True)
  # candidate_experience = models.CharField(max_length=255 , null=True , blank=True)
  # candidate_skills = models.CharField(max_length=255 , null=True , blank=True)
  # candidate_portfolio = models.CharField(max_length=255 , null=True , blank=True)
  # candidate_cover_letter = models.CharField(max_length=255 , null=True , blank=True)
  # candidate_resume = models.CharField(max_length=255 , null=True , blank=True)
  
  original_file = models.FileField(upload_to='CVS/') 

  full_text = models.TextField()

  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.candidate_name or f"CV {self.id}"
