"""
To deploy app:

1. Clear out any existing build/ subdirectory
2. Run: `$ python freeze.py` to build the build/ subdirectory
3. Copy the files in build/ into whatever directory contains the github.io pages repo:

    $ cp -r app/build/* crime-in-india.github.io/

4. Git add/commit/push to Github
5. Site should automatically update.
"""

import csv
from os.path import join
from operator import itemgetter
from flask_frozen import Freezer
from app import app

freezer = Freezer(app)

app.config['FREEZER_IGNORE_404_NOT_FOUND'] = True

@freezer.register_generator
def city_page():
    DATADIR = 'static/data'
    fpath = join(DATADIR, 'total-final-2.csv')

    with open(fpath, 'r') as csvin:
        data = list(csv.DictReader(csvin))
    for row in data:
        yield { 'city': row['city'] }


@freezer.register_generator
def crime_page():
  with open('static/data/total-final-2.csv', 'r') as csvin:
    datarows = list(csv.DictReader(csvin))
  for row in datarows:
    yield { 'crime': row['crime_name'] }

if __name__ == '__main__':
    freezer.freeze()