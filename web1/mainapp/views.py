from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
# Create your views here.

def main_index(reqest):
    task = Task.objects.all()

    return render(reqest, 'mainapp/index.html', {'title': 'Главная страница', 'tasks': task })


def about(reqest):
    return render(reqest, 'mainapp/about.html')


def create(reqest):
    return render(reqest, 'mainapp/create.html')

