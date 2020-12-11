from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MyUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model : MyUser
        fields = UserCreationForm.Meta.fields + ('user_nickname',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model : MyUser
        fields : UserChangeForm.Meta.fields
