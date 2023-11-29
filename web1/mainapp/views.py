from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def main_index(reqest):
    return render(reqest, 'mainapp/index.html')

def about(reqest):
    return render(reqest, 'mainapp/about.html')

