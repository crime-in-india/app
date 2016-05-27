# ThIs script takes care of the floating point errors in total.csv and rounds them off to the nearest single digit

import csv
from os.path import join

DATADIR = '../static/data'

# with open(join(DATADIR,'data-v7.csv')) as infile:
# 	datarows = csv.reader(infile)
# 	headers = next(datarows)

# 	with open(join(DATADIR, 'data-v8.csv'),'w') as outfile:
# 		writer = csv.writer(outfile)
# 		writer.writerow(headers)
		
# 		for row in datarows:
# 			print(row)
# 			row[-1] = round(float(row[-1]), 1)
# 			writer.writerow(row)

with open(join(DATADIR, 'total.csv')) as infile:
	datarows = csv.reader(infile)
	headers = next(datarows)

	with open(join(DATADIR, 'total-final-2.csv'),'w') as outfile:
		writer = csv.writer(outfile)
		writer.writerow(headers)
		
		for row in datarows:
			print(row)
			if row[-2] == '':
				row[-2] = '0.0'
			row[-2] = round(float(row[-2]), 1)
			writer.writerow(row)