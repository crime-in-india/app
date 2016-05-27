# This script combines the two categories: insult to the modesty of women and assault on women with intent to outrage her modesty into one category:
# 'Sexual harassment and molestation of women'

import csv
from os.path import join, basename

DATADIR = '../static/data'

files = ['2010.csv','2011.csv','2012.csv','2013.csv','2014.csv']
master = []
categ = 'Sexual harassment and molestation of women'

for f in files:
	the_file = join(DATADIR, f)
	write_file = f
	with open(the_file,'r') as infile:
		datarows = list(csv.reader(infile))
		datarows = datarows[1:]
		
		for i in range(0, len(datarows)-1,2):
			master.append(datarows[i])
			master.append(datarows[i+1])
			city = datarows[i][0]
			year = datarows[i][1]
			assault = datarows[i]
			insult = datarows[i+1]
			incidences = int(assault[3]) + int(insult[3])
			rate = 0.0
			new_row = [city,year,categ,incidences,rate]
			master.append(new_row)

with open('temp.csv', 'w') as outfile:
	writer = csv.writer(outfile)
	writer.writerows(master)