# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 10:51:23 2020

@author: andyz
"""

import requests
import pandas as pd
from fredapi import Fred

def scrape_to_df(symbol, API_KEY):
    fred = Fred(api_key=API_KEY)
    df = fred.get_series_all_releases(symbol)
    df.dropna(inplace=True)
    df['realtime_start'] = pd.to_datetime(df['realtime_start'], format='%Y-%m-%d')
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')    
    df['value'] = df['value'].astype(float)
    
    return df