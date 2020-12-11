from django.contrib import admin
from .models import MyUser
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import MyUser

# Register your models here.


admin.site.register(MyUser)
