from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def kline(request):
    return HttpResponse("<html><title>Kline</title></html>")
