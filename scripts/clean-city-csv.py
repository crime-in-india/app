# This script cleans up the files produced by the Pandas
# script. It fixes for the weird headers the Pandas script
# was producing

import csv
from os.path import join, basename
from glob import glob

DATADIR = '../static/data/temp'
files = glob(join(DATADIR, '*.csv'))
headers = ['crime_name', '2010', '2011', '2012', '2013', '2014']

# for f in files:
#   with open(f, 'r') as csvin:
#     reader = csv.reader(csvin)
#     next(reader)
#     next(reader)
#     next(reader)

#     outname = basename(f)[0:-4] + '.csv'
#     with open(outname, 'w') as outfile:
#       print("Writing", outname)
#       writer = csv.writer(outfile)
#       writer.writerow(headers)
#       writer.writerows(reader)

with open(join(DATADIR,'India.csv'), 'r') as csvin:
    reader = csv.reader(csvin)
    next(reader)
    next(reader)
    next(reader)

    with open('India.csv', 'w') as outfile:
      print("Writing", 'India.csv')
      writer = csv.writer(outfile)
      writer.writerow(headers)
      writer.writerows(reader)