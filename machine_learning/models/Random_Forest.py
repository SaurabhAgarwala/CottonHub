import numpy as np
import pandas as pd
from datetime import datetime

from sklearn.ensemble import RandomForestRegressor

from models.BaseModel import BaseModel

class RF_Model(BaseModel):
    def __init__(self, day_num, use_diff):
        super().__init__(day_num, use_diff)
        self.model_name = "Random_Forest"

    def set_model(self):
        self.model = RandomForestRegressor(**self.params)
    
    def set_params(self, params = {
        'n_estimators': 100,
        'criterion': 'mse',
        'max_depth': None,
        'min_samples_split': 2,
        'min_samples_leaf': 1,
        'max_features': 'auto'
        }):
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