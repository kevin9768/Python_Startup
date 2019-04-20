# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 16:16:24 2019

@author: Kevin
"""

import pandas as pd

file = "DJ_day_market_cap.csv"
df = pd.read_csv(file)
web = pd.read_html("https://histock.tw/stock/rank.aspx?&m=0&p=1&d=0")
dt = pd.DataFrame.to_dict(web[0])