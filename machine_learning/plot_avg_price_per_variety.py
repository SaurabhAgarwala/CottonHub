import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from get_forecasts import get_all_forecasts

all_forecasts = get_all_forecasts()
diff_vars = np.unique([x[1] for x in all_forecasts])

avg_prices = []
for var in diff_vars:
    var_cats = [x for x in all_forecasts if x[1] == var]
    today = [*all_forecasts[var_cats[0]]['Daily']['Forecasts'].keys()][0]
    avg_prices.append(np.mean([float(all_forecasts[x]['Daily']['Forecasts'][today]['Forecast_Price']) for x in var_cats]))

fig, ax = plt.subplots(1, 1)
ax.bar(np.arange(len(avg_prices)), avg_prices)
ax.set_xticks(np.arange(len(avg_prices)))
ax.set_xticklabels(diff_vars, rotation = 90)
plt.savefig('./images/avg_price_per_variety.png', bbox_inches = 'tight')