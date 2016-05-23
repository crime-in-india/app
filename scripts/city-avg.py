# This script inserts a new column for average crime rate in each city file in the 2010 data set. 
# This script has to be run from the scripts folder

import csv
from os.path import join, basename
from glob import glob
from statistics import mean

def get_avg(row):
  # If there are no numbers in the column, don't take them into account
  # while calculating average
  # E.g. don't do (0+0+0+2.4+2.5)/5. Do (2.4+2.5) / 2
  row = [float(r) for r in row if r is not '']
  return round(mean(row),1)

DATADIR = '../static/data'

files = glob(join(DATADIR,'cities','*.csv'))

for f in files:
  with open(f, 'r') as infile:
    print("currently reading", f)
    datarows = csv.reader(infile)
    headers = next(datarows)
    headers.append('avg')
    name = join('temp',basename(f)[:-4] + '.csv')

    with open(name, 'w') as outfile:
      writer = csv.writer(outfile)
      writer.writerow(headers)

      for row in datarows:
        avg = get_avg(row[1:]) # Skip the crime name column
        row.append(avg)
        writer.writerow(row)