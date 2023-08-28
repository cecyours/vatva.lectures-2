
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Post,Like,Comment
class UserSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','username','email','password1','password2']
 


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['topic', 'title', 'description', 'poster']