#!/usr/bin/python

import pyowm
import csv
import sys
import operator
import pandas as pd 
from apikey import owm_api_key
import time
import progressbar

# returns a list of towns in a country 'country' from data frame df as a dataframe
# country can be 'England', 'Scotland', 'Wales', or 'Northern Ireland'
def getTowns(df, country):
	towns = df.loc[df['Country'] == country]['Town'].to_frame()
	return towns

# returns a dataframe with towns in country 'country' and for each the current wind speed 
# in that town
def getWindSpeedsForTownsInCountry(df, country):

	towns = getTowns(df, country)

	bar = progressbar.ProgressBar()

	print ("Getting wind speeds for %s") % country
	for index, row in bar(towns.iterrows()):
	   	town = row['Town']
	   	try:
			wind_speed = owm.weather_at_place(town).get_weather().get_wind()['speed']
			towns['wind_speed'] = wind_speed
			# Supposed to be a max of 60 OWM API requests can be made per minute
			# not currently applied
			# time.sleep(1)
		except pyowm.exceptions.OWMError:
			pass
		except:
			pass
	return towns

def getAverageWindSpeedForTowns(towns):

	return towns['wind_speed'].mean()

def getAverageWindSpeedsForCountries(df):

	ni_towns = getWindSpeedsForTownsInCountry(df, 'Northern Ireland')
	welsh_towns = getWindSpeedsForTownsInCountry(df, 'Wales')
	scottish_towns = getWindSpeedsForTownsInCountry(df, 'Scotland')
	english_towns = getWindSpeedsForTownsInCountry(df, 'England')

	wind_speeds = {}

	wind_speeds['Northern Ireland'] = getAverageWindSpeedForTowns(ni_towns)
	wind_speeds['Wales'] = getAverageWindSpeedForTowns(welsh_towns)
	wind_speeds['Scotland'] = getAverageWindSpeedForTowns(scottish_towns)
	wind_speeds['England'] = getAverageWindSpeedForTowns(english_towns)

	return wind_speeds

###########################################################################################

if __name__ == '__main__':

	owm = pyowm.OWM(owm_api_key)  

	# get the name of the file containing a list of towns in the countries
	if (len(sys.argv) == 2):
		try:
			df = pd.read_csv(sys.argv[1])
		except:
			print('Unable to open %s') % sys.argv[1]
			exit(1)
	else:
		print ('Usage: wind-comparison <file name>')
		exit(1)

	wind_speeds = getAverageWindSpeedsForCountries(df)

	windiest_country = max(wind_speeds.iteritems(), key=operator.itemgetter(1))[0]

	print ("The windiest country in the UK at the moment is %s, with an average wind speed of %s m.p.h.") % \
	(windiest_country, wind_speeds[windiest_country])







