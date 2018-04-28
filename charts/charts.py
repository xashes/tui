from pyecharts import Kline, Bar
from pyecharts import Grid


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
