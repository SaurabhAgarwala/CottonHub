import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import json
import time
import os

import warnings
warnings.filterwarnings("ignore")

from models.ARIMA import ARIMA_Model
from models.SARIMA import SARIMA_Model
from models.Exp_Smoothing import Exp_Smoothing_Model

from utils.create_dir import create_dir

def forecast_day(model, cat, use_diff = False, squeeze_type = 'Daily', squeeze_factor = 7):
    forecasts = []
    try:
        model.load_model(cat)
        with open(f'./data/Forecast_Inputs/TS_Forecast_Inputs/today_date.txt', 'r') as load_file:
            today_date = datetime.strptime(load_file.readlines()[0], '%d/%m/%Y')
        forecast_dates = [today_date + timedelta(squeeze_factor * x) for x in range(1, 8)]
        if(use_diff == False):
            forecasts = model.forecast_price()
        else:
            with open(f'./data/Forecast_Inputs/TS_Forecast_Inputs/{squeeze_type}/prev_price_{cat}.txt', 'r') as load_file:
                prev_price = float(load_file.readlines()[0])
            forecasts = model.forecast_diff(prev_price)
        return list(zip(forecast_dates, forecasts)), True
    except:
        return None, False

all_models = {
    'ARIMA': ARIMA_Model,
    'Exp_Smoothing': Exp_Smoothing_Model,
    'SARIMA': SARIMA_Model
}

def TS_forecast_cat_prices(cat):
    squeeze_type_factor = [('Weekly', 7), ('Monthly', 30)]
    for squeeze_type, squeeze_factor in squeeze_type_factor:
        use_models = [
            ('ARIMA', False),
            ('Exp_Smoothing', False),
            ('SARIMA', False)
        ]
        for model_code, USE_DIFF in use_models:
            Model = all_models[model_code]

            all_forecasts = []
            model = Model(squeeze_type = squeeze_type, use_diff = USE_DIFF)
            forecasts, is_valid = forecast_day(model, cat, use_diff = USE_DIFF, squeeze_type = squeeze_type, squeeze_factor = squeeze_factor)
            if(is_valid == False):
                if(USE_DIFF == True):
                    check_path = f'./data/Forecasts/{squeeze_type}_Forecasts/{model.model_name}_Diff.csv'
                    if(os.path.isfile(check_path) == True):
                        os.remove(check_path)
                else:
                    check_path = f'./data/Forecasts/{squeeze_type}_Forecasts/{model.model_name}.csv'
                    if(os.path.isfile(check_path) == True):
                        os.remove(check_path)
                continue
            for forecast_date, forecast in forecasts:
                all_forecasts.append([cat, forecast_date, forecast])

            forecasts_df = pd.DataFrame(all_forecasts, columns = ['Category', 'Date', 'Forecast'])
            forecasts_df = forecasts_df.sort_values(by = ['Category', 'Date']).reset_index(drop = True)

            forecasts_df['Date'] = forecasts_df['Date'].apply(lambda x: datetime.strftime(x, '%d/%m/%Y'))
            create_dir(f"./data/Forecasts/{squeeze_type}_Forecasts/")
            if(USE_DIFF == True):
                forecasts_df.to_csv(f'./data/Forecasts/{squeeze_type}_Forecasts/{model.model_name}_Diff_{squeeze_type}.csv', index = False)
            else:
                forecasts_df.to_csv(f'./data/Forecasts/{squeeze_type}_Forecasts/{model.model_name}_{squeeze_type}.csv', index = False)