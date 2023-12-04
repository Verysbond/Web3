# from .models import Task
# from django.forms import ModelForm, TextInput
#
# class TaskForm(ModelForm):
#     class Meta:
#         model = Task
#         fields = ['title', 'task']
#         widgets = {'title': TextInput(attrs={'class': "form-control", "placeholder": 'Введите название'}),
#                    'task': TextInput(attrs={'class': "form-control", "placeholder": 'Введите описание'})
#         }
#
#

from django import forms


class TaskForm(forms.Form):
    title = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите название'
        })
    )
    task = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Ведите описание'
        })
    )
