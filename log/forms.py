from attr import field
from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'lastname', 'age', 'date', 'gender']