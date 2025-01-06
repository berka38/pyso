# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import Disease, Medic, Comments

# Register your models here.

@admin.register(Disease)
class PostAdmin(admin.ModelAdmin):
    list_display = ('Title', 'about')
    list_filter = ('tickets',)  # Kategorilere göre filtreleme


@admin.register(Medic)
class PostAdmin(admin.ModelAdmin):
    list_display = ('Title', 'video','about', 'img')
    list_filter = ('illness',)  # Kategorilere göre filtreleme

@admin.register(Comments)
class PostAdmin(admin.ModelAdmin):
    list_display = ('comment', 'user','medic')
    list_filter = ('medic',)  # Kategorilere göre filtreleme


