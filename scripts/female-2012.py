# This script replaces the rates for crimes against women
# using population of women. This is ONLY for the year 2012

import csv
from os.path import join

DATADIR = '../static/data'
pop_file = 'female-2011.csv'
data_file = 'data-v6.csv'
year = '2012'
f_crimes = ['Assault on women with intent to outrage her modesty','Cruelty by husband or his relatives', 'Custodial rape', 'Dowry deaths','Insult to the modesty of women', 'Kidnapping & abduction of women and girls', 'Molestation', 'Other rape', 'Rape', 'Sexual harassment']

# Read in female populations
with open(join(DATADIR, pop_file), 'r') as pop:
    cp = list(csv.DictReader(pop))

# Make a lookup dict of female pops in each city
city_pop = {}
for c in cp:
    if not city_pop.get(c['city']):
        city_pop[c['city']] = int(c['f_pop'])

# Read in the data file
with open(join(DATADIR, data_file), 'r') as data:
    datarows = list(csv.DictReader(data))
    # datarows = [d for d in datarows if d['year'] == year]

# Change rate of female crimes in 2010
for row in datarows:
    if row['year'] == year and row['crime_name'] in f_crimes:
        temp = float(100000 * int(row['incidences']) / int(city_pop[row['city']]))
        row['rate'] = round(temp, 1)

# Write a new csv
headers = ['city','year','crime_name','incidences','rate']

with open(join(DATADIR,'data-v7.csv'), 'w') as f:
    writer = csv.DictWriter(f, headers)
    writer.writeheader()
    writer.writerows(datarows)