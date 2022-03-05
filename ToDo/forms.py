from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

# представляет форму регистрации
class RegisterUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Имя пользователя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Повтор пароля'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


# представляет форму авторизации
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Логин'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Пароль'}))