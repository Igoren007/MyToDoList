from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from ToDo.forms import RegisterUserForm


def index(request):
    return render(request, 'ToDo/index.html')


def login(request):
    return render(request, 'ToDo/login.html')


def register(request):
    return render(request, 'ToDo/register.html')


def home(request):
    return render(request, 'ToDo/home.html')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    # шаблон для отображения формы
    template_name = 'ToDo/register.html'
    # куда перенаправляем при успешной регистрации
    success_url = reverse_lazy('login')

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     c_def = self.get_user_context(title="Регистрация")
    #     return dict(list(context.items()) + list(c_def.items()))