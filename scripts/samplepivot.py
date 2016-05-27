# This script writes a city-wise csv of crime data with years
# as column headers.

# TO FIX: It doesn't write the headers properly. Headers have 
# been manually entered.

import pandas as pd
import csv
from os.path import join
DATADIR = '../static/data'

with open(join(DATADIR, 'cities.csv')) as r:
    cities = [r['city'] for r in csv.DictReader(r)] # Get list of cities
cities.append("India")

dataf = pd.read_csv(join(DATADIR, 'data-v11.csv'))
dataf['rate'] = pd.to_numeric(dataf['rate'], errors='coerce')

headers = ['crime_name', '2010', '2011', '2012', '2013', '2014']

for city in cities:
    df = dataf[dataf.city==city]
    pv = pd.pivot_table(df, index=['crime_name'], columns=['year'], values=['rate'])
    fname = join(DATADIR,city + '.csv')
    print(fname)
    pv.to_csv(fname, header=True) #header writing doesn't work


# Write a file for India

# df = dataf[dataf.city=='India']
# pv = pd.pivot_table(df, index=['crime_name'], columns=['year'], values=['rate'])
# fname = join(DATADIR,'India.csv')
# print(fname)
pv.to_csv(fname, header=True) #header writing doesn't work