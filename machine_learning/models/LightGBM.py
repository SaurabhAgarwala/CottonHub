import numpy as np
import pandas as pd
from datetime import datetime

import lightgbm as lgb

from models.BaseModel import BaseModel

class LGB_Model(BaseModel):
    def __init__(self, day_num, use_diff):
        super().__init__(day_num, use_diff)
        self.model_name = "LightGBM"

    def set_model(self):
        pass
    
    def set_params(self, params = {}):
        self.params = params

    def output(self, X):
        return self.model.predict(X)

    def fit(self, train_X, train_Y, val_X, val_Y, verbose = False):
        lgb_train = lgb.Dataset(train_X, label = train_Y[:, 0], params={'verbosity': -1})
        lgb_val = lgb.Dataset(val_X, label = val_Y[:, 0], params={'verbosity': -1})
        self.model = lgb.train(self.params, lgb_train, 100, early_stopping_rounds = 10, valid_sets = lgb_val, verbose_eval = False)
        if(verbose == True):
            if(self.use_diff == True):
                self.evaluate_diff(val_X, val_Y, "Validation Results")
            else:
                self.evaluate_price(val_X, val_Y, "Validation Results")
