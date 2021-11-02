from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from .models import Graphs


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class CreateProject(ModelForm):
    class Meta:
        model = Graphs
        fields = ['title', 'description', 
                'x1','x2','x3','x4','x5',
                'y1','y2','y3','y4','y5']
