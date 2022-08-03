from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Enter login",required=True)
    email = forms.EmailField(label="Enter email",required=True)
    password1=forms.CharField(label="Enter password",required=True, widget=forms.PasswordInput())
    password2=forms.CharField(label="Confirm password",required=True,widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email',]
