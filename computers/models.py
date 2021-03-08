from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Computer(models.Model):
    title = models.CharField(verbose_name='Название ПК', max_length=200)
    kernel_version = models.CharField(verbose_name='ОС', max_length=300)
    product_type = models.CharField(verbose_name='Вид ОС', max_length=50)
    product_version = models.CharField(verbose_name='Версия ОС', max_length=20)
    processor_type = models.CharField(verbose_name='Процессор', max_length=300)
    physical_memory = models.CharField(verbose_name='Объём ОП', max_length=20)
    video_driver = models.CharField(verbose_name='Видео драйвер', max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Application(models.Model):
    application_name = models.CharField(verbose_name='Название программы', max_length=500)
    application_version = models.CharField(verbose_name='Версия программы', max_length=200)
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE, related_name='applications', null=True)


class Users(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
