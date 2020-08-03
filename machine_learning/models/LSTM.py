import numpy as np
import pandas as pd
from datetime import datetime

from utils.create_dir import create_dir
from preprocess.data_gen import data_gen

import tensorflow as tf
from tensorflow.keras import Input
from tensorflow.keras.models import Model
from tensorflow.keras.layers import *
from tensorflow.keras.callbacks import EarlyStopping

from models.BaseModel import BaseModel

class LSTM_Model(BaseModel):
    def __init__(self, day_num, use_diff):
        super().__init__(day_num, use_diff)
        self.model_name = "LSTM"
        self.day_feats = [15, 14, 13, 12, 11, 10, 9][day_num - 1]
        self.daydiff_feats = [14, 13, 12, 11, 10, 9, 8][day_num - 1]
        self.tsfresh_day_feats = [246, 251, 242, 244, 238, 205, 195][day_num - 1]
        self.tsfresh_daydiff_feats = [152, 149, 152, 143, 135, 141, 141][day_num - 1]
        self.date_feats = [82, 82, 82, 82, 82, 82, 82][day_num - 1]

    def set_model(self):
        input_layer = Input(shape = (self.day_feats + self.daydiff_feats + self.tsfresh_day_feats + self.tsfresh_daydiff_feats + self.date_feats, ))
        
        split1 = self.day_feats
        split2 = split1 + self.date_feats
        split3 = split2 + self.daydiff_feats
        split4 = split3 + self.tsfresh_day_feats
        split5 = split4 + self.tsfresh_daydiff_feats

        day_inputs = input_layer[:, split1:0:-1]
        day_inputs = Reshape((self.day_feats, 1))(day_inputs)
        day_lstm = Flatten()(GRU(self.params['hidden_size'], return_sequences = True)(day_inputs))
        
        daydiff_inputs = input_layer[:, split3:split2:-1]
        daydiff_inputs = Reshape((self.daydiff_feats, 1))(daydiff_inputs)
        daydiff_lstm = Flatten()(GRU(self.params['hidden_size'], return_sequences = True)(daydiff_inputs))
        
        tsfresh_day_inputs = input_layer[:, split3: split4]
        tsfresh_day_dense = Dense(100, activation = 'relu')(tsfresh_day_inputs)
        tsfresh_day_dense = Dense(50, activation = 'relu')(tsfresh_day_dense)
        tsfresh_day_dense = Dense(self.params['hidden_size'], activation = 'relu')(tsfresh_day_dense)
        
        tsfresh_daydiff_inputs = input_layer[:, split4: split5]
        tsfresh_daydiff_dense = Dense(100, activation = 'relu')(tsfresh_daydiff_inputs)
        tsfresh_daydiff_dense = Dense(50, activation = 'relu')(tsfresh_daydiff_dense)
        tsfresh_daydiff_dense = Dense(self.params['hidden_size'], activation = 'relu')(tsfresh_daydiff_dense)
        
        date_inputs = input_layer[:, split1: split2]
        date_dense = Dense(50, activation = 'relu')(date_inputs)
        date_dense = Dense(self.params['hidden_size'], activation = 'relu')(date_dense)
        
        concat_layer = Concatenate()([day_lstm, daydiff_lstm, tsfresh_day_dense, tsfresh_daydiff_dense, date_dense])
        inter_layer = Dense(50, activation = 'relu')(concat_layer)
        inter_layer = Dense(10, activation = 'relu')(inter_layer)
        output_layer = Dense(1)(inter_layer)
        
        self.model = Model(inputs = [input_layer], outputs = [output_layer])
        self.model.compile(optimizer = 'Adam', loss = 'mean_squared_error', metrics = ["mean_squared_error"])
    
    def set_params(self, params = {}):
        self.params = params

    def output(self, X):
        return self.model.predict(X)

    def fit(self, train_X, train_Y, val_X, val_Y, verbose = False):
        self.set_model()
        early_stop = EarlyStopping(monitor = 'val_loss', patience = 5)
        self.model.fit(train_X, train_Y[:, 0], validation_data = (val_X, val_Y[:, 0]), epochs = 500, batch_size = 128, verbose = False, callbacks = [early_stop])

