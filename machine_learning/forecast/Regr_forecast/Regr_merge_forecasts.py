import pandas as pd
import numpy as np
from datetime import datetime
import os
import json

def find_conf_interval(vals, weights, t = 0.95):
    new_vals = np.multiply(vals, weights) * len(vals) / sum(weights)
    return t * np.std(new_vals) / np.sqrt(len(new_vals))

def get_weights(vals):
    new_vals = - (vals - np.mean(vals)) / np.std(vals)
    return np.exp(new_vals) / np.sum(np.exp(new_vals))

def Regr_merge_forecasts(cat):
    N_SPLITS = 10
    
    mape_vals = []
    all_forecasts_files = os.listdir('./data/Forecasts/Daily_Forecasts/')
    all_forecast_data = pd.DataFrame()
    for forecast_file in all_forecasts_files:
        model = forecast_file.split('.')[0]
        forecast_data = pd.read_csv('./data/Forecasts/Daily_Forecasts/' + forecast_file, parse_dates = ['Date'], date_parser = lambda x: datetime.strptime(x, '%d/%m/%Y'))
        with open(f'./data/Model_Scores/{model}.json', 'r') as load_file:
            scores = json.load(load_file)
        if('Daily' not in model):
            for day_num in range(1, 8):
                for n_split in range(1, N_SPLITS + 1):
                    mape_vals.append(scores[str(day_num)][cat][str(n_split)]['MAPE'])
        else:
            mape_vals.extend([scores[cat]['MAPE']] * 7)
        all_forecast_data = pd.concat([all_forecast_data, forecast_data], axis = 0)
    all_forecast_data = all_forecast_data.assign(MAPE = mape_vals)

    forecasts = []
    all_forecast_data['Date'] = all_forecast_data['Date'].apply(datetime.strftime, format = '%d/%m/%Y')
    dates = list(all_forecast_data['Date'].unique())

    cat_forecasts = all_forecast_data[all_forecast_data['Category'] == cat]
    for date in dates:
        cat_date_forecasts = cat_forecasts[cat_forecasts['Date'] == date]
        forecast = cat_date_forecasts['Forecast'].values
        mapes = cat_date_forecasts['MAPE'].values
        weights = get_weights(mapes)
        interval = find_conf_interval(forecast, weights)
        final_forecast = np.sum(np.multiply(forecast, weights) / np.sum(weights))
        lower_bound = final_forecast - interval
        upper_bound = final_forecast + interval
        forecasts.append([date, final_forecast, lower_bound, upper_bound])

    forecast_dict = {}
    for date, forecast_val, lower_bound, upper_bound in forecasts:
        forecast_dict[date] = {'Forecast_Price': format(forecast_val, '.2f'), 'Lower_Bound': format(lower_bound, '.2f'), 'Upper_Bound': format(upper_bound, '.2f')}
    
    return forecast_dict