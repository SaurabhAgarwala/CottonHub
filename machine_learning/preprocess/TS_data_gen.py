import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class TS_data_gen:
    def __init__(self, data, cat, test_days = 7, n_splits = 5, use_diff = False):
        self.cat = cat
        self.cat_data = data[data['Category'] == cat].iloc[0]
        self.test_days = test_days
        self.use_diff = use_diff
        self.n_splits = n_splits
    
    def extract_train_data(self):
        if(self.use_diff == False):
            day_cols = [x for x in self.cat_data.index if 'group_' in x]
        else:
            day_cols = [x for x in self.cat_data.index if 'groupdiff_' in x]
        test_day_cols = [x for x in self.cat_data.index if 'group_' in x]
        squeeze_factor = int(day_cols[0].split('_')[1])
        train_vals = self.cat_data[day_cols].values
        train_vals = train_vals[train_vals > -10000]
        test_vals = self.cat_data[test_day_cols].values
        test_vals = test_vals[test_vals > -10000]
        today_date = self.cat_data['Today']
        if(self.use_diff == True):
            prev_day_cols = [x for x in self.cat_data.index if 'group_' in x]
            prev_prices = self.cat_data[prev_day_cols].values
            prev_prices = prev_prices[prev_prices > -10000]
        used_random_idx = []
        for _ in range(self.n_splits):
            while(1):
                random_idx = np.random.randint(test_vals.shape[0] // 2)
                if(random_idx in used_random_idx):
                    continue
                test = test_vals[1 + random_idx: 1 + (random_idx + self.test_days)]
                if(np.var(test) > 100):
                    test = reversed(test)
                    break
            used_random_idx.append(random_idx)
            train_dates = reversed([today_date - timedelta(days = squeeze_factor * (2 + (random_idx + self.test_days) + x)) for x in range(train_vals.shape[0] - self.test_days - 1 - random_idx)])
            test_dates = reversed([today_date - timedelta(days = squeeze_factor * (2 + random_idx + x)) for x in range(self.test_days)])
            train = reversed(train_vals[1 + (random_idx + self.test_days):])
            train_series = pd.Series(train, index = pd.DatetimeIndex(train_dates).to_period(f'{squeeze_factor}D')).astype('float')
            test_series = pd.Series(test, index = pd.DatetimeIndex(test_dates).to_period(f'{squeeze_factor}D')).astype('float')
            if(self.use_diff == False):
                prev_price = None
            else:
                prev_price = prev_prices[1 + (random_idx + self.test_days)]
            yield train_series, test_series, prev_price
    
    def extract_all_data(self):
        if(self.use_diff == False):
            day_cols = [x for x in self.cat_data.index if 'group_' in x]
        else:
            day_cols = [x for x in self.cat_data.index if 'groupdiff_' in x]
        squeeze_factor = int(day_cols[0].split('_')[1])
        train_test = self.cat_data[day_cols].values
        train_test = train_test[train_test > -10000]
        today_date = self.cat_data['Today']
        if(self.use_diff == True):
            prev_day_cols = [x for x in self.cat_data.index if 'group_' in x]
            prev_prices = self.cat_data[prev_day_cols].values
            prev_prices = prev_prices[prev_prices > -10000]
        
        train_dates = reversed([today_date - timedelta(days = squeeze_factor * (x + 1)) for x in range(train_test.shape[0])])
        train = reversed(train_test)
        train = pd.Series(train, index = pd.DatetimeIndex(train_dates).to_period(f'{squeeze_factor}D')).astype('float')
        if(self.use_diff == True):
            prev_price = prev_prices[0]
            return train, prev_price, today_date
        else:
            return train, today_date