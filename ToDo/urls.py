from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path('user_settings/', get_user_edit, name='user_settings'),
    path('create_task/', create_task, name='create_task'),
    path('done_tasks/', done_tasks, name='done_tasks'),
    path('task-edit/<int:pk>', TaskEdit.as_view(), name='task-edit'),
    path('task_delete/<int:pk>', task_delete, name='task_delete'),
    path('task_make_done/<int:pk>', task_make_done, name='task_make_done'),
    path('statistic/', statistic, name='statistic'),
    path('about/', about, name='about'),
]