import numpy as np
import pandas as pd
from datetime import datetime
from sklearn.model_selection import StratifiedShuffleSplit

class extract_XY:
    def __init__(self, data, use_diff = False):
        self.data = data
        self.use_diff = use_diff

    def extract_forecast_X(self, idx):
        feat_cols = [x for x in self.data.columns if 'feat_' in x]
        today_date = self.data.loc[idx[0]]['Date']
        X = self.data.loc[idx][feat_cols].values
        if(self.use_diff == False):
            return X, today_date
        else:
            prev_price = self.data.loc[idx[0]]['Prev_Modal_Price']
            return X, prev_price, today_date

    def extract_XY(self, idx):
        feat_cols = [x for x in self.data.columns if 'feat_' in x]
        X = self.data.loc[idx][feat_cols].values
        if(self.use_diff == False):
            Y = self.data.loc[idx]['Modal_Price']
            Y = np.expand_dims(Y, axis = 1)
        else:
            Y = self.data.loc[idx]['Modal_Price_Diff']
            prev_prices = self.data.loc[idx]['Prev_Modal_Price']
            true_prices = self.data.loc[idx]['Modal_Price']
            Y = np.column_stack((Y, prev_prices))
            Y = np.column_stack((Y, true_prices))
        return X, Y
        
class split_data:
    
    # (Train_Perc + Val_Perc) = 100
    # (Train + Val)_Perc + Test_Perc = 100
    def __init__(self, data, test_perc = 10, val_perc = 10, n_splits = 5):
        self.data = data
        self.test_perc = test_perc
        self.val_perc = val_perc
        self.n_splits = n_splits
    
    def extract_train_val_test(self, forecast_len = 7):
        idx = np.arange(self.data.shape[0] - 1)
        test_strat_splits = StratifiedShuffleSplit(n_splits = self.n_splits, test_size = self.test_perc / 100)
        val_strat_splits = StratifiedShuffleSplit(n_splits = 1, test_size = self.val_perc / 100)
        train_val_test_year = self.data.loc[idx]['Date'].apply(lambda x: 1 if x.date().year > 2015 else 0)
        for train_val_idx, test_idx in test_strat_splits.split(idx, train_val_test_year):
            test_IDX = idx[test_idx]
            train_val_IDX = idx[train_val_idx]
            train_val_year = train_val_test_year[train_val_idx]
            for train_idx, val_idx in val_strat_splits.split(train_val_IDX, train_val_year):
                train_IDX = train_val_IDX[train_idx]
                val_IDX = train_val_IDX[val_idx]
                yield train_IDX, val_IDX, test_IDX

class data_gen:
    def __init__(self, data, cat, test_perc = 10, val_perc = 10, n_splits = 5, use_diff = False):
        self.cat = cat
        self.cat_data = data[data['Category'] == cat]
        self.cat_data = self.cat_data.reset_index(drop = True)
        self.cat_data = self.cat_data.sort_values(by = 'Date')
        self.test_perc = test_perc
        self.val_perc = val_perc
        self.n_splits = n_splits
        self.use_diff = use_diff
        self.cat_extract_XY = extract_XY(self.cat_data, use_diff = self.use_diff)
    
    def extract_data(self):
        split = split_data(self.cat_data, test_perc = self.test_perc, val_perc = self.val_perc, n_splits = self.n_splits)
        for train_idx, val_idx, test_idx in split.extract_train_val_test():
            train_X, train_Y = self.cat_extract_XY.extract_XY(train_idx)
            val_X, val_Y = self.cat_extract_XY.extract_XY(val_idx)
            test_X, test_Y = self.cat_extract_XY.extract_XY(test_idx)
            yield train_X, train_Y, val_X, val_Y, test_X, test_Y
    
    def extract_forecast_data(self):
        return self.cat_extract_XY.extract_forecast_X([self.cat_data.shape[0] - 1])
        
class batch_gen:
    def __init__(self, batch_size):
        self.batch_size = batch_size
    
    def extract_batches(self, X, Y):
        idx = np.arange(X.shape[0])
        np.random.shuffle(idx)
        num_batches = (len(idx) // self.batch_size) + 1
        for batch_num in range(num_batches):
            batch_start = batch_num * self.batch_size
            batch_stop = batch_num * self.batch_size + self.batch_size
            batch_X = X[batch_start: batch_stop, ]
            batch_Y = Y[batch_start: batch_stop, ]
            yield batch_X, batch_Y