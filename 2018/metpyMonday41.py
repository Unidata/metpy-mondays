
# Metpy Monday
# 41 - Multiprocessing
# https://www.youtube.com/watch?v=5TINkCci_W4


import multiprocessing as mp

from datetime import datetime

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
from matplotlib import patheffects
from metpy.plots.ctables import registry
from siphon.catalog import TDSCatalog

def plot_dataset(dataset):
	print('Plotting dataset: ', dataset)
	
	# Get dataset
	ds = dataset.remote_access(service = 'OPENDAP')
	
	# Pull out what we need from the GOES netCDF file
	data_var = ds.variables['Rad']
	x = ds.variables['x'][:]
	y = ds.variables['y'][:]
	proj_var = ds.variables[data_var.grid_mapping]
	
	# Create a Globe specifying a spherical earth with the correct radius
	globe = ccrs.Globe(ellipse = 'sphere', semimajor_axis = proj_var.semi_major_axis, semiminor_axis = proj_var.semi_minor_axis)
	
	proj = ccrs.LambertConformal(central_longitude = proj_var.longitude_of_projection_origin, central_latitude = proj_var.latitude_of_projection_origin, globe = globe)
	
	
	# Make the plot
	fig = plt.figure(figsize = (1.375 * 40, 40))
	ax = fig.add_subplot(1, 1, 1, projection = proj)
	plt.subplots_adjust(left = 0, bottom = 0, right = 1, top = 1, wspace = 0, hspace = 0)
	
	wv_norm, wv_cmap = registry.get_with_range('WVCIMSS_r', 195, 265)
	im = ax.imshow(data_var[:], extent = (x.min(), x.max(), y.min(), y.max()), origin = 'upper', transform = proj)
	im.set_cmap(wv_cmap)
	im.set_norm(wv_norm)
	
	ax.add_feature(cfeature.BORDERS, linewidth = 8, edgecolor = 'black')
	ax.add_feature(cfeature.STATES.with_scale('50m'), linestyle = '-', edgecolor = 'black', linewidth = 4)
	
	timestamp = datetime.strptime(ds.time_coverage_start, '%Y-%m-%dT%H:%M:%S.%fZ')
	
	
	# Add text and save the returned object so we can manipulate it
	text_time = ax.text(0.01, 0.01, timestamp.strftime('%d %B %Y %H:%M'), horizontalalignment = 'left', transform = ax.transAxes, color = 'white', fontsize = 100, weight = 'bold')
	
	outline_effect = [patheffects.withStroke(linewidth = 15, foreground = 'black')]
	text_time.set_path_effects(outline_effect)
	
	ax.set_extent([-124.5, -105, 38.5, 50])
	ax.gridlines(linestyle = ':', color = 'black', linewidth = 2)
	
	filename = 'image_{}.png'.format(dataset)
	plt.savefig(filename)
	return filename

	
# Use Agg backend
plt.switch_backend('Agg')

# Get a catalog of GOES 16 data
date = datetime.utcnow()
channel = 8
region = 'CONUS'
cat = TDSCatalog('http://thredds-test.unidata.ucar.edu/thredds/catalog/satellite/goes/east/grb/ABI/{}/Channel{:02d}/{:%Y%m%d}/catalog.xml'.format(region, channel, date))

with mp.Pool(processes = 4) as pool:
	pool.map(plot_dataset, cat.datasets[-10:])
	pool.close()
	pool.join()

