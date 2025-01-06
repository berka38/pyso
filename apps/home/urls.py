# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    # Matches any html file
    path('Disease/<str:strs>', views.Diseases, name='Diseases'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('illumination', views.illumination, name='illumination'),
    #re_path(r'^.*\.*', views.pages, name='pages'),

    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
