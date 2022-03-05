from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from ToDo.forms import RegisterUserForm, LoginUserForm


home_menu = {'current': 'Текущие',
             'done': 'Законченные',
             'all': 'Все задачи'
             }


def index(request):
    return render(request, 'ToDo/index.html')


# def login(request):
#     return render(request, 'ToDo/login.html')


# def register(request):
#     return render(request, 'ToDo/register.html')


def logout_user(request):
    logout(request)
    return redirect('login')


def home(request):
    return render(request, 'ToDo/home.html', {'menu': home_menu})


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    # шаблон для отображения формы
    template_name = 'ToDo/register.html'
    # куда перенаправляем при успешной регистрации
    success_url = reverse_lazy('login')


    #при успешной регистрации сразу авторизовываемся
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'ToDo/login.html'

    def get_success_url(self):
        return reverse_lazy('home')