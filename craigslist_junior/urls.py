# Project level  craigslist_junior/urls.py
from django.urls import include, path

urlpatterns = [
    path('categories/', include('categories.urls')),
]