from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    avatar = models.ImageField(
        blank=True,
        verbose_name='Avatar',
        upload_to=f'media/',
        default='../static/ToDo/images/default.png'
    )
    date_of_birth = models.DateField(blank=True, null=True)