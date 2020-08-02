import numpy as np
import pandas as pd
from datetime import datetime

def date_features(data):
    data = data.assign(date_D = data['Date'].apply(lambda x: x.date().day))
    data = data.assign(date_M = data['Date'].apply(lambda x: x.date().month))
    data = data.assign(date_Y = data['Date'].apply(lambda x: x.date().year))

    data = data.assign(date_DOW = data['Date'].apply(lambda x: x.date().weekday()))
    data = data.assign(date_weekend = data['date_DOW'].apply(lambda x: 1 if ((x == 5) or (x == 6)) else 0))
    data = data.assign(date_weekday = data['date_DOW'].apply(lambda x: 1 if x in [0, 1, 2, 3, 4] else 0))

    for n in range(2, 7):
        for month_start in range(1, 13):
            month_stop = month_start + n
            season = [x % 12 + 1 for x in range(month_start, month_stop)]
            data[f'date_season_{month_start}_{(month_stop - 1) % 12}'] = data['date_M'].apply(lambda x: 1 if x in season else 0)

    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    for month_idx in range(1, 13):
        data[f'date_month_{months[month_idx - 1]}'] = data['date_M'].apply(lambda x: 1 if x == month_idx else 0)

    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    for day_idx in range(7):
        data[f'date_DOW_{days[day_idx]}'] = data['date_DOW'].apply(lambda x: 1 if x == day_idx else 0)

    data = data.drop(['date_D', 'date_DOW', 'date_M'], axis = 1)
    return data