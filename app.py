from flask import Flask, render_template, abort
import csv

app = Flask(__name__)

def get_data():
  csv_path = 'static/data/crime-master.csv'

  with open(csv_path, 'r') as infile:
    datarows = list(csv.DictReader(infile))
  return datarows

@app.route("/")
def homepage():
  template='index.html'
  return render_template(template)

@app.route("/<city>/")
def city_data(city):
  template = 'city-page.html'
  temp = get_data()
  data=[]

  for row in temp:
    if row['city'] == city:
      data.append(row)
  return render_template(template, data=data, city=city, total=temp)

if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)
