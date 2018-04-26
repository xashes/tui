from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.homepage, name='homepage'),
    re_path(r'^add_record$', views.add_record, name='add_record'),
]
