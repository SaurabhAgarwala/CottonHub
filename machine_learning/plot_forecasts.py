import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from get_forecasts import get_forecasts, get_all_forecasts
from utils.create_dir import create_dir

def plot_forecasts(cat, forecasts, refer_data, forecast_type = 'Daily'):
    cat_name = f'{cat[0]}_x_{cat[1]}'
    cat_data = refer_data[refer_data['Category'] == cat_name]
    if(cat_data.shape[0] == 0):
        return
    day_cols = [x for x in cat_data.columns if x.startswith('day_')]

    prev_vals = list(reversed(cat_data.iloc[-1][day_cols]))
    prices = prev_vals + [float(forecasts[x]['Forecast_Price']) for x in forecasts]
    lower = prev_vals + [float(forecasts[x]['Lower_Bound']) for x in forecasts]
    upper = prev_vals + [float(forecasts[x]['Upper_Bound']) for x in forecasts]

    _, ax = plt.subplots(1, 1)
    ax.plot(np.arange(len(prices)), prices, color = 'red')
    ax.fill_between(np.arange(len(prices)), upper, lower, color = 'blue', alpha = 0.5)
    ax.set_ylim(0, 10000)

    create_dir(f'./images/forecast_imgs/{forecast_type}/')
    plt.savefig(f'./images/forecast_imgs/{forecast_type}/{cat_name}_forecast.png', bbox_inches = 'tight')

def plot_all_forecasts(refer_data):
    all_forecasts = get_all_forecasts()
    cats = [['Adilabad', 'Cotton'], ['Amreli', 'Other'], ['Annigeri', 'GCH'], ['Anoopgarh', 'American'], ['Arvi', 'H'], ['Asifabad', 'Cotton'], ['Babra', 'Shanker'], ['Bagasara', 'Other'], ['Balwadi', 'H'], ['Bhattu Kalan', 'American'], ['Bhavnagar', 'Other'], ['Bhiloda', 'Other'], ['Bhokar', 'Other'], ['Bijapur', 'LH'], ['Bilara', 'Other'], ['Bodeli', 'Shanker'], ['Bodeli(Hadod)', 'Shanker'], ['Bodeli(Kalediya)', 'Shanker'], ['Bodeli(Modasar)', 'Shanker'], ['Botad(Haddad)', 'Shanker'], ['Choppadandi', 'Cotton'], ['Chotila', 'Shanker'], ['Davangere', 'MCU'], ['Dhandhuka', 'Shanker'], ['Dhoraji', 'H.B'], ['Dhrol', 'Other'], ['Ding', 'American'], ['Enkoor', 'Cotton'], ['Gajsinghpur', 'American'], ['Gharsana', 'American'], ['Goluwala', 'American'], ['Goluwala', 'Desi'], ['Gondal', 'H.B'], ['Halvad', 'Other'], ['Hanumangarh', 'Desi'], ['Haveri', 'GCH'], ['Hubli (Amaragol)', 'GCH'], ['Indravelly(Utnoor)', 'Cotton'], ['Jaitsar', 'American'], ['Jamnagar', 'Other'], ['Jangaon', 'Cotton'], ['Jetpur(Dist.Rajkot)', 'Cotton'], ['Jhabua', 'DCH'], ['Jobat', 'Other'], ['Kalmeshwar', 'Other'], ['Kapadvanj', 'Other'], ['Karimnagar', 'Cotton'], ['Karjan', 'Shanker'], ['Kekri', 'Other'], ['Khairthal', 'Other'], ['Khammam', 'Cotton'], ['Khetia', 'H'], ['Kille Dharur', 'Other'], ['Kolathur', 'Other'], ['Konganapuram', 'Other'], ['Kothagudem', 'Cotton'], ['Kuber', 'Cotton'], ['Limdi', 'Shanker'], ['Mahuva(Station Road)', 'Shanker'], ['Malout', 'Other'], ['Manavdar', 'Shanker'], ['Narkhed', 'Other'], ['Narsampet', 'Cotton'], ['Padampur_Rajasthan', 'American'], ['Pandhurna', 'Other'], ['Parbhani', 'Other'], ['Parkal', 'Cotton'], ['Patan', 'Other'], ['Pilli Banga', 'American'], ['Pilli Banga', 'Desi'], ['Pulgaon', 'Other'], ['Raichur', 'F'], ['Raisingh Nagar', 'American'], ['Rajura', 'Other'], ['Ranebennur', 'GCH'], ['Rawatsar', 'American'], ['Rawla', 'American'], ['Sadulshahar', 'American'], ['Sangriya', 'Other'], ['Saunsar', 'H'], ['Savanur', 'GCH'], ['Sendhwa', 'H'], ['Sirsa_Haryana', 'American'], ['Sri Karanpur', 'American'], ['Sri Vijayanagar', 'American'], ['Sri Vijayanagar', 'Desi'], ['Sriganganagar', 'American'], ['Suratgarh', 'American'], ['Thirumangalam', 'MCU'], ['Thirumangalam', 'Other'], ['Uchana', 'American'], ['Unava', 'Other'], ['Usilampatty', 'LRA'], ['Usilampatty', 'MCU'], ['Usilampatty', 'Other'], ['Vankaner', 'Other'], ['Vikkiravandi', 'Other'], ['Villupuram', 'Other'], ['Visavadar', 'Other'], ['Visnagar', 'Other'], ['Warangal', 'Cotton']]
    for cat_idx, cat in enumerate(cats):
        plot_forecasts(cat, all_forecasts[cat_idx]['Daily'], refer_data, 'Daily')
        plot_forecasts(cat, all_forecasts[cat_idx]['Weekly'], refer_data, 'Weekly')
        plot_forecasts(cat, all_forecasts[cat_idx]['Monthly'], refer_data, 'Monthly')

refer_data = pd.read_csv('./data/Training_Data/day_1.csv', usecols = ['Category'] + [f'day_{x}' for x in range(1, 16)])
plot_all_forecasts(refer_data)