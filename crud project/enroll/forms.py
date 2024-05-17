from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.core import validators
from .models import kashif
from django import forms


class SignupForm(UserCreationForm):
     class Meta:
         model = User
         fields = ['username','first_name','last_name','email']
         labels = {'email': 'Email'}
         widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
        }
    


class StudentRegistration(forms.ModelForm):
    class Meta:
        model = kashif
        fields = ['name','email', 'password']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
        }
    
    