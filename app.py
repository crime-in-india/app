from flask import Flask, render_template, abort
import csv
from os.path import join

app = Flask(__name__)

# Get all data, entire data dump
def get_data():
  csv_path = 'static/data/data-v7.csv'
  with open(csv_path, 'r') as infile:
    datarows = list(csv.DictReader(infile))
  return datarows

# Route to home page
@app.route("/")
def homepage():
  template='index.html'
  return render_template(template)




# Route to each city's individual page
@app.route("/cities/<city>/")
def city_page(city):
  DATADIR = 'static/data/city-avg'
  citypath = join(DATADIR, city + '.csv')
  indiapath = join(DATADIR, 'India.csv')

  # Get categories of crimes
  with open('static/data/crime-categories.csv', 'r') as csvin:
    categs = list(csv.DictReader(csvin))

  violent_categs = [c['crime'] for c in categs if c['category'] == 'Violent Crime']
  women_categs = [d['crime'] for d in categs if d['category'] == 'Crime Against Women']
  prop_categs = [p['crime'] for p in categs if p['category'] == 'Property Crime']

  template = 'city-page.html'
  
  with open(citypath, 'r') as csvin:
    data = list(csv.DictReader(csvin))

  with open(indiapath, 'r') as i:
    india = list(csv.DictReader(i))

  return render_template(template, data=data, city=city, v=violent_categs,w=women_categs,p=prop_categs, india=india)



# Route to crime page
@app.route("/crime/<crime>/")
def crime_page(crime):
  template = 'crime-page.html'
  temp = get_data()
  data = []

  data = [row for row in temp if row['crime_name'] == crime]
  return render_template(template, crime_data=data, total=temp, crime=crime)


# Route to crime landing page
@app.route("/crime-landing")
def crime_landing():
  template = 'crime-landing.html'
  return render_template(template)


# Route to the city landing page
@app.route("/cities")
def city_landing():
  template = 'city-landing.html'
  with open('static/data/cities-overall.csv', 'r') as csvin:
    datarows = list(csv.DictReader(csvin))

  # Don't show India in the table
  only_cities = datarows[:-1]  

  india = datarows[-1]
  citylist = [c for c in datarows if c['avg'] > india['avg']]
  citylist.append(india)
  return render_template(template,cities=only_cities,chartdata=citylist)



# Route for violent crimes page
@app.route("/violent-crimes")
def violent_landing_page():
  template = 'violent-page.html'
  with open('static/data/crime-categories.csv', 'r') as csvin:
    categs = list(csv.DictReader(csvin))

  categs = [c['crime'] for c in categs if c['category'] == 'Violent Crime']
  data = get_data()
  violent_data = [d for d in data if d['crime_name'] in categs]
  return render_template(template,violent=violent_data)


# Route for crimes against women page
@app.route("/women-crimes")
def women_landing_page():
  template = 'women-page.html'
  with open('static/data/crime-categories.csv', 'r') as csvin:
    categs = list(csv.DictReader(csvin))

  categs = [c['crime'] for c in categs if c['category'] == 'Crime Against Women']
  data = get_data()
  women_data = [d for d in data if d['crime_name'] in categs]
  return render_template(template,w_data=women_data)



# Route to the data dump page
@app.route("/data")
def data_table():
  template = 'data.html'
  data = get_data()
  return render_template(template, master=data)

if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)