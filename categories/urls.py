#App level  categories/urls.py
#<Server path>/categories/<path>

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]