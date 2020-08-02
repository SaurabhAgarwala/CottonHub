# https://data.gov.in/catalog/variety-wise-daily-market-prices-data-cotton?filters%5Bfield_catalog_reference%5D=92788&format=json&offset=0&limit=6&sort%5Bcreated%5D=desc

import numpy as np
import pandas as pd
import xml.etree.ElementTree as ET
import os
import time

headers = ['State', 'District', 'Market', 'Commodity', 'Variety', 'Date', 'Min_Price', 'Max_Price', 'Modal_Price']

def load_xml(filename):
    xml_data = ET.parse(f'./data/Cotton_Prices_Data/Cotton_{filename}.xml')
    root = xml_data.getroot()
    data_node = root[0][0][0][1]
    data_node = data_node[0]
    raw_headers = ['State', 'District', 'Market', 'Commodity', 'Variety', 'Arrival_Date', 'Min_x0020_Price', 'Max_x0020_Price', 'Modal_x0020_Price']

    data_matrix = []
    for i in range(len(data_node)):
        data_row = [None] * len(headers)
        for j in range(len(headers)):
            try:
                tag = data_node[i][j].tag
                text = data_node[i][j].text
            except:
                pass
            data_row[raw_headers.index(tag)] = text
        data_matrix.append(data_row)
    data_df = pd.DataFrame(data_matrix, columns = headers)
    for col in ['Min_Price', 'Max_Price', 'Modal_Price']:
        data_df[col] = pd.to_numeric(data_df[col])
    return data_df

def load_csv(filename):
    data_df = pd.read_csv(f'./data/Cotton_Prices_Data/Cotton_{filename}.csv')
    data_df.columns = headers
    for col in ['Min_Price', 'Max_Price', 'Modal_Price']:
        data_df[col] = pd.to_numeric(data_df[col])
    return data_df

def load_all():
    df = pd.concat(
        [
            load_xml('2001-2002'), load_xml('2003'), load_xml('2004'), load_xml('2005'), load_xml('2006'), load_xml('2007'),
            load_xml('2008'), load_xml('2009'), load_xml('2010'), load_xml('2011'), load_xml('2012'), load_xml('2013'),
            load_xml('2014'), load_xml('2015'), load_xml('2016'), load_xml('2017'), load_xml('2018'),
            load_csv('2019'), load_csv('2020')
        ], axis = 0
    )
    
    df.to_csv("./data/Prices.csv", index = False)

load_all()