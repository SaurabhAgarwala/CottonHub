import numpy as np
import pandas as pd
from datetime import datetime

from statsmodels.tsa.holtwinters import ExponentialSmoothing

from utils.create_dir import create_dir

from models.TS_BaseModel import TS_BaseModel

class Exp_Smoothing_Model(TS_BaseModel):
    def __init__(self, use_diff, squeeze_type):
        super().__init__(use_diff, squeeze_type)
        self.model_name = "Exp_Smoothing"

    def set_model(self):
        pass
    
    def set_params(self, params = {}):
        self.params = params

    def output(self, num_forecasts = 7):
        return self.model.forecast(num_forecasts)
        
    def fit(self, train, verbose = False):
        if(self.squeeze_type == 'Daily'):
            seasonal_periods = 7
        elif(self.squeeze_type == 'Weekly'):
            seasonal_periods = 4
        else:
            seasonal_periods = 12
        self.model = ExponentialSmoothing(train, trend = 'add', seasonal = 'add', seasonal_periods = seasonal_periods)
        self.model = self.model.fit(**self.params)
        