from flask import Flask, render_template, abort, request
import csv
from os.path import join
from operator import itemgetter

app = Flask(__name__)

# Get all data, entire data dump
def get_data():
  csv_path = 'static/data/data-v11.csv'
  with open(csv_path, 'r') as infile:
    datarows = list(csv.DictReader(infile))
  return datarows

#################################################################

# Route to home page
@app.route("/")
def homepage():
  template='index.html'
  with open('static/data/total-final-2.csv', 'r') as csvin:
    datarows = list(csv.DictReader(csvin))

    total = [d for d in datarows if d['crime_name'] == 'Total cognizable crimes under IPC' and d['city'] != 'India']
    total = sorted(total, key=lambda r:float(r['avg']), reverse=True)[:5]

    assault = [d for d in datarows if d['crime_name'] == 'Hurt' and d['city'] != 'India']
    assault = sorted(assault, key=lambda r:float(r['avg']), reverse=True)[:5]

    robbery = [d for d in datarows if d['crime_name'] == 'Robbery' and d['city'] != 'India']
    robbery = sorted(robbery, key=lambda r:float(r['avg']), reverse=True)[:5]

    murder = [d for d in datarows if d['crime_name'] == 'Murder' and d['city'] != 'India']
    murder = sorted(murder, key=lambda r:float(r['avg']), reverse=True)[:5]

    kidnapping = [d for d in datarows if d['crime_name'] == 'Kidnapping' and d['city'] != 'India']
    kidnapping = sorted(kidnapping, key=lambda r:float(r['avg']), reverse=True)[:5]

    cheating = [d for d in datarows if d['crime_name'] == 'Cheating' and d['city'] != 'India']
    cheating = sorted(cheating, key=lambda r:float(r['avg']), reverse=True)[:5]

    harass = [d for d in datarows if d['crime_name'] == 'Sexual harassment and molestation of women' and d['city'] != 'India']
    harass = sorted(harass, key=lambda r:float(r['avg']), reverse=True)[:5]

    rape = [d for d in datarows if d['crime_name'] == 'Rape' and d['city'] != 'India']
    rape = sorted(rape, key=lambda r:float(r['avg']), reverse=True)[:5]

    rash = [d for d in datarows if d['crime_name'] == 'Deaths due to rash/negligent driving' and d['city'] != 'India']
    rash = sorted(rash, key=lambda r:float(r['avg']), reverse=True)[:5]


    categs = ['Overall crimes', 'Murder', 'Rape', 'Sexual harassment', 'Hurt', 'Robbery', 'Kidnapping', 'Cheating', 'Deaths due to rash driving']

    list_data = [total, murder,rape,harass,assault,robbery,kidnapping,cheating,rash]

  return render_template(template, categs=categs,list_data=list_data)



#################################################################



# Route to each city's individual page
@app.route("/cities/<city>/")
def city_page(city):
  DATADIR = 'static/data/city-avg'
  citypath = join(DATADIR, city + '.csv')
  indiapath = join(DATADIR, 'India.csv')

  # Get categories of crimes
  with open('static/data/crime-categories.csv', 'r') as csvin:
    categs = list(csv.DictReader(csvin))

  cat_list = {}

  for el in categs:
    if not cat_list.get(el['crime']):
      cat_list[el['crime']] = el['category']

  violent_categs = [c['crime'] for c in categs if c['category'] == 'Violent Crime']
  women_categs = [d['crime'] for d in categs if d['category'] == 'Crime Against Women']
  prop_categs = [p['crime'] for p in categs if p['category'] == 'Property Crime']
  econ_categs = [p['crime'] for p in categs if p['category'] == 'Economic Crime']
  total_categs = violent_categs + women_categs + prop_categs + econ_categs

  template = 'city-page.html'

  # Get data of selected city
  with open(citypath, 'r') as csvin:
    data = list(csv.DictReader(csvin))

  for r in data:
    if r['crime_name'] in total_categs:
      r['categ'] = cat_list[r['crime_name']]

  table_data = [row for row in data if row['crime_name'] in total_categs]
  table_data = sorted(table_data, key=lambda r:r['categ'])

  # Get national average data
  with open(indiapath, 'r') as i:
    india = list(csv.DictReader(i))

  return render_template(template, data=data, city=city, v=violent_categs,w=women_categs,p=prop_categs,e=econ_categs, india=india,table_data=table_data)


#################################################################

# Route to crime page
@app.route("/crime/<crime>/")
def crime_page(crime):
  template = 'crime-page.html'
  with open('static/data/total-final-2.csv', 'r') as csvin:
    datarows = list(csv.DictReader(csvin))
  temp = get_data()
  data = []

  data = [row for row in datarows if row['crime_name'] == crime]
  return render_template(template, crime_data=data, total=temp, crime=crime)


