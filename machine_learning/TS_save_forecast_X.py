import numpy as np
import pandas as pd
from datetime import datetime

from utils.create_dir import create_dir
from preprocess.TS_data_gen import TS_data_gen

for SQUEEZE_TYPE in ['Daily', 'Weekly', 'Monthly']:
    N_SPLITS = 5
    USE_DIFF = True

    data = pd.read_csv(f'./data/Training_Data/TS_{SQUEEZE_TYPE}_final.csv', parse_dates = ['Today'], date_parser = lambda x: datetime.strptime(x, '%d/%m/%Y'))
    create_dir(f'./data/Forecast_Inputs/TS_Forecast_Inputs/{SQUEEZE_TYPE}/')
    cats = list(data['Category'].unique())
    for cat in cats:
        DataGen = TS_data_gen(data, cat, n_splits = N_SPLITS, use_diff = USE_DIFF)
        train, prev_price, today_date = DataGen.extract_all_data()
        with open(f'./data/Forecast_Inputs/TS_Forecast_Inputs/{SQUEEZE_TYPE}/prev_price_{cat}.txt', 'w') as save_file:
            save_file.writelines(str(prev_price))
    with open(f'./data/Forecast_Inputs/TS_Forecast_Inputs/today_date.txt', 'w') as save_file:
        save_file.writelines(datetime.strftime(today_date, '%d/%m/%Y'))