# Metpy Monday
# 162 - Creating REST APIs Part 3
# https://www.youtube.com/watch?v=NqHErtJhmbM

from datetime import datetime
import json
import flask
from flask import request, Response
from siphon.simplewebservice.ndbc import NDBC
import io

app = flask.Flask(__name__)
app.config['DEBUG'] = True

def get_data_for_buoy(buoy):
	"""
	Gets current data for a given buoy.
	"""
	df = NDBC.latest_observations()
	df['time'] = [datetime.strftime(t, '%Y-%m-%dT%H:%M') for t in df['time']]
	return df[df['station'] == buoy]

def get_variable_for_all_buoys(varname):
	"""
	Gets variable for all buoys.
	"""
	df = NDBC.latest_observations()
	df['time'] = [datetime.strftime(t, '%Y-%m-%dT%H:%M') for t in df['time']]
	return df[['time', 'station', varname]]


def get_data_for_all_buoys():
	"""
	Gets data for all buoys.
	"""
	df = NDBC.latest_observations()
	df['time'] = [datetime.strftime(t, '%Y-%m-%dT%H:%M') for t in df['time']]
	return df

	
@app.route('/', methods = ['GET'])
def home():
	return '<h1>Buoy API</h1>'

@app.route('/singlebuoy', methods = ['GET'])
def single_buoy():
	req = dict(request.values)
	buoy_data = get_data_for_buoy(req.get('buoynumber'))
	if buoy_data is not None:
#	return f""" <h1>Flask API for <a target="_blank" href="https://www.ndbc.noaa.gov/">NDBC</a> </h1>
#	<p>Air temperature at <b>41139</b> is {buoy_data.to_dict('records')[0]['air_temperature']}.</p>"""
		return json.dumps(buoy_data.to_dict('records')[0])
	else:
		return 'No valid request'
		

@app.route('/singlevariable', methods = ['GET'])
def single_variable():
	req = dict(request.values)
	buoy_data = get_variable_for_all_buoys(req.get('varname'))
	if buoy_data is not None:
#	return f""" <h1>Flask API for <a target="_blank" href="https://www.ndbc.noaa.gov/">NDBC</a> </h1>
#	<p>Air temperature at <b>41139</b> is {buoy_data.to_dict('records')[0]['air_temperature']}.</p>"""
		return json.dumps(buoy_data.to_dict('records'))
	else:
		return 'No valid request'

@app.route('/currentcsv', methods=['GET'])
def all_data():
	buoy_data = get_data_for_all_buoys()
	s = io.StringIO()
	buoy_data.to_csv(s, index=False)
	return Response(s.getvalue(), headers={'Content-Disposition': 'attachment;filename=buoydata.txt'})


app.run()

# run in terminal: python metpyMonday162-myapi.py
