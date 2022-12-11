import email
from email.policy import default
from pyexpat import model
from re import T
from tkinter import CASCADE
from unittest import case
from django.db import models
from django.forms import EmailField

# Create your models here.
#experience, min_salary , job_type, education, job_shift,job_category,job_desc,website
#user master table
class UserMaster(models.Model):
    email= models.EmailField(max_length=50,default="nomail")
    password = models.CharField(max_length=50)
    otp = models.IntegerField()
    role = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_varified  =models.BooleanField(default=False)
    is_created = models.DateTimeField(auto_now_add=True)
    is_updated = models.DateTimeField(auto_now_add=True)


class Candidate(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50,default = "-")
    lastname = models.CharField(max_length=50,default = "-")
    contact = models.CharField(max_length=50,default = "")
    min_salary = models.CharField(max_length=50,default = "")
    state = models.CharField(max_length=50,default = "-")
    city = models.CharField(max_length=50,default = "-")
    country = models.CharField(max_length=50,default = "-")
    dob = models.CharField(max_length=50)
    edu = models.CharField(max_length=50,default = "-")
    gender= models.CharField(max_length=50,default = "")
    profile_pic = models.ImageField(upload_to="app/images/candidates")
    exp = models.CharField(max_length=50,default="0")
    job_category = models.CharField(max_length=50,default="-")
    website = models.CharField(max_length=50,default="-")
    

class Company(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=150,default = "")
    firstname = models.CharField(max_length=50,default = "")
    lastname = models.CharField(max_length=50,default = "")
    state = models.CharField(max_length=50,default = "")
    city = models.CharField(max_length=50,default = "")
    country = models.CharField(max_length=50,default = "")
    contact = models.CharField(max_length=50,default = "")
    company_address = models.CharField(max_length=150,default = "")
    profile_pic = models.ImageField(upload_to="app/images/companies")
   

class jobDetails(models.Model):
    company_id = models.ForeignKey(Company,on_delete=models.CASCADE)
    jobname = models.CharField(max_length=150,default="")
    companyname = models.CharField(max_length=150,default="")
    companyaddress = models.CharField(max_length=250,default="")
    jobdescription = models.TextField(max_length=500,default="")
    qualification = models.CharField(max_length=150,default="")
    responsibilities = models.CharField(max_length=150,default="")
    location= models.CharField(max_length=200,default="")
    workmode = models.CharField(max_length=150,default="")
    companywebsite = models.CharField(max_length=150,default="")
    companyemail = models.CharField(max_length=150,default="")
    experience = models.CharField(max_length=150,default="")
    skills = models.CharField(max_length=250,default="")
    salary = models.CharField(max_length=100,default="")
    timing = models.CharField(max_length=120,default="")

class ApplyJob(models.Model):
    candidate = models.ForeignKey(Candidate,on_delete=models.CASCADE)
    job = models.ForeignKey(jobDetails,on_delete=models.CASCADE)
    company = models.ForeignKey(Company,on_delete=models.CASCADE,null=True)
    firstname = models.CharField(max_length=50,default = "-")
    lastname = models.CharField(max_length=50,default = "-")
    contact = models.CharField(max_length=50,default = "")
    min_salary = models.CharField(max_length=50,default = "")
    edu = models.CharField(max_length=50,default = "-")
    gender= models.CharField(max_length=50,default = "")
    resume = models.ImageField(upload_to="app/resume")
    exp = models.CharField(max_length=50,default="0")
    job_category = models.CharField(max_length=50,default="-")
    website = models.CharField(max_length=50,default="-")



