from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

# представляет форму регистрации
from ToDo.models import CustomUser


class RegisterCustomUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Имя пользователя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Повтор пароля'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


# представляет форму авторизации
class LoginCustomUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Логин'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Пароль'}))


class CustomUserEditForm(UserChangeForm):
    """
    Форма для редактирования аккаунта пользователя
    """
    avatar = forms.ImageField(required=False,
                              widget=forms.FileInput(attrs={
                                  'class': 'fadeIn second',
                                  'placeholder': 'Avatar',
                              }))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'fadeIn second'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'fadeIn second'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'fadeIn second'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'fadeIn second'}))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class': 'fadeIn second'}))

    class Meta:
        model = CustomUser
        fields = ('avatar', 'username', 'email', 'first_name', 'last_name', 'date_of_birth')