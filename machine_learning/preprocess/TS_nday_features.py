import numpy as np
import pandas as pd
from datetime import datetime

def TS_nday_features(data):
    n = len([x for x in data.columns if 'group_' in x])
    squeeze_factor = int([x for x in data.columns if 'group_' in x][0].split('_')[1])
    for i in range(1, n):
        data[f'groupdiff_{squeeze_factor}_{i}'] = (data[f'group_{squeeze_factor}_{i}'] - data[f'group_{squeeze_factor}_{i+1}']) / data[f'group_{squeeze_factor}_{i+1}']
    data = data.fillna(-10000)
    return data
