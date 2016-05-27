# This script simply uses the 2011 population list to populate the rate column for the newly added category 'Sexual harassment and molestation of women'

import csv
from os.path import join, basename

DATADIR = '../static/data'
pop_file = join(DATADIR,'female-2011.csv')
the_file = join(DATADIR,'data-v10.csv')

with open(pop_file,'r') as popin:
  pops = list(csv.DictReader(popin))

# Make a lookup dict of female pops in each city
city_pop = {}
for c in pops:
    if not city_pop.get(c['city']):
        city_pop[c['city']] = int(c['f_pop'])

with open(the_file,'r') as infile:
  datarows = list(csv.DictReader(infile))

  for row in datarows:
    if row['crime_name'] == 'Sexual harassment and molestation of women':
      temp = float(100000 * int(row['incidences']) / int(city_pop[row['city']]))
      row['rate'] = round(temp, 1)

# Write a new csv
headers = ['city','year','crime_name','incidences','rate']

with open(join(DATADIR,'data-v11.csv'), 'w') as f:
    w = csv.DictWriter(f, headers)
    w.writeheader()
    for r in datarows:
        # r['rate'] = round(float(r['rate']), 1)
        print('Writing', r)
        w.writerow(r)