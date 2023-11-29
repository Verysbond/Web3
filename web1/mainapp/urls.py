
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_index, name="main_index"),
    path('about', views.about, name="about"),
]