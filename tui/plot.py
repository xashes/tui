import dash_core_components as dcc
import dash_html_components as html
import jaqs.util as jutil
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output

from app import app
from tdata import local

all_symbols = local.query_all_symbol_names()
frequencies = ['M', 'W', 'D', 30, 5, 1]

layout = html.Div([
    html.Div([
        html.Div(
            [
                dcc.Dropdown(
                    id='symbol',
                    options=[{
                        'label': s,
                        'value': s.split(' ')[0]
                    } for s in all_symbols],
                    value='000001.SH'),
                dcc.RadioItems(
                    id='frequency',
                    options=[{
                        'label': str(i),
                        'value': i
                    } for i in frequencies],
                    value='D',
                    labelStyle={
                        'display': 'inline-block'
                    }),
                dcc.RadioItems(
                    id='adjust_mode',
                    options=[{
                        'label': str(i),
                        'value': i
                    } for i in [None, 'hfq']],
                    value=None,
                    labelStyle={
                        'display': 'inline-block'
                    }),
            ],
            style={
                'width': '48%',
                'display': 'inline-block'
            }),
    ]),
    dcc.Graph(id='plot'),
    dcc.Link('Home', href='/')
])


@app.callback(
    Output('plot', 'figure'),[
        Input('symbol', 'value'),
        Input('frequency', 'value'),
        Input('adjust_mode', 'value')
    ]
)
def update_plot(symbol, frequency, adjust_mode):
    df = local.daily(symbol)
    print(df.index[-10:])

    turnover = go.Bar(
        x=df.index,
        y=df['turnover'],
        name='Turnover',
        opacity=0.8,
        marker=dict(
            color=['red']
        )
    )

    kline = go.Candlestick(
        name='Kline',
        x=df.index,
        open=df['open'],
        high=df['high'],
        low=df['low'],
        close=df['close'],
        # yaxis='y3',
        stream=dict(maxpoints=50),
        increasing=dict(line=dict(color='red')),
        decreasing=dict(line=dict(color='green')),
        xcalendar='chinese'
    )

    data = [kline]

    layout = go.Layout(
        xaxis={
            'title': 'Date',
            'rangeslider': {'visible': False},
        },
        # yaxis={'title': 'Volume',
        #        'domain': [0, 0.2]},
        # yaxis2={'title': 'MACD',
        #         'domain': [0.2, 0.4]},
        # yaxis3={
        #     'title': 'Price',
        #     'domain': [0.4, 1],
        # },
        margin={'l': 40,
                'b': 20,
                't': 20,
                'r': 10},
        height=760,
        hovermode='x')


    return {'data': data, 'layout': layout}
