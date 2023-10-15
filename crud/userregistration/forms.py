from django import forms
from .models import User
class UserRegFrom(forms.ModelForm):
    class Meta:
        model= User
        fields= {'name','password','dob'}
        widgets= forms.DateInput( )