from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import remote
from jaqs.data.dataservice import QueryDataError


# Create your views here.
def index(request):
    return render(request, 'index.html')


def update(request):
    try:
        remote.update_database()
    except QueryDataError as qe:
        return HttpResponse(f'{qe}')
    return HttpResponse('Update Success')
