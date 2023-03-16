from django.contrib import admin
from django.urls import path
from app11.views import *
app_name='something'
urlpatterns=[
    path('janasena/',janasena,name='janasena')
]
