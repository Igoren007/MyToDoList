from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('login/', login, name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
]