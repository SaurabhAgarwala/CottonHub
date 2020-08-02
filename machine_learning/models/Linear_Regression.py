import numpy as np
import pandas as pd
from datetime import datetime

from utils.create_dir import create_dir

from sklearn.linear_model import LinearRegression

from models.BaseModel import BaseModel

class LR_Model(BaseModel):
    def __init__(self, day_num, use_diff):
        super().__init__(day_num, use_diff)
        self.model_name = "Linear_Regression"

    def set_model(self):
        self.model = LinearRegression(**self.params)
    
    def set_params(self, params = {'fit_intercept': True}):
        self.params = params

    def output(self, X):
        return self.model.predict(X)

    def fit(self, train_X, train_Y, val_X, val_Y, verbose = False):
        self.model.fit(train_X, train_Y[:, 0])
        if(verbose == True):
            if(self.use_diff == True):
                self.evaluate_diff(val_X, val_Y, "Validation Results")
            else:
                self.evaluate_price(val_X, val_Y, "Validation Results")