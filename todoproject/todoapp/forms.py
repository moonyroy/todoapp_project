from django import forms
from django.forms import fields
from django.forms.fields import Field
from .models import TodoItem

class TodoItemForm(forms.ModelForm):
    class Meta :
        model = TodoItem
        fields = ['work' , 'date']

