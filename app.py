from flask import Flask, render_template, request
from flask_googlemaps import GoogleMaps, Map
from flask_pymongo import MongoClient

app = Flask(__name__, template_folder="templates")
app.config['MONGO_DBNAME'] = 'maps'
app.config['GOOGLEMAPS_KEY'] = "AIzaSyB2tVZQaAh_EgYl3mvINIX2p77FHSXel-c"
client = MongoClient("mongodb+srv://user:user@preventechdb-swyud.mongodb.net/test?retryWrites=true&w=majority")
db = client.maps

GoogleMaps(
	app,
	key="AIzaSyB2tVZQaAh_EgYl3mvINIX2p77FHSXel-c"
)


@app.route('/')
def fullmap():
	# carica i segnaposti
	markers = list()
	for i in db.coord.find({}, {"_id": 0}):
		markers.append(i)
	# carica la mappa
	fullmap = Map(
		identifier="fullmap",
		varname="fullmap",
		style=(
			"height:100%;"
			"width:100%;"
			"position:relative;"
		),
		# coordinate iniziali
		lat=40.852015,
		lng=14.270947,
		markers=markers,
		language="it",
		center_on_user_location=True

		# maptype = "TERRAIN",
		# zoom="5"
	)
	return render_template(
		'index.html',
		fullmap=fullmap,
		GOOGLEMAPS_KEY=request.args.get('apikey')
	)


@app.route('/clickpost/', methods=['POST'])
def clickpost():
	# Now lat and lon can be accessed as:
	lat = request.form['lat']
	lng = request.form['lng']
	print(lat)
	print(lng)
	return "ok"


@app.route('/about')
def about():
	return render_template('about.html')


if __name__ == '__main__':
	app.run()
