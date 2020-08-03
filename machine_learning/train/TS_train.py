import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import json
from itertools import product
import time

import warnings
warnings.filterwarnings("ignore")
from statsmodels.tools.sm_exceptions import ConvergenceWarning
warnings.simplefilter('ignore', ConvergenceWarning)

from preprocess.TS_data_gen import TS_data_gen

from models.ARIMA import ARIMA_Model
from models.SARIMA import SARIMA_Model
from models.Exp_Smoothing import Exp_Smoothing_Model

from utils.metrics import print_scores
from utils.create_dir import create_dir

def train_model(Model, DataGen, hyperparam_tuning = False, verbose = True, params_dict = {}, use_diff = False, max_combos = 50, save_model = False, squeeze_type = 'Weekly'):

    model = Model(use_diff = use_diff, squeeze_type = squeeze_type)
    
    if(hyperparam_tuning == True):
        model.hyperparam_tuning(params_dict, DataGen, verbose = verbose, max_combos = max_combos)
    model.load(DataGen.cat)
    model.set_model()
    
    avg_scores = {'MAE': 0, 'RMSE': 0, 'MAPE': 0, 'SMAPE': 0}
    err_cnt = 0
    while(1):
        for train, test, prev_price in DataGen.extract_train_data():
            try:
                model.fit(train, verbose = verbose)
            except Exception as ex:
                print(ex)
                print("***************\nError encountered while fitting!\n***************")
                err_cnt = err_cnt + 1
                if(err_cnt == 10):
                    exit()
                time.sleep(2)
                model.load(DataGen.cat)
                model.set_model()
                avg_scores = {'MAE': 0, 'RMSE': 0, 'MAPE': 0, 'SMAPE': 0}
                continue

            if(use_diff == True):
                score = model.predict_diff(test, prev_price)
            else:
                score = model.predict_price(test)
            for key in score:
                avg_scores[key] += (score[key] / DataGen.n_splits)
        break
    if(save_model == True):
        if(use_diff == True):
            train, _, _ = DataGen.extract_all_data()
        else:
            train, _ = DataGen.extract_all_data()
        try:
            model.fit(train)
            model.save_model(DataGen.cat)
        except Exception as ex:
            print(f"$$$$$$$$$$$$$$$$$$$\n{ex}\nUnable to train...\n$$$$$$$$$$$$$$$$$$$")
    
    if(verbose == True):
        print_scores(avg_scores, "\nFinal Test Results")

    return model, avg_scores

def TS_train(model_code, SQUEEZE_TYPE = 'Weekly', USE_DIFF = False, HYPERPARAM_TUNING = True, SAVE_SCORES = False, N_SPLITS = 10, MAX_COMBOS = 50, VERBOSE = False):
    
    all_models = {
        'ARIMA': ARIMA_Model,
        'SARIMA': SARIMA_Model,
        'Exp_Smoothing': Exp_Smoothing_Model
    }

    if(SQUEEZE_TYPE == 'Daily'):
        seasonal_val = 7
    elif(SQUEEZE_TYPE == 'Weekly'):
        seasonal_val = 4
    else:
        seasonal_val = 12
    all_params_dict = {
        'ARIMA': {'order': list(product([0, 1, 3, 5, 7], [0, 1], [0, 1]))},
        'SARIMA': {'order': list(product([0, 1, 2], [0, 1], [0, 1])), 'seasonal_order': [seasonal_val]},
        'Exp_Smoothing': {'smoothing_level': [0.3, 0.6, 0.9], 'smoothing_slope': [0.3, 0.6, 0.9], 'smoothing_seasonal': [0.3, 0.6, 0.9]}
    }
    
    Model = all_models[model_code]
    if(model_code in all_params_dict):
        params_dict = all_params_dict[model_code]
    else:
        params_dict = {}

    if(HYPERPARAM_TUNING == True):
        N_SPLITS = 5
        VERBOSE = True

    all_scores = {}
    data = pd.read_csv(f'./data/Training_Data/TS_{SQUEEZE_TYPE}_final.csv', parse_dates = ['Today'], date_parser = lambda x: datetime.strptime(x, '%d/%m/%Y'))

    cats = list(data['Category'].unique())
    for cat in cats:
        print(f"Category: {cat}")
        DataGen = TS_data_gen(data, cat, n_splits = N_SPLITS, use_diff = USE_DIFF)
        model, all_scores[cat] = train_model(Model, DataGen, hyperparam_tuning = HYPERPARAM_TUNING, verbose = VERBOSE, params_dict = params_dict, use_diff = USE_DIFF, save_model = SAVE_SCORES, squeeze_type = SQUEEZE_TYPE, max_combos = MAX_COMBOS)

    if(SAVE_SCORES == True):
        create_dir(f"./data/Model_Scores/")
        if(USE_DIFF == True):
            with open(f"./data/Model_Scores/{model.model_name}_Diff_{SQUEEZE_TYPE}.json", 'w') as save_file:
                json.dump(all_scores, save_file)
        else:
            with open(f"./data/Model_Scores/{model.model_name}_{SQUEEZE_TYPE}.json", 'w') as save_file:
                json.dump(all_scores, save_file)