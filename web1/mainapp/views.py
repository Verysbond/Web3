from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def main_index(reqest):
    return HttpResponse('<h4>HELLO</h4>')
