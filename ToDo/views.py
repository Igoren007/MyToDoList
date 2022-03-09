from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from ToDo.forms import LoginCustomUserForm, RegisterCustomUserForm, CustomUserEditForm, TaskCreateForm
from ToDo.models import Task

home_menu = {'current': 'Текущие',
             'done': 'Законченные',
             'all': 'Все задачи',
             'statistic': 'Статистика'
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


def create_task(request):
    """
        Создание новой задачи
    """
    if request.POST:
        task_create_form = TaskCreateForm(request.POST, instance=request.user)
        if task_create_form.is_valid():
            #task_create_form.instance.user_id = request.user.id
            #task_create_form.save()
            title = request.POST['title']
            descr = request.POST['descr']
            priority = request.POST['priority']
            print(title, descr, priority)
            Task.objects.create(title=title, descr=descr, priority=priority)
            print('after save')
            return redirect('home')
    else:
        task_create_form = TaskCreateForm(instance=request.user)
        print('else')
    return render(request, 'ToDo/create_task.html', {'task_create_form': task_create_form, 'menu': home_menu})

@login_required
def home(request):
    return render(request, 'ToDo/home.html', {'menu': home_menu})


def get_user_edit(request):
    """
    Изменение данных пользователя
    """
    if request.POST:
        user_edit_form = CustomUserEditForm(request.POST, request.FILES, instance=request.user)
        if user_edit_form.is_valid():
            user_edit_form.save()
            return redirect('user_settings')
    else:
        user_edit_form = CustomUserEditForm(instance=request.user)
    return render(request, 'ToDo/user_settings.html', {'user_edit_form': user_edit_form, 'menu': home_menu})


class RegisterUser(CreateView):
    form_class = RegisterCustomUserForm
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
    form_class = LoginCustomUserForm
    template_name = 'ToDo/login.html'

    def get_success_url(self):
        return reverse_lazy('home')

# class TaskCreate(CreateView):
#     form_class = TaskCreateForm
#     template_name = 'ToDo/create_task.html'
#     success_url = reverse_lazy('home')
#
#     def form_valid(self, form):
#         form.instance.user_id = self.request.user.id
#         return super(TaskCreate, self).form_valid(form)