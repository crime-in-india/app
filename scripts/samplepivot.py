import pandas as pd
import csv
from os.path import join
DATADIR = 'static/data'

with open(join(DATADIR, 'cities.csv')) as r:
    cities = [r['city'] for r in csv.DictReader(r)]

dataf = pd.read_csv(join(DATADIR, 'data.csv'))
dataf['rate'] = pd.to_numeric(dataf['rate'], errors='coerce')


for city in cities:
    df = dataf[dataf.city==city]
    pv = pd.pivot_table(df, index=['crime_name'], columns=['year'], values=['rate'])
    fname = join(DATADIR, 'cities', city + '.csv')
    print(fname)
    pv.to_csv(fname, header=False)



