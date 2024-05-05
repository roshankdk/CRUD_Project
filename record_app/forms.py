from dataclasses import field

from django.forms import widgets
from .models import user
from django import forms

class userForm(forms.ModelForm):
    class Meta():
        model = user
        fields = ('first_name','last_name','email','phone')
        widgets = {
            'first_name':forms.TextInput(),
            'last_name':forms.TextInput(),
            'email':forms.EmailInput(),
            'phone':forms.TextInput(),
        }
