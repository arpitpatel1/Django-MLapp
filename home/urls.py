from unittest import result
from django.contrib import admin
from django.urls import path
from home import views
import pickletools

urlpatterns = [
     path("", views.index, name='home'),
     path("result/", views.result, name='result')
    ]