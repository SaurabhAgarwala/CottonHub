import numpy as np
import pandas as pd
from datetime import datetime
import time

from forecast.Regr_forecast.Regr_forecast_cat_prices import Regr_forecast_cat_prices
from forecast.Regr_forecast.Regr_merge_forecasts import Regr_merge_forecasts
from forecast.TS_forecast.TS_forecast_cat_prices import TS_forecast_cat_prices
from forecast.TS_forecast.TS_merge_forecasts import TS_merge_forecasts

def get_forecasts(market, variety):
    cat = market + '_x_' + variety
    forecasts = {'Daily': {}, 'Weekly': {}, 'Monthly': {}}
    Regr_forecast_cat_prices(cat)
    TS_forecast_cat_prices(cat)
    daily_forecasts = Regr_merge_forecasts(cat)
    forecasts['Daily'] = daily_forecasts
    weekly_monthly_forecasts = TS_merge_forecasts(cat)
    forecasts['Weekly'] = weekly_monthly_forecasts['Weekly']
    forecasts['Monthly'] = weekly_monthly_forecasts['Monthly']
    return forecasts

def get_all_forecasts():
    cats = [['Adilabad', 'Cotton'], ['Amreli', 'Other'], ['Annigeri', 'GCH'], ['Anoopgarh', 'American'], ['Arvi', 'H'], ['Asifabad', 'Cotton'], ['Babra', 'Shanker'], ['Bagasara', 'Other'], ['Balwadi', 'H'], ['Bhattu Kalan', 'American'], ['Bhavnagar', 'Other'], ['Bhiloda', 'Other'], ['Bhokar', 'Other'], ['Bijapur', 'LH'], ['Bilara', 'Other'], ['Bodeli', 'Shanker'], ['Bodeli(Hadod)', 'Shanker'], ['Bodeli(Kalediya)', 'Shanker'], ['Bodeli(Modasar)', 'Shanker'], ['Botad(Haddad)', 'Shanker'], ['Choppadandi', 'Cotton'], ['Chotila', 'Shanker'], ['Davangere', 'MCU'], ['Dhandhuka', 'Shanker'], ['Dhoraji', 'H.B'], ['Dhrol', 'Other'], ['Ding', 'American'], ['Enkoor', 'Cotton'], ['Gajsinghpur', 'American'], ['Gharsana', 'American'], ['Goluwala', 'American'], ['Goluwala', 'Desi'], ['Gondal', 'H.B'], ['Halvad', 'Other'], ['Hanumangarh', 'Desi'], ['Haveri', 'GCH'], ['Hubli (Amaragol)', 'GCH'], ['Indravelly(Utnoor)', 'Cotton'], ['Jaitsar', 'American'], ['Jamnagar', 'Other'], ['Jangaon', 'Cotton'], ['Jetpur(Dist.Rajkot)', 'Cotton'], ['Jhabua', 'DCH'], ['Jobat', 'Other'], ['Kalmeshwar', 'Other'], ['Kapadvanj', 'Other'], ['Karimnagar', 'Cotton'], ['Karjan', 'Shanker'], ['Kekri', 'Other'], ['Khairthal', 'Other'], ['Khammam', 'Cotton'], ['Khetia', 'H'], ['Kille Dharur', 'Other'], ['Kolathur', 'Other'], ['Konganapuram', 'Other'], ['Kothagudem', 'Cotton'], ['Kuber', 'Cotton'], ['Limdi', 'Shanker'], ['Mahuva(Station Road)', 'Shanker'], ['Malout', 'Other'], ['Manavdar', 'Shanker'], ['Narkhed', 'Other'], ['Narsampet', 'Cotton'], ['Padampur_Rajasthan', 'American'], ['Pandhurna', 'Other'], ['Parbhani', 'Other'], ['Parkal', 'Cotton'], ['Patan', 'Other'], ['Pilli Banga', 'American'], ['Pilli Banga', 'Desi'], ['Pulgaon', 'Other'], ['Raichur', 'F'], ['Raisingh Nagar', 'American'], ['Rajura', 'Other'], ['Ranebennur', 'GCH'], ['Rawatsar', 'American'], ['Rawla', 'American'], ['Sadulshahar', 'American'], ['Sangriya', 'Other'], ['Saunsar', 'H'], ['Savanur', 'GCH'], ['Sendhwa', 'H'], ['Sirsa_Haryana', 'American'], ['Sri Karanpur', 'American'], ['Sri Vijayanagar', 'American'], ['Sri Vijayanagar', 'Desi'], ['Sriganganagar', 'American'], ['Suratgarh', 'American'], ['Thirumangalam', 'MCU'], ['Thirumangalam', 'Other'], ['Uchana', 'American'], ['Unava', 'Other'], ['Usilampatty', 'LRA'], ['Usilampatty', 'MCU'], ['Usilampatty', 'Other'], ['Vankaner', 'Other'], ['Vikkiravandi', 'Other'], ['Villupuram', 'Other'], ['Visavadar', 'Other'], ['Visnagar', 'Other'], ['Warangal', 'Cotton']]
    cat_forecasts = []
    for market, variety in cats:
        cat_forecasts.append(get_forecasts(market, variety))
    return cat_forecasts