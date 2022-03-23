import datetime
from datetime import date

from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from ToDo.forms import LoginCustomUserForm, RegisterCustomUserForm, CustomUserEditForm, TaskCreateForm, TaskEditForm, \
    TaskSort

from ToDo.forms import LoginCustomUserForm, RegisterCustomUserForm, CustomUserEditForm, TaskCreateForm

from ToDo.models import Task

home_menu = {'home': 'Главная',
             'done_tasks': 'Выполненные',
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

@login_required
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
            user_id = request.user.id
            #print(title, descr, priority)
            Task.objects.create(title=title, descr=descr, priority=priority, user_id=user_id)
            #print('after save')
            return redirect('home')
    else:
        task_create_form = TaskCreateForm(instance=request.user)
        print('else')
    return render(request, 'ToDo/create_task.html', {'task_create_form': task_create_form, 'menu': home_menu})


class TaskEdit(UpdateView):
    template_name = 'ToDo/task-edit.html'
    model = Task
    form_class = TaskEditForm
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = home_menu
        context['title'] = 'Редактирование задачи'
        return context


@login_required
def done_tasks(request):
    tasks = Task.objects.filter(user_id=request.user.id, is_finished=True).order_by('created_at').reverse()
    return render(request, 'ToDo/done_tasks.html', {'menu': home_menu, 'tasks': tasks})


def task_delete(request, pk):
    try:
        Task.objects.filter(user_id=request.user.id, id=pk).delete()
        return redirect('home')
    except:
        return redirect('home')


def task_make_done(request, pk):
    #Task.objects.filter(user_id=request.user.id, id=pk).update(is_finished=True)
    #Task.objects.filter(user_id=request.user.id, id=pk).update(complated_at=date.today().strftime("%d/%m/%y %H:%M"))
    task = Task.objects.get(id=pk)
    task.is_finished = True
    task.save()
    return redirect('home')


@login_required
def home(request):
    current_date = date.today().strftime("%A, %d %B %Y")
    sort_form = TaskSort(request.POST)
    tasks = Task.objects.filter(user_id=request.user.id)

#сортируем задачи по разным критериям
    if sort_form.is_valid():
        needed_sort = sort_form.cleaned_data.get("sort")
        if needed_sort == "date_new":
            tasks = tasks.order_by("-created_at")
        elif needed_sort == "date_old":
            tasks = tasks.order_by("created_at")
        elif needed_sort == "priority":
            tasks = tasks.order_by("priority")

    return render(request, 'ToDo/home.html', {'menu': home_menu, 'tasks_active':tasks, 'tasks_finished':tasks.order_by("-complated_at"), 'date':current_date, 'sort_form': sort_form})


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


def statistic(request):
    return render(request, 'ToDo/statistic.html', {'menu': home_menu})
