import numpy as np
import pandas as pd
from datetime import datetime

def nday_features(data, day_num = 1):
    n = len([x for x in data.columns if 'day_' in x])
    data = data[(data['Forecast_Num'] == 0) | (data['Forecast_Num'] == day_num)]
    data = data.drop([f'day_{x+1}' for x in range(day_num-1)], axis = 1)
    data['Modal_Price_Diff'] = (data['Modal_Price'] - data[f'day_{day_num}']) / ((day_num - 1) * data['Modal_Price'] + data[f'day_{day_num}'])
    for i in range(day_num, n):
        data[f'daydiff_{i}'] = (data[f'day_{i}'] - data[f'day_{i+1}']) / data[f'day_{i+1}']
    return data