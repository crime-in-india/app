# This script combines all the city files (the ones with average rates) into one big master file.
# This script has to be run from the scripts folder and the file is saved in the data folder

import csv
from os.path import join, basename
from glob import glob

DATADIR = '../static/data'
files = glob(join(DATADIR,'city-avg', '*.csv'))
headers = ['city', 'crime_name','2010','2011','2012','2013','2014','avg']
master = []

for f in files:
  with open(join(DATADIR,'total.csv'), 'w') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(headers)

    with open(f, 'r') as infile:
      print("currently reading", f)
      datarows = csv.reader(infile)
      city = basename(f)[:-4]
      next(datarows)

      for row in datarows:
        row.insert(0, city)
        master.append(row)
    writer.writerows(master)