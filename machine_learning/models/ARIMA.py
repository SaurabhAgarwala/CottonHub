import numpy as np
import pandas as pd
from datetime import datetime
import pickle

from utils.create_dir import create_dir

from statsmodels.tsa.arima.model import ARIMA

from models.TS_BaseModel import TS_BaseModel

class ARIMA_Model(TS_BaseModel):
    def __init__(self, use_diff, squeeze_type):
        super().__init__(use_diff, squeeze_type)
        self.model_name = "ARIMA"

    def set_model(self):
        pass
    
    def set_params(self, params = {}):
        self.params = params

    def output(self, num_forecasts = 7):
        return self.model.forecast(num_forecasts)
        
    def fit(self, train, verbose = False):
        self.model = ARIMA(train, **self.params)
        self.model = self.model.fit()
    
    def save_model(self, cat):
        if(self.use_diff == True):
            model_name = f"{self.model_name}_Diff"
        else:
            model_name = self.model_name
        create_dir(f'./data/Saved_Models/{model_name}/{cat}')
        self.model.save(f"./data/Saved_Models/{model_name}/{cat}/model_{self.squeeze_type}.pkl", remove_data = True)