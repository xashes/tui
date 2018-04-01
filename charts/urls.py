from django.urls import path

from . import views

urlpatterns = [
    path('kline/', views.kline, name='kline'),
]
