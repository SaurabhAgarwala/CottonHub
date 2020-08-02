import numpy as np
import pandas as pd
from datetime import datetime

from TS_nday_features import TS_nday_features

data = pd.read_csv('./data/Preprocessed_Data/TS_Preprocessed_Daily_Prices.csv', parse_dates = ['Today'], date_parser = lambda x: datetime.strptime(x, '%d/%m/%Y'))
feat_data = TS_nday_features(data)
feat_data['Today'] = feat_data['Today'].apply(lambda x: datetime.strftime(x, '%d/%m/%Y'))
feat_data.to_csv(f'./data/Training_Data/TS_Daily_final.csv', index = False)

data = pd.read_csv('./data/Preprocessed_Data/TS_Preprocessed_Weekly_Prices.csv', parse_dates = ['Today'], date_parser = lambda x: datetime.strptime(x, '%d/%m/%Y'))
feat_data = TS_nday_features(data)
feat_data['Today'] = feat_data['Today'].apply(lambda x: datetime.strftime(x, '%d/%m/%Y'))
feat_data.to_csv(f'./data/Training_Data/TS_Weekly_final.csv', index = False)

data = pd.read_csv('./data/Preprocessed_Data/TS_Preprocessed_Monthly_Prices.csv', parse_dates = ['Today'], date_parser = lambda x: datetime.strptime(x, '%d/%m/%Y'))
feat_data = TS_nday_features(data)
feat_data['Today'] = feat_data['Today'].apply(lambda x: datetime.strftime(x, '%d/%m/%Y'))
feat_data.to_csv(f'./data/Training_Data/TS_Monthly_final.csv', index = False)