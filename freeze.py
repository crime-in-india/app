"""
To deploy app:

1. Clear out any existing build/ subdirectory
2. Run: `$ python freeze.py` to build the build/ subdirectory
3. Copy the files in build/ into whatever directory contains the github.io pages repo:

    $ cp -r app/build/* crime-in-india.github.io/

4. Git add/commit/push to Github
5. Site should automatically update.
"""

from flask_frozen import Freezer
from app import app
freezer = Freezer(app)

app.config['FREEZER_IGNORE_404_NOT_FOUND'] = True
# @freezer.register_generator
# def city_landing():


if __name__ == '__main__':
    freezer.freeze()

# @app.route("/city-list")
# def city_page(city):
#   DATADIR = 'static/data/city-avg'
#   citypath = join(DATADIR, city + '.csv')

#################################################################


# def crime_page(crime):
  # template = 'crime-page.html'
  # with open('static/data/total-final-2.csv', 'r') as csvin:
  #   datarows = list(csv.DictReader(csvin))
  # temp = get_data()
  # data = []

  # data = [row for row in datarows if row['crime_name'] == crime]
  # return render_template(template, crime_data=data, total=temp, crime=crime)




# def violent_landing_page():
#     pass

# def women_landing_page():
#     pass


# #################################################################

# def prop_landing_page():
#     pass



# def econ_landing_page():
#     pass

# def about():
#     pass

# @app.route("/data")
# def data_table():
#     pass

#################################################################

# # Route to the story page
# def story_page():
#     pass


# #################################################################

# def ref_page():
#     pass

