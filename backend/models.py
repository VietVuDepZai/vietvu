from django.db import models

# Create your models here.
class Skill(models.Model):
    imageUrl = models.ImageField(upload_to='image')
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

class Experiences(models.Model):
    title = models.CharField(max_length=500)
    company_name =  models.CharField(max_length=500)
    icon=  models.ImageField(upload_to='image')
    iconBg=  models.CharField(max_length=500)
    linkicon=  models.CharField(max_length=100)
    date=  models.CharField(max_length=500)
    points=  models.CharField(max_length=500)

class Projects(models.Model):
    iconUrl =  models.ImageField(upload_to='image')
    theme = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    description =  models.CharField(max_length=500)
    link =  models.CharField(max_length=100)