import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import json
import time

import warnings
warnings.filterwarnings("ignore")

from models.Moving_Average import MA_Model
from models.Linear_Regression import LR_Model
from models.Random_Forest import RF_Model
from models.XGBoost import XGB_Model
from models.LightGBM import LGB_Model

from utils.create_dir import create_dir

def forecast_day(model, cat, day_num, use_diff = False, n_splits = 5):
    forecasts = []
    for model_num in range(n_splits):
        model.load_model(cat, day_num, model_num + 1)
        with open(f'./data/Forecast_Inputs/Regr_Forecast_Inputs/Day_{day_num}/forecast_X_{cat}.npy', 'rb') as load_file:
            forecast_X = np.load(load_file)
        with open(f'./data/Forecast_Inputs/Regr_Forecast_Inputs/Day_{day_num}/forecast_date.txt', 'r') as load_file:
            forecast_date = datetime.strptime(load_file.readlines()[0], '%d/%m/%Y')
        if(use_diff == False):
            forecast = model.forecast_price(forecast_X)
            forecasts.append([forecast_date, forecast])
        else:
            with open(f'./data/Forecast_Inputs/Regr_Forecast_Inputs/prev_price_{cat}.txt', 'r') as load_file:
                prev_price = float(load_file.readlines()[0])
            forecast = model.forecast_diff(forecast_X, prev_price)
            forecasts.append([forecast_date, forecast])
    return forecasts

all_models = {
    'MA': MA_Model,
    'LR': LR_Model,
    'RF': RF_Model,
    'XGB': XGB_Model,
    'LGB': LGB_Model
}

def Regr_forecast_cat_prices(cat):
    use_models = [
        ('XGB', True),
        ('LGB', True),
        ('RF', True)
    ]
    for model_code, USE_DIFF in use_models:
        Model = all_models[model_code]

        N_SPLITS = 10

        all_forecasts = []
        for day_num in range(1, 8):
            model = Model(day_num = day_num, use_diff = USE_DIFF)
            forecasts = forecast_day(model, cat, day_num = day_num, use_diff = USE_DIFF, n_splits = N_SPLITS)
            for forecast_date, forecast in forecasts:
                all_forecasts.append([cat, forecast_date, forecast])

        forecasts_df = pd.DataFrame(all_forecasts, columns = ['Category', 'Date', 'Forecast'])
        forecasts_df = forecasts_df.sort_values(by = ['Category', 'Date']).reset_index(drop = True)

        forecasts_df['Date'] = forecasts_df['Date'].apply(lambda x: datetime.strftime(x, '%d/%m/%Y'))
        create_dir("./data/Forecasts/Daily_Forecasts/")
        if(USE_DIFF == True):
            forecasts_df.to_csv(f'./data/Forecasts/Daily_Forecasts/{model.model_name}_Diff.csv', index = False)
        else:
            forecasts_df.to_csv(f'./data/Forecasts/Daily_Forecasts/{model.model_name}.csv', index = False)
