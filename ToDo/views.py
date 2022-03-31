import datetime
import pandas as pd
from datetime import date

from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from ToDo.forms import LoginCustomUserForm, RegisterCustomUserForm, CustomUserEditForm, TaskCreateForm, TaskEditForm, \
    TaskSort, DatePeriodForm

from ToDo.forms import LoginCustomUserForm, RegisterCustomUserForm, CustomUserEditForm, TaskCreateForm

from ToDo.models import Task

home_menu = {'home': 'Главная',
             'done_tasks': 'Выполненные',
             'statistic': 'Статистика'
             }


def index(request):
    return render(request, 'ToDo/index.html')


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
            title = request.POST['title']
            descr = request.POST['descr']
            priority = request.POST['priority']
            user_id = request.user.id
            Task.objects.create(title=title, descr=descr, priority=priority, user_id=user_id)
            return redirect('home')
    else:
        task_create_form = TaskCreateForm(instance=request.user)

    context = {
        'task_create_form': task_create_form,
        'menu': home_menu,
        'title': 'Создание задачи'
    }
    return render(request, 'ToDo/create_task.html', context=context)


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
    """
        Старница отображения выполненных задач
    """
    tasks = Task.objects.filter(user_id=request.user.id, is_finished=True).order_by('created_at').reverse()
    context = {
        'tasks': tasks,
        'menu': home_menu,
        'title': 'Выполненные задачи'
    }
    return render(request, 'ToDo/done_tasks.html', context=context)


@login_required
def task_delete(request, pk):
    """
        Функция удаления задач.
        В шаблоне home.html на задаче есть ссылка с href="{% url 'task_delete' task.id %}"
        По нажатию на нее сюда передается url в виде task_delete/task.id
    """
    try:
        Task.objects.filter(user_id=request.user.id, id=pk).delete()
        return redirect('home')
    except:
        return redirect('home')


@login_required
def task_make_done(request, pk):
    """
        Функция изменения статуса задачи на "выполнено".
        В шаблоне home.html на задаче есть ссылка с href="{% url 'task_make_done' task.id %}"
        По нажатию на нее сюда передается url в виде task_make_done/task.id
    """
    try:
        task = Task.objects.get(id=pk)
        task.is_finished = True
        task.save()
        return redirect('home')
    except:
        return redirect('home')


@login_required
def home(request):
    """
        Домашняя страница пользователя.
    """
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

    context = {
        'menu': home_menu,
        'tasks_active': tasks,
        'tasks_finished': tasks.order_by("-complated_at")[:5],
        'date': current_date,
        'sort_form': sort_form,
        'title': 'Домашняя страница'
    }
    return render(request, 'ToDo/home.html', context=context)


@login_required
def get_user_edit(request):
    """
    Страница редактирования данных пользователя
    """
    if request.POST:
        user_edit_form = CustomUserEditForm(request.POST, request.FILES, instance=request.user)
        if user_edit_form.is_valid():
            user_edit_form.save()
            return redirect('user_settings')
    else:
        user_edit_form = CustomUserEditForm(instance=request.user)

    context = {
        'user_edit_form': user_edit_form,
        'menu': home_menu,
        'title': 'Редактирование данных пользователя'
    }
    return render(request, 'ToDo/user_settings.html', context=context)


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

@login_required
def statistic(request):
    data = dict()
    date_form = DatePeriodForm(request.POST)
    context = {
        'menu': home_menu,
        'date_form': date_form,
        'title': 'Статистика'
    }
    if date_form.is_valid():
        start_date = date_form.cleaned_data.get("start_date")
        end_date = date_form.cleaned_data.get("end_date")
        #прибавляем end_date 1439 мин чтобы установить значение времени в 23:59 текущего дня
        end_date += datetime.timedelta(minutes=1439)

        #выбираем из БД все задачи за указанный промежуток времени
        all_tasks = Task.objects.values('is_finished', 'complated_at').filter(user_id=request.user.id, complated_at__gte=start_date, complated_at__lte=end_date)

#отбираем только выполненные задачи и в графе complated_at оставляем только день-месяц-год
        finished_tasks = []
        for task in all_tasks:
            if task['is_finished'] == True:
                task['complated_at'] = task['complated_at'].strftime("%d %m %Y")
                finished_tasks.append(task)

#используя pandas делаем группировку выполненных задач по дате и считаем их кол-во. формируем набор данных для графика.
        df = pd.DataFrame(finished_tasks)
        #print(df)
        df2 = df.groupby('complated_at').size().reset_index(name='Count')
        #print(df2)
        x_axis = df2.complated_at.to_list()
        y_axis = df2.Count.to_list()
        #print(x_axis, y_axis)

        data['all'] = len(all_tasks)
        data['finished'] = len(finished_tasks)
        data['percent'] = int(100*len(finished_tasks)/len(all_tasks))

        context['data'] = data
        context['x_axis'] = x_axis
        context['y_axis'] = y_axis

    return render(request, 'ToDo/statistic.html', context=context)
