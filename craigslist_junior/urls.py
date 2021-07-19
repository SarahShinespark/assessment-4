# Project level  craigslist_junior/urls.py
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='home_index'),
    path('categories/', include('categories.urls')),
]