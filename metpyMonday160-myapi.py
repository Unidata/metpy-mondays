import flask
from siphon.simplewebservice.ndbc import NDBC

app = flask.Flask(__name__)
app.config['DEBUG'] = True

def get_data_for_buoy(buoy):
	"""
	Gets current data for a given buoy.
	"""
	df = NDBC.latest_observations()
	return df[df['station'] == buoy]
	
@app.route('/', methods = ['GET'])
def home():
	buoy_data = get_data_for_buoy('41139')
#	return f""" <h1>Flask API for <a target="_blank" href="https://www.ndbc.noaa.gov/">NDBC</a> </h1>
#	<p>Air temperature at <b>41139</b> is {buoy_data.to_dict('records')[0]['air_temperature']}.</p>"""
	return str(buoy_data.to_dict('records')[0])
	
app.run()

# run in terminal: python metpyMonday160-myapi.py
