#%%
from train.TS_train import TS_train
from train.train import train

#%%
#train('LGB', USE_DIFF = True, HYPERPARAM_TUNING = True, SAVE_SCORES = False, TEST_PERC = 15, VAL_PERC = 10, N_SPLITS = 5, MAX_COMBOS = 100, VERBOSE = True)
train('LGB', USE_DIFF = True, HYPERPARAM_TUNING = False, SAVE_SCORES = True, TEST_PERC = 15, VAL_PERC = 10, N_SPLITS = 10, MAX_COMBOS = 100, VERBOSE = True)
#train('XGB', USE_DIFF = True, HYPERPARAM_TUNING = True, SAVE_SCORES = False, TEST_PERC = 15, VAL_PERC = 10, N_SPLITS = 5, MAX_COMBOS = 250, VERBOSE = True)
#train('XGB', USE_DIFF = True, HYPERPARAM_TUNING = False, SAVE_SCORES = True, TEST_PERC = 15, VAL_PERC = 10, N_SPLITS = 10, MAX_COMBOS = 100, VERBOSE = False)
#train('RF', USE_DIFF = True, HYPERPARAM_TUNING = True, SAVE_SCORES = False, TEST_PERC = 15, VAL_PERC = 10, N_SPLITS = 5, MAX_COMBOS = 10, VERBOSE = True)
#train('RF', USE_DIFF = True, HYPERPARAM_TUNING = False, SAVE_SCORES = True, TEST_PERC = 15, VAL_PERC = 10, N_SPLITS = 10, MAX_COMBOS = 100, VERBOSE = False)
#train('LSTM', USE_DIFF = True, HYPERPARAM_TUNING = True, SAVE_SCORES = False, TEST_PERC = 15, VAL_PERC = 10, N_SPLITS = 1, MAX_COMBOS = 10, VERBOSE = True)

# Arima Training
#print("ARIMA Training")
#TS_train('ARIMA', 'Daily', USE_DIFF = False, HYPERPARAM_TUNING = True, SAVE_SCORES = False, N_SPLITS = 10, MAX_COMBOS = 50, VERBOSE = True)
#TS_train('ARIMA', 'Weekly', USE_DIFF = False, HYPERPARAM_TUNING = True, SAVE_SCORES = False, N_SPLITS = 10, MAX_COMBOS = 50, VERBOSE = True)
#TS_train('ARIMA', 'Monthly', USE_DIFF = False, HYPERPARAM_TUNING = True, SAVE_SCORES = False, N_SPLITS = 10, MAX_COMBOS = 50, VERBOSE = True)

# Arima Saving
#TS_train('ARIMA', 'Daily', USE_DIFF = False, HYPERPARAM_TUNING = False, SAVE_SCORES = True, N_SPLITS = 10, MAX_COMBOS = 50, VERBOSE = False)
#TS_train('ARIMA', 'Weekly', USE_DIFF = False, HYPERPARAM_TUNING = False, SAVE_SCORES = True, N_SPLITS = 10, MAX_COMBOS = 50, VERBOSE = False)
#TS_train('ARIMA', 'Monthly', USE_DIFF = False, HYPERPARAM_TUNING = False, SAVE_SCORES = True, N_SPLITS = 10, MAX_COMBOS = 50, VERBOSE = False)

# Sarima Training
#TS_train('SARIMA', 'Daily', USE_DIFF = False, HYPERPARAM_TUNING = True, SAVE_SCORES = False, N_SPLITS = 10, MAX_COMBOS = 6, VERBOSE = True)
#TS_train('SARIMA', 'Weekly', USE_DIFF = False, HYPERPARAM_TUNING = True, SAVE_SCORES = False, N_SPLITS = 10, MAX_COMBOS = 50, VERBOSE = True)
#TS_train('SARIMA', 'Monthly', USE_DIFF = False, HYPERPARAM_TUNING = True, SAVE_SCORES = False, N_SPLITS = 10, MAX_COMBOS = 50, VERBOSE = True)

# Sarima Saving
#TS_train('SARIMA', 'Daily', USE_DIFF = False, HYPERPARAM_TUNING = False, SAVE_SCORES = True, N_SPLITS = 10, MAX_COMBOS = 6, VERBOSE = False)
#TS_train('SARIMA', 'Weekly', USE_DIFF = False, HYPERPARAM_TUNING = False, SAVE_SCORES = True, N_SPLITS = 10, MAX_COMBOS = 50, VERBOSE = False)
#TS_train('SARIMA', 'Monthly', USE_DIFF = False, HYPERPARAM_TUNING = False, SAVE_SCORES = True, N_SPLITS = 10, MAX_COMBOS = 50, VERBOSE = False)

# Exp Smoothing Training
#TS_train('Exp_Smoothing', 'Daily', USE_DIFF = False, HYPERPARAM_TUNING = True, SAVE_SCORES = False, N_SPLITS = 10, MAX_COMBOS = 250, VERBOSE = True)
#TS_train('Exp_Smoothing', 'Weekly', USE_DIFF = False, HYPERPARAM_TUNING = True, SAVE_SCORES = False, N_SPLITS = 10, MAX_COMBOS = 250, VERBOSE = True)
#TS_train('Exp_Smoothing', 'Monthly', USE_DIFF = False, HYPERPARAM_TUNING = True, SAVE_SCORES = False, N_SPLITS = 10, MAX_COMBOS = 250, VERBOSE = True)

# Exp Smoothing Saving
#TS_train('Exp_Smoothing', 'Daily', USE_DIFF = False, HYPERPARAM_TUNING = False, SAVE_SCORES = True, N_SPLITS = 10, MAX_COMBOS = 50, VERBOSE = False)
#TS_train('Exp_Smoothing', 'Weekly', USE_DIFF = False, HYPERPARAM_TUNING = False, SAVE_SCORES = True, N_SPLITS = 10, MAX_COMBOS = 50, VERBOSE = False)
#TS_train('Exp_Smoothing', 'Monthly', USE_DIFF = False, HYPERPARAM_TUNING = False, SAVE_SCORES = True, N_SPLITS = 10, MAX_COMBOS = 50, VERBOSE = False)


# %%
