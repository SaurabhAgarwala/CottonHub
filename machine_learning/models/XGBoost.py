import numpy as np
import pandas as pd
from datetime import datetime

import xgboost as xgb

from models.BaseModel import BaseModel

class XGB_Model(BaseModel):
    def __init__(self, day_num, use_diff):
        super().__init__(day_num, use_diff)
        self.model_name = "XGBoost"

    def set_model(self):
        pass
    
    def set_params(self, params = {}):
        self.params = params

    def output(self, X):
        xgb_X = xgb.DMatrix(X)
        return self.model.predict(xgb_X)

    def fit(self, train_X, train_Y, val_X, val_Y, verbose = False):
        xgb_train = xgb.DMatrix(train_X, label = train_Y[:, 0])
        xgb_val = xgb.DMatrix(val_X, label = val_Y[:, 0])
        evallist = [(xgb_train, 'train'), (xgb_val, 'eval')]
        self.model = xgb.train(self.params, xgb_train, 3, evallist, verbose_eval = False)
        if(verbose == True):
            xgb_val = xgb.DMatrix(val_X)
            if(self.use_diff == True):
                self.evaluate_diff(val_X, val_Y, "Validation Results")
            else:
                self.evaluate_price(val_X, val_Y, "Validation Results")
