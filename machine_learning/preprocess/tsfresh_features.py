import numpy as np
import pandas as pd
from tsfresh import extract_features, select_features
from tsfresh.utilities.dataframe_functions import impute
from datetime import datetime

import sys
sys.path.append('./utils/')
from create_dir import create_dir

import warnings
warnings.filterwarnings("ignore")

def extract_tsfresh_features(data, sel_target = 'Modal_Price', sel_col = 'day_', feature_use = 1):
    sel_cols = [x for x in data.columns if sel_col in x]
    
    features_df = pd.DataFrame()
    feature_target = pd.Series()

    print("Extracting Tsfresh features...")
    cats = list(data['Category'].unique())
    num_iters = int(np.ceil(len(cats) // feature_use))
    for cat_ind in range(num_iters):
        sel_cats = cats[cat_ind * feature_use: (cat_ind + 1) * feature_use]
        sel_data = data[data['Category'].apply(lambda x: (x in sel_cats))]
        
        timeseries = pd.melt(
            sel_data,
            id_vars = ['ID', 'Date'],
            value_vars = sel_cols,
            var_name = 'Day_Num',
            value_name = 'Price')
        timeseries = timeseries.sort_values(by = 'ID')
        timeseries = timeseries.reset_index(drop = True)
        timeseries = timeseries.drop('Day_Num', axis = 1)
        
        Y = sel_data[sel_target]
        Y.index = sel_data['ID']
        
        features = extract_features(timeseries, column_id = 'ID', column_sort = 'Date', n_jobs = 8, disable_progressbar = True)
        impute(features)
        features_df = pd.concat([features_df, features], axis = 0)
        feature_target = feature_target.append(Y, verify_integrity = True)
        
    features_df = select_features(features_df, feature_target, n_jobs = 8)
    feature_names = list(features_df.columns)
    print(f"No. of features: {len(feature_names)}")

    features_df = features_df.reset_index(drop = False)
    features_cols = ['ID']
    features_cols.extend(['tsfresh_'+sel_col+str(x+1) for x in range(len(feature_names))])
    features_df.columns = features_cols

    data = data.merge(features_df, on = 'ID')
    return data, feature_names

def tsfresh_features(data, day_num = 1):
    create_dir(f'./data/Training_Data/')
    
    data, feature_names = extract_tsfresh_features(data, sel_target = 'Modal_Price', sel_col = 'day_')
    print("Done Extracting Tsfresh Price Features\n")
    data, diff_feature_names = extract_tsfresh_features(data, sel_target = 'Modal_Price_Diff', sel_col = 'daydiff_')
    print("Done Extracting Tsfresh Diff Features\n")

    create_dir(f'./data/Training_Data/Tsfresh_Features/')
    feature_names_file = open(f'./data/Training_Data/Tsfresh_Features/day_{day_num}.txt', 'w')
    for name in feature_names:
        feature_names_file.write(name)
        feature_names_file.write('\n')
    feature_names_file.close()

    create_dir(f'./data/Training_Data/Tsfresh_Diff_Features/')
    feature_names_file = open(f'./data/Training_Data/Tsfresh_Diff_Features/day_{day_num}.txt', 'w')
    for name in diff_feature_names:
        feature_names_file.write(name)
        feature_names_file.write('\n')
    feature_names_file.close()

    return data