from email.policy import default
from django.db import models

# Create your models here.
def user_directory_path(instance, filename):
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return format( filename)
  
class webinfo(models.Model):
    title=models.CharField(max_length=200, null=True, blank=True)
    backgroundImage=models.ImageField(default="banner.png", null=True,blank=True)


    def __str__(self):
        return self.title

class Services(models.Model):
    name=models.CharField(max_length=200, null=True, blank=True)
    image=models.ImageField(null=True,blank=True, default="placeholder.jpg")
    desc=models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name

class Projects(models.Model):

    name=models.CharField(max_length=200, null=True, blank=True)
    image=models.ImageField(null=True,blank=True,default="placeholder.jpg")
    desc=models.CharField(max_length=500, null=True, blank=True)
    livelink=models.CharField(max_length=500, null=True, blank=True)
    githublink=models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name

class expertise(models.Model):
    name=models.CharField(max_length=200, null=True, blank=True)
    percentage=models.FloatField(default=0.0, null=True, blank=True)

    def __str__(self):
        return self.name

class personal(models.Model):
    fname=models.CharField(max_length=200, null=True, blank=True)
    lname=models.CharField(max_length=200, null=True, blank=True)
    profile=models.ImageField(null=True,blank=True,default="placeholder.jpg")
    address=models.CharField(max_length=200, null=True, blank=True)
    email=models.CharField(max_length=200, null=True, blank=True)
    about=models.TextField(null=True, blank=True)
    creativeskills=models.TextField(null=True, blank=True)
    about2=models.TextField(null=True, blank=True)
    upload = models.FileField(upload_to = user_directory_path,default="Nauman_Iftikhar_1.pdf")
    githubprofile=models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.fname


