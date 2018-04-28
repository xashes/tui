from django.shortcuts import render, redirect
from . import charts
from tdata import local

REMOTE_HOST = 'https://pyecharts.github.io/assets/js'


# Create your views here.
def kline(request):
    symbol = '000001.SH'
    bar = local.daily(symbol)
    grids = charts.grids(bar)
    context = dict(
        chart=grids.render_embed(),
        host=REMOTE_HOST,
        # chart_id=grids.chart_id,
        # my_width='100%',
        # my_height=600,
        # my_option=json_dumps(grids.options),
        script_list=grids.get_js_dependencies())
    return render(request, 'chart.html', context)
