from django.shortcuts import render
from .create_data import create_nodes
from django.http import HttpResponse
from tdata import local

# Create your views here.
def create(request):
    create_nodes(local.query_index_table())
    return HttpResponse('operation complete')
