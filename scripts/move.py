# This script inserts a new column for the cities that did not figure in
# the 2010 data set. This is because Pandas has not taken into account 
# that these cities had to have a blank row for the 2010 column

import csv
from os.path import join, basename
from glob import glob

DIR = '../static/data'

fnames = ['Aurangabad', 'Chandigarh', 'Durg-Bhilainagar', 'Ghaziabad', 'Gwalior', 'Jodhpur', 'Kannur', 'Kollam', 'Kota', 'Kozhikode', 'Malappuram', 'Raipur', 'Ranchi', 'Srinagar', 'Thiruvananthapuram', 'Thrissur', 'Tiruchirappalli','Vasai-Virar']

for city in fnames:
  f = join(DIR, 'cities', city + '.csv')
  with open(f, 'r') as infile:
    datarows = csv.reader(infile)
    headers = next(datarows)

    with open(city + '.csv', 'w') as fout:
      writer = csv.writer(fout)
      writer.writerow(headers)
      
      for row in datarows:
        temp = [row[0],'',row[1],row[2],row[3],row[4]]
        writer.writerow(temp)