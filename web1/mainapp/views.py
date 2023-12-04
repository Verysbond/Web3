from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
# Create your views here.

def main_index(request):
    task = Task.objects.all()

    return render(request, 'mainapp/index.html', {'title': 'Главная страница', 'tasks': task })


def about(request):
    return render(request, 'mainapp/about.html')


def create(request):
    form = TaskForm()
    context = {
        "form": form,
    }
    return render(request, 'mainapp/create.html', context)

