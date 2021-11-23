from django.db import models

# Create your models here.

class Team(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    facebook = models.URLField(max_length=200)
    google = models.URLField(max_length=200)
    twitter = models.URLField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstName

class Contactus(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.fullname + ' -- ' + self.email
