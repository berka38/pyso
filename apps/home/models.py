# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.utils import timezone
from apps.authentication.models import Profile
# Create your models here.


def user_directory_path(instance, filename):
    # Kullanıcıya özel dizin yolu
    return f'user_{instance.job.Jobs.user.username}/job_{instance.job.id}/{filename}'


class job(models.Model):
    Date = models.DateTimeField(auto_now_add=True)
    Active = models.BooleanField()
    Title = models.CharField(max_length=50)
    About = models.TextField()
    Finish = models.BooleanField()
    Spend = models.IntegerField()
    Income = models.IntegerField()
    Jobs = models.ForeignKey(Profile, related_name="jobs", on_delete=models.CASCADE)
    


class Disease(models.Model):
    Title = models.CharField(max_length=50)
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Yükleme zamanı
    img = models.FileField(upload_to='uploads/')  # Dosyanın yükleneceği klasör
    about = models.TextField()
    CATEGORY_CHOICES = [
        ('boş', 'Lütfen bir hastalık seçiniz'),
        ('fıtık', 'Fıtık'),
        ('donuk', 'Donuk'),
        ('osteoartriti', 'Kireçlenme'),
        ('inme', 'Felç'),
        ('skolyoz', 'Skolyoz'),
        ('romatoid', 'Romatoid'),
        ('parkinson', 'Parkinson'),
    ]

    tickets =  models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,  # Seçenekler eklendi
        default='boş'  # Varsayılan değer
    )
    def __str__(self):
        return f"{self.Title} "

class Medic(models.Model):
    Title = models.CharField(max_length=50)
    video = models.FileField(upload_to='uploads/')  # Dosyanın yükleneceği klasör
    about = models.TextField()
    img = models.FileField(upload_to='uploads/')  # Dosyanın yükleneceği klasör
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Yükleme zamanı
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Kullanıcı bilgisi
    time = models.DurationField()    
    illness = models.ForeignKey(Disease, related_name="illnesss", on_delete=models.CASCADE)
     
    def __str__(self):
        return f"{self.Title}, {self.user.username}. "
    

class Comments(models.Model):
    comment = models.TextField()
    medic = models.ForeignKey(Medic, related_name="medics", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Kullanıcı bilgisi
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Yükleme zamanı
    def __str__(self):
            return f"Yükleyen {self.user.username}, zaman {self.uploaded_at}. "