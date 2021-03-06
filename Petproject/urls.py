"""Petproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.views.generic import RedirectView
from django.urls import include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('catalog/', include('catalog.urls')),
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# include() использован чтобы добавлять URL из каталога приложения 
# из модуля views импортировать функцию hello. символ точки говорит о том, что модуль views находится в той же папке, что и файл urls.py
# from .views import hello
# Пошаговое добавление в данном случае необходимо для пошагового разделения для понимания
# Добавлены URL соотношения, чтобы перенаправить запросы с корневового URL, на URL приложения
# static() использован чтобы добавить соотношения для статических файлов
# Только на период разработки











