# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import Medic

# Register your models here.

@admin.register(Medic)
class PostAdmin(admin.ModelAdmin):
    list_display = ('Title', 'video', 'img', 'user')
    list_filter = ('tickets',)  # Kategorilere göre filtreleme


