from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
# Create your views here.

def main_index(request):
    task = Task.objects.all()

    return render(request, 'mainapp/index.html', {'title': 'Главная страница', 'tasks': task})


def about(request):
    return render(request, 'mainapp/about.html')


def create(request):
    error = ""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main_index")
        else:
            error = "Форма была не верной"
    form = TaskForm()
    context = {
        "form": form,
        "error": error
    }

    return render(request, "mainapp/create.html", context=context)




