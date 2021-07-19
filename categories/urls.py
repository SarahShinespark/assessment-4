#App level  categories/urls.py
#<Server path>/categories/<path>

from django.urls import path
from . import views

app_name = "categories"

urlpatterns = [
    # Appends to path "categories"
    path('',    views.index, name='categories_all'),
    path('new', views.cat_new, name='categories_new'),
    path('<int:category_id>',        views.cat_detail, name='categories_detail'),
    path('<int:category_id>/edit',   views.cat_edit, name='categories_edit'),
    path('<int:category_id>/delete', views.cat_delete, name='categories_delete'),
    path('<int:category_id>/posts/new',                  views.post_new, name='posts_new'),
    path('<int:category_id>/posts/<int:post_id>',        views.post_detail, name='posts_detail'),
    path('<int:category_id>/posts/<int:post_id>/edit',   views.post_edit, name='posts_edit'),
    path('<int:category_id>/posts/<int:post_id>/delete', views.post_delete, name='posts_delete'),
]
