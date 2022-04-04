# Generated by Django 4.0.3 on 2022-04-04 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0009_task_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('L', 'низкий'), ('M', 'обычный'), ('H', 'высокий')], default='medium', max_length=10),
        ),
    ]