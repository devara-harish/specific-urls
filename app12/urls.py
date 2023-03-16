from django.contrib import admin
from django.urls import path
from app12.views import *
app_name='nothing'
urlpatterns=[
    path('pspk/',pspk,name='pspk'),
]
