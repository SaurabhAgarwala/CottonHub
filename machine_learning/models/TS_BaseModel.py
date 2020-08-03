import numpy as np
import pandas as pd
from datetime import datetime
from itertools import product
import json
import time
import pickle

from utils.metrics import get_scores, print_scores
from utils.create_dir import create_dir

class TS_BaseModel:
    def __init__(self, use_diff = False, squeeze_type = 'Weekly'):
        self.model = None
        self.params = {}
        self.model_name = ''
        self.use_diff = use_diff
        self.squeeze_type = squeeze_type

    ############################################################
    # Model-specific Functions
    ############################################################
    #   --> set_params
    #   --> set_model
    #   --> output
    #   --> fit
    #   --> batch_XY
    ############################################################
    
    def set_params(self, params):
        pass

    def set_model(self):
        pass

    def output(self, num_forecasts = 7):
        return np.zeros(num_forecasts)

    def fit(self, train, verbose):
        pass

    def batch_XY(self, X, Y, batch_size = 32):
        yield np.zeros((batch_size, X.shape[1])), np.zeros(batch_size, Y.shape[1])

    ############################################################
    # Common Functions
    ############################################################
    #   --> predict_price
    #   --> predict_diff
    #   --> evaluate_price
    #   --> evaluate_diff
    #   --> forecast_price
    #   --> forecast_diff
    #   --> hyperparam_tuning
    #   --> save
    #   --> load
    ############################################################

    def predict_price(self, Y, num_forecasts = 7):
        preds = self.output(num_forecasts)
        true = Y.values
        return get_scores(true, preds)
    
    def predict_diff(self, Y, prev_price, num_forecasts = 7):
        preds = self.output(num_forecasts).values
        preds_prices = [prev_price]
        for ind in range(num_forecasts):
            preds_prices.append(preds_prices[ind] * (1 + preds[ind]))
        preds_prices = preds_prices[1:]
        true = Y.values
        return get_scores(true, preds_prices)
    
    def evaluate_price(self, Y, title):
        scores = self.predict_price(Y)
        print_scores(scores, title)
    
    def evaluate_diff(self, Y, prev_price, title):
        scores = self.predict_diff(Y, prev_price)
        print_scores(scores, title)

    def forecast_price(self, num_forecasts = 7):
        preds = self.output(num_forecasts)
        return preds

    def forecast_diff(self, prev_price, num_forecasts = 7):
        preds = self.output(num_forecasts)
        preds_prices = [prev_price]
        for ind in range(num_forecasts):
            preds_prices.append(preds_prices[ind] * (1 + preds[ind]))
        preds_prices = preds_prices[1:]
        return preds_prices

    def hyperparam_tuning(self, params_dict, datagen, max_combos = 50, verbose = False):
        params = list(params_dict.keys())
        params_list = list(product(*(params_dict[x] for x in params_dict)))
        if(len(params_list) > max_combos):
            print("Performing Randomized Search...")
            params_list_idx = np.random.choice(len(params_list), size = max_combos, replace = False)
            params_list = [params_list[x] for x in params_list_idx]
        params_scores = {}
        start = time.time()
        for param in params_list:
            param_dict = dict(zip(params, param))
            self.set_params(param_dict)
            self.set_model()
            scores_MAPE = 0
            for train, test, prev_price in datagen.extract_train_data():
                try:
                    self.fit(train, verbose = False)
                    if(self.use_diff == True):
                        scores_MAPE += self.predict_diff(test, prev_price)['MAPE']
                    else:
                        scores_MAPE += self.predict_price(test)['MAPE']
                except Exception as ex:
                    print(ex)
                    print(f"**********\nError Encountered for {param}!\n**********")
                    scores_MAPE = 1000
            scores_MAPE /= datagen.n_splits
            params_scores[param] = scores_MAPE
        best_param = sorted(params_scores.items(), key = lambda x: x[1], reverse = False)[0][0]
        best_param = dict(zip(params, best_param))
        if(verbose == True):
            print("Best Param: ", best_param)
        self.set_params(best_param)
        self.save(datagen.cat)
        stop = time.time()
        print(f"Time Taken: {((stop - start) / 60.0):.1f} min.")

    def save(self, cat):
        if(self.use_diff == True):
            model_name = f"{self.model_name}_Diff"
        else:
            model_name = self.model_name
        create_dir(f"./data/Model_Weights/{model_name}/{cat}/")
        with open(f"./data/Model_Weights/{model_name}/{cat}/model_{self.squeeze_type}.json", 'w') as save_file:
            json.dump(self.params, save_file)
    
    def load(self, cat):
        if(self.use_diff == True):
            model_name = f"{self.model_name}_Diff"
        else:
            model_name = self.model_name
        with open(f"./data/Model_Weights/{model_name}/{cat}/model_{self.squeeze_type}.json", 'r') as load_file:
            self.params = json.load(load_file)
    
    def save_model(self, cat):
        if(self.use_diff == True):
            model_name = f"{self.model_name}_Diff"
        else:
            model_name = self.model_name
        create_dir(f'./data/Saved_Models/{model_name}/{cat}')
        with open(f"./data/Saved_Models/{model_name}/{cat}/model_{self.squeeze_type}.pkl", 'wb') as save_file:
            pickle.dump(self.model, save_file)
    
    def load_model(self, cat):
        if(self.use_diff == True):
            model_name = f"{self.model_name}_Diff"
        else:
            model_name = self.model_name
        with open(f"./data/Saved_Models/{model_name}/{cat}/model_{self.squeeze_type}.pkl", 'rb') as load_file:
            self.model = pickle.load(load_file)