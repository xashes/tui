from django.shortcuts import render, redirect

# Create your views here.
def kline(request):
    return render(request, 'kline.html')
