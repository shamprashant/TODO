from django.db import models

# Create your models here.

class Task(models.Model):
    comment = models.CharField(max_length = 150)