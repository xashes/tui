from pyecharts import Kline, Bar, Line
from pyecharts import Grid, Overlap, Page
from features.zen import hist_sum


def grids(data):
    kline = Kline(data.symbol[0])
    kline.add(
        '',
        data.index,
        data.loc[:, ['open', 'close', 'low', 'high']].values,
        mark_line=['max', 'min'],
        mark_line_valuedim=['highest', 'lowest'],
        is_datazoom_show=True,
        datazoom_xaxis_index=[0, 1],
    )

    turnover = Bar()
    turnover.add(
        '',
        data.index,
        data['turnover'].values / pow(10, 9),
        mark_line=['max', 'min'],
        is_datazoom_show=True,
    )

    grid = Grid(page_title=data['symbol'][0], width=1800, height=900)
    grid.add(kline, grid_bottom='40%')
    grid.add(turnover, grid_top='65%')
    grid.show_config()
    return grid


def brush(data):
    data = hist_sum(data)
    kline = Kline()
    kline.add(
        'Kline',
        data.index,
        data.loc[:, ['open', 'close', 'low', 'high']].values,
        mark_line=['max', 'min'],
        mark_line_valuedim=['highest', 'lowest'],
        is_datazoom_show=True,
        datazoom_xaxis_index=[0, 1],
    )
    brush = Line()
    brush.add(
        'Brush',
        data.index,
        data.endpoint.values,
    )
    overlap = Overlap()
    overlap.add(kline)
    overlap.add(brush)

    macd = Bar()
    macd.add(
        'MACD',
        data.index,
        data.hist_sum.values,
    )
    page = Page()
    page.add(overlap)
    page.add(macd)
    return page
