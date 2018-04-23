from django.shortcuts import render
from .create_data import create_company_nodes
from django.http import HttpResponse

# Create your views here.
def create(request):
    create_company_nodes()
    return HttpResponse('operation complete')
