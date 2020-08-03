import numpy as np
import pandas as pd
from datetime import datetime

from models.BaseModel import BaseModel

class MA_Model(BaseModel):
    def __init__(self, day_num, use_diff):
        super().__init__(day_num, use_diff)
        self.model_name = "Moving_Average"

    def set_model(self):
        pass
    
    def set_params(self, params = {'n': 7}):
        self.params = params

    def output(self, X):
        return np.mean(X[:, :self.params['n']], axis = 1)

    def fit(self, train_X, train_Y, val_X, val_Y, verbose = False):
        # No fitting to be done
        if(verbose == True):
            if(self.use_diff == True):
                self.evaluate_diff(val_X, val_Y, "Validation Results")
            else:
                self.evaluate_price(val_X, val_Y, "Validation Results")
