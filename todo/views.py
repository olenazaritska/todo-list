from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo.models import Task
from todo.forms import TaskForm


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")
