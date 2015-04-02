__author__ = 'msveshnikov'

from django.db import models


class CV(models.Model):
    name = models.CharField(max_length=30)
    pub_date = models.DateTimeField('date published')
    photo = models.ImageField()
    location = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    skype = models.CharField(max_length=50)
    facebook = models.CharField(max_length=50)
    about_me = models.CharField(max_length=1500)
    technical = models.CharField(max_length=5000)
    education = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    date_from = models.DateTimeField('start date')
    date_to = models.DateTimeField('end date')
    description = models.CharField(max_length=100)
    responsibilities = models.CharField(max_length=1000)
    achievements = models.CharField(max_length=200)
    technologies = models.CharField(max_length=100)
