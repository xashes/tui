from django.urls import re_path

from . import views

urlpatterns = [
    re_path('^create$', views.create, name='create')
]
