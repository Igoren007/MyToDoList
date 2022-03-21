from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from MyToDoList import settings


class CustomUser(AbstractUser):
    avatar = models.ImageField(
        blank=True,
        verbose_name='Avatar',
        upload_to=f'images/',
        default='../static/ToDo/images/default.png'
    )
    date_of_birth = models.DateField(blank=True, null=True)


class Task(models.Model):
    PRIORITY_LEVEL = (('L', 'low'),
                      ('H', 'hight'),
                      ('M', 'medium'),
                      )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    descr = models.CharField(max_length=500)
    priority = models.CharField(max_length=10, choices=PRIORITY_LEVEL, default='medium')
    is_finished = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    complated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title