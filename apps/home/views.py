# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import matplotlib
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from apps.home.models import Medic
from django.db.models import Sum
from django.contrib.auth.models import User
from apps.authentication.models import Profile
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
import os
from django.conf import settings





from django.core.files.storage import FileSystemStorage

datat = {
    "badges":[
        {
            "name":"deneme",
            "url":"dada",
        },
        {
            "name":"deneme1",
            "url":"dad1",
        },
        {
            "name":"deneme2",
            "url":"dada2",
        },
        {
            "name":"deneme3",
            "url":"dada3",
        },
    ]
}

@login_required(login_url="/login/")
def index(request):

    # profile, created = Profile.objects.get_or_create(user=request.user)
        
        # `balance` değerini güncelle ve profile kaydet
    # profile.balance += 10
    # profile.save()
    #spends = Profile.spends.all()
    profile = Profile.objects.get(user=request.user)
    #for spend in profile.spends.all():
    #   print(f"Tarih: {spend.Date}, Açıklama: {spend.About}, Harcama: {spend.Spend} TL")   

    today = timezone.now().date()

   
    media_items = Medic.objects.all().order_by('-uploaded_at')



    category = request.GET.get('category')  # URL'deki kategori parametresini al
    if category:
        media_items = Medic.objects.filter(tickets=category)  # Kategoriye göre filtreleme
    else:
        media_items = Medic.objects.all()  # Tüm postlar
    all_categories = Medic.objects.values_list('tickets', flat=True).distinct()  # Tüm kategorileri getir









    # Sayfa render edilirken, kullanıcı bilgileri burada alınabilir
    profile = Profile.objects.get(user=request.user)
    
    #dataas= TextFile.objects.filter(user=profile.user)
    
    
    context = {
    'datas': datat,
    'profile' : profile,
    'usersCount':User.objects.count(),
    'segment': 'index',
    'media_items': media_items,
    'all_categories': all_categories,
    'medic_count':Medic.objects.count(),
    }
    

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))
    


def detail(request, id):
    media_items = Medic.objects.get(id=id)

    # Görselleri şablona gönder
    context = {
        'media_items': media_items,
    }

    return render(request, 'home/detail.html', context)