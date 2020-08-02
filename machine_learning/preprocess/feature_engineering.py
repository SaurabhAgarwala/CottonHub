import numpy as np
import pandas as pd
from datetime import datetime

from nday_features import nday_features
from date_features import date_features
from tsfresh_features import tsfresh_features

data = pd.read_csv('./data/Preprocessed_Data/Preprocessed_Prices.csv', parse_dates = ['Date'], date_parser = lambda x: datetime.strptime(x, '%d/%m/%Y'))

data = date_features(data)
for day_num in range(1, 7 + 1):
    print(f"\n\nDay Num: {day_num}")
    feat_data = nday_features(data, day_num = day_num)
    feat_data = tsfresh_features(feat_data, day_num = day_num)
    feat_data = feat_data.drop('Forecast_Num', axis = 1)
    feat_data['Date'] = feat_data['Date'].apply(lambda x: datetime.strftime(x, '%d/%m/%Y'))
    feat_data.to_csv(f'./data/Training_Data/day_{day_num}.csv', index = False)