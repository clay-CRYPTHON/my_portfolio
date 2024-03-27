from django.utils import timezone
from django.db import models


class ProjectModel(models.Model):
    name = models.CharField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='portfolio/image')

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    subject = models.CharField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return self.name


class ExperienceEdu(models.Model):
    class Status(models.TextChoices):
        Experience = 'Ex', 'Experience'
        Education = 'ED', 'Education'

    status = models.CharField(max_length=2,
                              choices=Status.choices)
    date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=250)
    body = models.TextField()

    objects = models.Manager()

    def __str__(self):
        return self.status


class SkillsLang(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
