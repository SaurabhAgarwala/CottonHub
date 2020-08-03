import numpy as np
import pandas as pd
from datetime import datetime
from itertools import product
import json
import time
import pickle

from utils.metrics import get_scores, print_scores
from utils.create_dir import create_dir

class BaseModel:
    def __init__(self, day_num = 1, use_diff = False):
        self.model = None
        self.params = {}
        self.day_num = day_num
        self.model_name = ''
        self.use_diff = use_diff

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

    def output(self, X):
        return np.zeros(X.shape[0])

    def fit(self, train_X, train_Y, val_X, val_Y, verbose):
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

    def predict_price(self, X, Y):
        preds = self.output(X)
        true = Y[:, 0]
        return get_scores(true, preds)
    
    def predict_diff(self, X, Y):
        preds = self.output(X)
        prev_prices = Y[:, 1]
        preds = (np.multiply(prev_prices, 1 + preds)) / (1 - (self.day_num - 1) * preds)
        true = Y[:, 2]
        return get_scores(true, preds)
    
    def evaluate_price(self, X, Y, title):
        scores = self.predict_price(X, Y)
        print_scores(scores, title)
    
    def evaluate_diff(self, X, Y, title):
        scores = self.predict_diff(X, Y)
        print_scores(scores, title)

    def forecast_price(self, X):
        preds = self.output(X)[0]
        return preds

    def forecast_diff(self, X, prev_prices):
        preds = self.output(X)[0]
        preds = (prev_prices * (1 + preds)) / (1 - (self.day_num - 1) * preds)
        return preds

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
            for train_X, train_Y, val_X, val_Y, test_X, test_Y in datagen.extract_data():
                self.fit(train_X, train_Y, val_X, val_Y, verbose = False)
                if(self.use_diff == True):
                    scores_MAPE += self.predict_diff(test_X, test_Y)['MAPE']
                else:
                    scores_MAPE += self.predict_price(test_X, test_Y)['MAPE']
            scores_MAPE /= datagen.n_splits
            params_scores[param] = scores_MAPE
        best_param = sorted(params_scores.items(), key = lambda x: x[1], reverse = False)[0][0]
        best_param = dict(zip(params, best_param))
        if(verbose == True):
            print("Best Param: ", best_param)
        self.set_params(best_param)
        self.save(datagen.cat)
        stop = time.time()
        print(f"Time Taken: {((stop - start) / 60):.1f} min.")

    def save(self, cat):
        if(self.use_diff == True):
            model_name = f"{self.model_name}_Diff"
        else:
            model_name = self.model_name
        create_dir(f"./data/Model_Weights/{model_name}/{cat}")
        with open(f"./data/Model_Weights/{model_name}/{cat}/model_{self.day_num}.json", 'w') as save_file:
            json.dump(self.params, save_file)
    
    def load(self, cat):
        if(self.use_diff == True):
            model_name = f"{self.model_name}_Diff"
        else:
            model_name = self.model_name
        with open(f"./data/Model_Weights/{model_name}/{cat}/model_{self.day_num}.json", 'r') as load_file:
            self.params = json.load(load_file)
    
    def save_model(self, cat, day_num, model_num):
        if(self.use_diff == True):
            model_name = f"{self.model_name}_Diff"
        else:
            model_name = self.model_name
        create_dir(f'./data/Saved_Models/{model_name}/{cat}/')
        with open(f"./data/Saved_Models/{model_name}/{cat}/day_{day_num}_model_{model_num}.pkl", 'wb') as save_file:
            pickle.dump(self.model, save_file)
    
    def load_model(self, cat, day_num, model_num):
        if(self.use_diff == True):
            model_name = f"{self.model_name}_Diff"
        else:
            model_name = self.model_name
        with open(f"./data/Saved_Models/{model_name}/{cat}/day_{day_num}_model_{model_num}.pkl", 'rb') as load_file:
            self.model = pickle.load(load_file)