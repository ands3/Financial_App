# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 18:27:24 2020

@author: andyz
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage')
    ]