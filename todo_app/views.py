from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView
from .models import Task
from django.urls import reverse_lazy
# Create your views here.

class TaskList(ListView):
    model = Task

class UpdateTask(UpdateView):
    model = Task
    fields = '__all__'

class DeleteTask(DeleteView):
    model = Task
    success_url = reverse_lazy('todo_app:list')
