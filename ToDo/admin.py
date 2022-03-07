from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from ToDo.forms import CustomUserEditForm, RegisterCustomUserForm
from ToDo.models import CustomUser


# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = RegisterCustomUserForm
    form = CustomUserEditForm
    model = CustomUser
    list_display = ['email', 'username','first_name', 'last_name',]

admin.site.register(CustomUser, CustomUserAdmin)