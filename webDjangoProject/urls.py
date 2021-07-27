"""webDjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from app01 import views

urlpatterns = [
    url('^login/',views.login),
    url('^sc_list/',views.sc_list),
    url('^sc_add/',views.sc_add),
    url('^sc_del/',views.sc_del),
    url('^sc_edit/',views.sc_edit),
    url('^store_list/',views.store_list),
    url('^store_add/',views.store_add),
    url('^store_del/',views.store_del),
    url('^store_edit/',views.store_edit),
]
