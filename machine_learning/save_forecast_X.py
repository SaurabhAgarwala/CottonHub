import numpy as np
import pandas as pd
from datetime import datetime

from utils.create_dir import create_dir
from preprocess.data_gen import data_gen

TEST_PERC = 15
VAL_PERC = 10
N_SPLITS = 5
USE_DIFF = True

for day_num in range(1, 8):
    data = pd.read_csv(f'./data/Training_Data/final_{day_num}.csv', parse_dates = ['Date'], date_parser = lambda x: datetime.strptime(x, '%d/%m/%Y'))
    create_dir(f'./data/Forecast_Inputs/Regr_Forecast_Inputs/Day_{day_num}/')
    cats = list(data['Category'].unique())
    for cat in cats:
        DataGen = data_gen(data, cat, test_perc = TEST_PERC, val_perc = VAL_PERC, n_splits = N_SPLITS, use_diff = USE_DIFF)
        forecast_X, prev_price, forecast_date = DataGen.extract_forecast_data()
        with open(f'./data/Forecast_Inputs/Regr_Forecast_Inputs/Day_{day_num}/forecast_X_{cat}.npy', 'wb') as save_file:
            np.save(save_file, forecast_X)
        if(day_num == 1):
            with open(f'./data/Forecast_Inputs/Regr_Forecast_Inputs/prev_price_{cat}.txt', 'w') as save_file:
                save_file.writelines(str(prev_price))
    with open(f'./data/Forecast_Inputs/Regr_Forecast_Inputs/Day_{day_num}/forecast_date.txt', 'w') as save_file:
        save_file.writelines(datetime.strftime(forecast_date, '%d/%m/%Y'))