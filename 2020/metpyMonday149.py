# Metpy Monday
# 149 - Making the GFS Text You with Twilio Part 3
# https://www.youtube.com/watch?v=MwgXUvKM2M4

# conda install -c conda-forge twilio

from datetime import datetime, timedelta
from twilio.rest import Client
from metpy.units import units
from siphon.catalog import TDSCatalog
import numpy as np
import time
from apscheduler.schedulers.backgorund import BackgroundScheduler

def send_forecast():

    # See twil.io/secure
    account_sid = ''
    auth_token = ''

    from_number = ''
    to_number = ''

    # Location information
    lat = -94.54
    lon = 36.18

    # Get the GFS Forecast
    best_gfs = TDSCatalog('http://thredds.ucar.edu/thredds/catalog/grib/NCEP/GFS/Global_0p5deg/catalog.xml?dataset=grib/NCEP/GFS/Global_0p5deg/Best')

    best_ds = best_gfs.datasets[0]
    ncss = best_ds.subset()
    query = ncss.query()
    now = datetime.utcnow()
    query.lonlat_point(lat, lon).vertical_level(100000).time_range(now, now + timedelta(days = 1))
    query.variables('Temperature_isobaric').accept('netcdf')
    data = ncss.get_data(query)

    temp = data.variables[Temperature_isobaric'][:].squeeze()

    idx_max = np.argmax(temp)
    idx_min = np.argmin(temp)

    # Get the min/max temperatures in degF
    max_temp = (temp[idx_max] * units.kelvin).to('degF')
    min_temp = (temp[idx_min] * units.kelvin).to('degF')

    client = Client(account_sid, auth_token)

    message_text = f'24 hr GFS Max T: {max_temp.m:.1f} degF Min T: {min_temp.m:.1f} degF'

    if min_temp <= 32:
        message_text += 'FREEZE HAZARD'
        
    message = client.messages.create(body = message_text, from = from_number, to = to_number)

    print(message.sid)
    
if __name__ == '__main__':
	scheduler = BackgroundScheduler()
	scheduler.add_job(send_forecast, trigger = 'cron', hour = '7')
	scheduler.start()
	
	try:
		while True:
			time.sleep(1)
	except (KeyboardInterrupt, SystemExit):
		scheduler.shutdown()
