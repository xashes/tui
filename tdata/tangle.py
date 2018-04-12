import talib
import numpy as np
from sklearn.preprocessing import MinMaxScaler


def tangle(df):
    closes = df.close.values.astype(np.float64)
    df['ma5'] = talib.EMA(closes, 5)
    df['ma10'] = talib.EMA(closes, 10)
    df['ma20'] = talib.EMA(closes, 20)
    df['ma30'] = talib.EMA(closes, 30)

    columns = ['ma5', 'ma10', 'ma20', 'ma30']
    df = df.dropna()

    df['std'] = df[columns].std(axis='columns', ddof=0, numeric_only=True)
    columns.extend(['open', 'close', 'high', 'low', 'std'])
    scaler = MinMaxScaler()
    df[columns] = scaler.fit_transform(df[columns].values)

    return df
