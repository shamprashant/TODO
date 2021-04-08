from django.db import models
from django.urls import reverse
# Create your models here.

class Task(models.Model):
    comment = models.CharField(max_length = 150)
    
    def get_absolute_url(self):
        return reverse('todo_app:list')