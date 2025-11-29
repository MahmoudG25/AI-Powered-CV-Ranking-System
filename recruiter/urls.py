from django.urls import path
from . import views

app_name = 'recruiter'

urlpatterns = [
  path('', views.upload_view, name='upload')
]