#################################################################


# Route to the city landing page
@app.route("/city-list/")
def city_landing():
  template = 'city-landing.html'
  with open('static/data/total-final-2.csv', 'r') as csvin:
    datarows = list(csv.DictReader(csvin))

  datarows = [r for r in datarows if r['crime_name'] == 'Total cognizable crimes under IPC']

  # Don't show India in the table
  only_cities = [d for d in datarows if d['city'] != 'India']

  # india = [d for d in datarows if d['crime_name'] == 'Total cognizable crimes under IPC' and d['city'] is 'India']
  # citylist = [c for c in datarows if c['avg'] > india[0]['avg']]
  # citylist.append(india)
  return render_template(template,cities=only_cities,n=datarows)



#################################################################



# Route for violent crimes page
@app.route("/violent-crimes/")
def violent_landing_page():
  DATADIR = './static/data'
  fname = join(DATADIR, 'total-final-2.csv')

  # Get national data
  with open(fname, 'r') as i:
    national = list(csv.DictReader(i))

  template = 'violent-page.html'
  with open('static/data/crime-categories.csv', 'r') as csvin:
    categs = list(csv.DictReader(csvin))

  categs = [c['crime'] for c in categs if c['category'] == 'Violent Crime']
  violent_data = [d for d in national if d['crime_name'] in categs]

  return render_template(template,violent=violent_data,n=national)



#################################################################


# ROUTE FOR CRIMES AGAINST WOMEN PAGE
@app.route("/women-crimes/")
def women_landing_page():
  DATADIR = './static/data'
  fname = join(DATADIR, 'total-final-2.csv')

  template = 'women-page.html'

  # Get national data
  with open(fname, 'r') as i:
    national = list(csv.DictReader(i))

  with open('static/data/crime-categories.csv', 'r') as csvin:
    categs = list(csv.DictReader(csvin))

  categs = [c['crime'] for c in categs if c['category'] == 'Crime Against Women']
  women_data = [d for d in national if d['crime_name'] in categs]
  women_data = sorted(women_data,key=lambda r:r['crime_name'])
  return render_template(template,w_data=women_data, n=national)



#################################################################


# ROUTE FOR PROPERTY CRIMES PAGE
@app.route("/property-crimes/")
def prop_landing_page():
  DATADIR = './static/data'
  fname = join(DATADIR, 'total-final-2.csv')

  template = 'property-page.html'

  # Get national data
  with open(fname, 'r') as i:
    national = list(csv.DictReader(i))

  with open('static/data/crime-categories.csv', 'r') as csvin:
    categs = list(csv.DictReader(csvin))

  categs = [c['crime'] for c in categs if c['category'] == 'Property Crime']
  prop_data = [d for d in national if d['crime_name'] in categs]

  return render_template(template,prop=prop_data, n=national)

#################################################################


# ROUTE FOR ECONOMIC CRIMES PAGE
@app.route("/economic-crimes/")
def econ_landing_page():
  DATADIR = './static/data'
  fname = join(DATADIR, 'total-final-2.csv')

  template = 'econ-page.html'

  # Get national data
  with open(fname, 'r') as i:
    national = list(csv.DictReader(i))

  with open('static/data/crime-categories.csv', 'r') as csvin:
    categs = list(csv.DictReader(csvin))

  categs = [c['crime'] for c in categs if c['category'] == 'Economic Crime']
  econ_data = [d for d in national if d['crime_name'] in categs]

  return render_template(template,econ=econ_data, n=national)


#################################################################
# ROUTE FOR ABOUT PAGE

@app.route("/about/")
def about():
  template = 'about.html'
  return render_template(template)


#################################################################

# Route to the data dump page
@app.route("/data/")
def data_table():
  DATADIR = './static/data'
  indiapath = join(DATADIR, 'total-final-2.csv')
  template = 'data.html'

  with open(indiapath, 'r') as i:
    data = list(csv.DictReader(i))

  total = [d for d in data if d['crime_name'] == 'Total cognizable crimes under IPC']

  data = [d for d in data if d['crime_name'] != 'Total cognizable crimes under IPC']

  return render_template(template, master=data, total=total)


#################################################################

# Route to the story page
@app.route("/stories/")
def story_page():
  DATADIR = './static/data'
  fpath = join(DATADIR, 'total-final-2.csv')

  with open(fpath, 'r') as i:
    data = list(csv.DictReader(i))

  template = 'stories.html'

  return render_template(template,data=data)

#################################################################

# Route to the references page
@app.route("/references/")
def ref_page():
  template = 'reference.html'
  return render_template(template)

if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)
