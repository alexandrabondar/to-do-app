from .models import Task
from django.forms import ModelForm, TextInput, Textarea
from django import forms


class TaskForm(forms.Form):
    title_task = forms.CharField(max_length=100, widget = forms.TextInput(attrs={
        'class': 'form-control mt-2',
        'placeholder': 'Enter a task'
    }))

    description_task = forms.CharField(max_length=200, widget=forms.Textarea(attrs={
        'class': 'form-control mt-2',
        'placeholder': 'Enter a description'
    }))
    # class Meta:
    #     model = Task
    #     fields = ["title_task", "description_task"]
    #     widgets = {
    #         'title_task': TextInput(attrs={
    #             'class': 'form-control mt-2',
    #             'placeholder': 'Enter a task'
    #         }),
    #         'description_task': Textarea(attrs={
    #             'class': 'form-control mt-2',
    #             'placeholder': 'Enter a description'
    #         }),
    #     }