from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)


class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(null=True, max_length=70)
    location = models.CharField(null=True, max_length=70)
    date_range = models.CharField(null=True, max_length=70)
    position = models.CharField(null=True, max_length=70)
    job_description = models.CharField(null=True, max_length=70)


class Education(models.Model):
    DEGREE_CHOICES = [
        ('diploma', 'Diploma'),
        ('associate', 'Associate Degree'),
        ('bachelor', "Bachelor's Degree"),
        ('master', "Master's Degree"),
        ('phd', 'PhD'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    university = models.CharField(null=True, max_length=70)
    location = models.CharField(null=True, max_length=70)
    date_range = models.CharField(null=True, max_length=70)
    degree = models.CharField(null=True, max_length=70, choices=DEGREE_CHOICES)
    study_description = models.CharField(null=True, max_length=70)

    @property
    def pretified_degree(self):
        return dict(self.DEGREE_CHOICES).get(self.degree)
