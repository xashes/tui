from django.shortcuts import render, redirect
from . import charts
from django.http import HttpResponse
from django.template import loader
from tdata import local

REMOTE_HOST = 'https://pyecharts.github.io/assets/js'


# Create your views here.
def kline(request):
    symbol = '000001.SH'
    data = local.daily(symbol)
    template = loader.get_template('kline.html')
    kline = charts.kline(data)
    context = dict(
        kline=kline.render_embed(),
        host=REMOTE_HOST,
        script_list=kline.get_js_dependencies())
    return HttpResponse(template.render(context, request))
