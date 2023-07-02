from django.urls import path,include
from . import views

urlpatterns = [
    path('skill/',views.skill,name='skill')
]