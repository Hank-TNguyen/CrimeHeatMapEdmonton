from flask import Flask, request, send_from_directory, render_template
import sqlite3
import json
import os

root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "client")
app = Flask(__name__, static_url_path='', static_folder='client')

@app.route('/data')
def data():
	conn = sqlite3.connect("../data.db")
	c = conn.cursor()
	query = "select coors.lat, coors.lon, sum(data.num_incidents)" \
" from 	crime_data data, coordinates coors " \
" where 	data.nbh = coors.nbh and data.year = 2018" \
" group by data.nbh"


	c.execute(query);
	return json.dumps(c.fetchall())

@app.route('/app/<path:path>')
def send_app(path):
	return send_from_directory('client', path)

@app.route('/')
def index():
	return send_from_directory('client', 'index.html')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')