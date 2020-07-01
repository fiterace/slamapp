from django.db import models

# Create your models here.
class tableThree(models.Model):
    senior = models.CharField(max_length=264)
    junior = models.CharField(max_length=264)
    ans1 = models.CharField(max_length=1000)
    ans2 = models.CharField(max_length=1000)
    ans3 = models.CharField(max_length=1000)
    ans4 = models.CharField(max_length=1000)
    ans5 = models.CharField(max_length=1000)
    ans6 = models.CharField(max_length=1000)
    ans7 = models.CharField(max_length=1000)
    ans8 = models.CharField(max_length=1000)
    ans9 = models.CharField(max_length=1000)
    ans10 = models.CharField(max_length=1000)
    ans11 = models.CharField(max_length=1000)
    ans12 = models.CharField(max_length=1000)
    ans13 = models.CharField(max_length=1000)
    ans14 = models.CharField(max_length=1000)
    ans15 = models.CharField(max_length=1000)

class senior_users(models.Model):
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=264, default="NA")