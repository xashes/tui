from django.shortcuts import render, redirect
from . import charts
from tdata import local

REMOTE_HOST = 'https://pyecharts.github.io/assets/js'


# Create your views here.
def chart(request):
    symbol = '000001.SH'
    if request.method == 'POST':
        symbol = request.POST.get('symbol', '')
    bar = local.daily(symbol)
    grids = charts.grids(bar)
    zen = charts.brush(bar)
    context = dict(
        chart=zen.render_embed(),
        host=REMOTE_HOST,
        script_list=grids.get_js_dependencies())
    return render(request, 'chart.html', context)
