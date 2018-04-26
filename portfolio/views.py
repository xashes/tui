from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def add_record(request):
    return render(request, 'add_record.html')
