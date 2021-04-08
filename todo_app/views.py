from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
# Create your views here.

class TaskList(ListView):
    model = Task

class UpdateTask(UpdateView):
    model = Task
    fields = '__all__'

class DeleteTask(DeleteView):
    model = Task
    success_url = reverse_lazy('todo_app:list')

class CreateTask(CreateView):
    model = Task
    fields = '__all__'

def create_task(request):
    task = request.POST['task']
    task = Task(comment=task)
    task.save()
    return redirect('todo_app:list')
