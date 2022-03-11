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
    path('task-edit/<int:pk>', TaskEdit.as_view(), name='task-edit'),
]