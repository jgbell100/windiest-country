####################################################################################

# reads a csv file with town names, gets the latitude and longitude for each, and 
# appends them to the csv columns as new columns.
# 
# Prints the min/max for lat and lng across all the towns.
# 
# Where the lat/lng for a town can't be obtained, it is removed from the csv file.
# 
####################################################################################

import googlemaps
import sys
from apikey import google_api_key
import pandas as pd
import numpy as np
import os


def getLatLongFromAddress(address):

	geocode_result = gmaps.geocode(address)
	geometry = [d['geometry'] for d in geocode_result if 'geometry' in d]
	location = [d['location'] for d in geometry if 'location' in d]
	lat = [d['lat'] for d in location if 'lat' in d]
	lng = [d['lng'] for d in location if 'lng' in d]
	if (len(lat) == 0 or len(lng) == 0):
		raise ValueError('Could not get lat/lng for %s' % address) 
	return lat[0], lng[0]



gmaps = googlemaps.Client(key=google_api_key)

try:
	input_file = sys.argv[1]
	df = pd.read_csv(input_file)
except:
	print('Unable to open file')
	exit(1)

df['Lat'] = np.nan
df['Long'] = np.nan

# get the lat and lng for each town and add it to the dataframe
for index, row in df.iterrows():

	address = row['Town'] + ',' + row['Country']

	try:
		lat, lng = getLatLongFromAddress(address)
	except ValueError as err:
		# remove the row from the dataframe
		df.drop(df.index[index])
		print ('Dropping %s ') % address

	df.at[df.index[index], 'Lat'] = lat
	df.at[df.index[index], 'Long'] = lng

# print the min/max for lat and lng 
# this will be used to determine the proportions of the image for the heatmap
print("Min Latitude: %s ") % df['Lat'].min()
print("Max Latitude: %s ") % df['Lat'].max()
print("Min Longitude: %s ") % df['Long'].min()
print("Max Longitude: %s ") % df['Long'].max()

# save the data frame with the lat and lng to a csv file
filename, file_extension = os.path.splitext(input_file)
df.to_csv(filename + '_with_lat_and_long.csv')









