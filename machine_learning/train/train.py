import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import json

import warnings
warnings.filterwarnings("ignore")

from preprocess.data_gen import data_gen

from models.Moving_Average import MA_Model
from models.Linear_Regression import LR_Model
from models.Random_Forest import RF_Model
from models.XGBoost import XGB_Model
from models.LightGBM import LGB_Model
from models.LSTM import LSTM_Model

from utils.metrics import print_scores
from utils.create_dir import create_dir

def train_day(Model, DataGen, day_num, hyperparam_tuning = False, verbose = True, params_dict = {}, use_diff = False, max_combos = 50, save_model = False):

    model = Model(day_num = day_num, use_diff = use_diff)
    
    if(hyperparam_tuning == True):
        model.hyperparam_tuning(params_dict, DataGen, verbose = verbose, max_combos = max_combos)
    model.load(DataGen.cat)
    model.set_model()
    
    avg_scores = {'MAE': 0, 'RMSE': 0, 'MAPE': 0, 'SMAPE': 0}
    scores = {}
    model_num = 1
    for train_X, train_Y, val_X, val_Y, test_X, test_Y in DataGen.extract_data():
        model.fit(train_X, train_Y, val_X, val_Y, verbose = verbose)
        if(use_diff == True):
            scores[model_num] = model.predict_diff(test_X, test_Y)
        else:
            scores[model_num] = model.predict_price(test_X, test_Y)
        for key in scores[model_num]:
            avg_scores[key] += (scores[model_num][key] / DataGen.n_splits)
        if(save_model == True):
            model.save_model(DataGen.cat, day_num, model_num)
            model_num = model_num + 1
    if(verbose == True):
        print_scores(avg_scores, "\nFinal Test Results")
    return model, scores

def train(model_code, USE_DIFF = False, HYPERPARAM_TUNING = True, SAVE_SCORES = False, TEST_PERC = 15, VAL_PERC = 10, N_SPLITS = 10, MAX_COMBOS = 50, VERBOSE = False):
    
    all_models = {
        'MA': MA_Model,
        'LR': LR_Model,
        'RF': RF_Model,
        'XGB': XGB_Model,
        'LGB': LGB_Model,
        'LSTM': LSTM_Model
    }

    all_params_dict = {
        'MA': {
            'n': [1, 2, 3, 4, 5, 6, 7]
        },
        'LR': {
            'fit_intercept': [True, False]
        },
        'RF': {
            'n_estimators': [100, 150],
            'max_depth': [None, 5, 10],
            'min_samples_split': [2, 3],
            'min_samples_leaf': [1, 2],
            'max_features': ['sqrt', 'log2'],
            'n_jobs': [-1]
        },
        'XGB': {
            'eta': [0.3, 0.5, 0.1],
            'gamma': [0, 1],
            'verbosity': [0],
            'max_depth': [3, 6, 9],
            'min_child_weight': [1, 2],
            'max_delta_step': [0, 4, 8],
            'colsample_bytree': [0, 0.5],
            'lambda': [1, 2],
            'objective': ['reg:squarederror', 'reg:linear', 'reg:squaredlogerror']
        },
        'LGB': {
            'objective': ['regression'],
            'num_iterations': [100, 150, 200],
            'learning_rate': [0.1, 0.05],
            'num_leaves': [15, 31, 63],
            'max_depth': [4, 6, 8],
            'min_data_in_leaf': [20, 10, 30],
            'feature_fraction': [1, 0.5],
            'verbosity': [-1],
            'metric': ['mape']
        },
        'LSTM': {
            'hidden_size': [5, 10, 15]
        }
    }

    Model = all_models[model_code]
    if(model_code in all_params_dict):
        params_dict = all_params_dict[model_code]
    else:
        params_dict = {}

    if(HYPERPARAM_TUNING == True):
        TEST_PERC = 20
        VAL_PERC = 15
        N_SPLITS = 1
        VERBOSE = True

    all_scores = {}
    for day_num in range(1, 8):
        print(f"\nDay Number {day_num}")
        all_scores[day_num] = {}
        data = pd.read_csv(f'./data/Training_Data/final_{day_num}.csv', parse_dates = ['Date'], date_parser = lambda x: datetime.strptime(x, '%d/%m/%Y'))

        cats = list(data['Category'].unique())
        for cat in cats:
            print(f"\n\nCategory: {cat}")
            DataGen = data_gen(data, cat, test_perc = TEST_PERC, val_perc = VAL_PERC, n_splits = N_SPLITS, use_diff = USE_DIFF)
            model, all_scores[day_num][cat] = train_day(Model, DataGen, day_num = day_num, hyperparam_tuning = HYPERPARAM_TUNING, verbose = VERBOSE, params_dict = params_dict, use_diff = USE_DIFF, max_combos = MAX_COMBOS, save_model = SAVE_SCORES)

    if(SAVE_SCORES == True):
        create_dir(f"./data/Model_Scores/")
        if(USE_DIFF == True):
            with open(f"./data/Model_Scores/{model.model_name}_Diff.json", 'w') as save_file:
                json.dump(all_scores, save_file)
        else:
            with open(f"./data/Model_Scores/{model.model_name}.json", 'w') as save_file:
                json.dump(all_scores, save_file)