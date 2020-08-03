import numpy as np
import pandas as pd
from datetime import datetime

from statsmodels.tsa.arima.model import ARIMA

from models.TS_BaseModel import TS_BaseModel

class SARIMA_Model(TS_BaseModel):
    def __init__(self, use_diff, squeeze_type):
        super().__init__(use_diff, squeeze_type)
        self.model_name = "SARIMA"

    def set_model(self):
        pass
    
    def set_params(self, params = {}):
        params['seasonal_order'] = (params['order'][0], params['order'][1], params['order'][2], params['seasonal_order'])
        self.params = params

    def output(self, num_forecasts = 7):
        return self.model.forecast(num_forecasts)
        
    def fit(self, train, verbose = False):
        self.model = ARIMA(train, **self.params)
        self.model = self.model.fit()
        