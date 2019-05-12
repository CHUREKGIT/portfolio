from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.TextField()
    jobposition = models.CharField(max_length=200, default='paker')

