from django import forms
from django.forms import fields
from .models import Participant


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username')
    email = forms.EmailField(label='Email')
