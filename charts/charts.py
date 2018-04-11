import pyecharts as pe


def kline(bar):
    data = bar[['open', 'close', 'low', 'high']]
    kline = pe.Kline(bar['symbol'][0])
    kline.add(
        'day',
        data.index,
        data.values,
        mark_line=['max', 'min'],
        mark_line_valuedim=['highest', 'lowest'],
        bar_width=20,
        is_datazoom_show=True)
    return kline
