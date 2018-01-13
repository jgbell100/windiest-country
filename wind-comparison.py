###########################################################################################
#
#
#
###########################################################################################

import pyowm
import csv
import pandas as pd 
from apikey import owm_api_key

# returns a list of towns in a country 'country' from data frame df as a series
# country can be 'England', 'Scotland', 'Wales', or 'Northern Ireland'
def getTowns(df, country):
	towns = df.loc[df['Country'] == country]['Town'].to_frame()
	return towns

def getWindSpeedsForTownsInCountry(df, country_name):

	towns = getTowns(df, country_name)


	for index, row in towns.iterrows():
	   	town = row['Town']
	   	try:
			wind_speed = owm.weather_at_place(town).get_weather().get_wind()['speed']
			towns['wind_speed'] = wind_speed
		except pyowm.exceptions.OWMError:
			pass
	return towns

def getAverageWindSpeedForTowns(towns):
	return towns['wind_speed'].mean()

owm = pyowm.OWM(owm_api_key)  

df = pd.read_csv('Towns_List_Simple.csv')

ni_towns = getWindSpeedsForTownsInCountry(df, 'Northern Ireland')
welsh_towns = getWindSpeedsForTownsInCountry(df, 'Wales')

avg_wind_speed_ni = getAverageWindSpeedForTowns(ni_towns)
avg_wind_speed_wales = getAverageWindSpeedForTowns(welsh_towns)

print avg_wind_speed_ni
print avg_wind_speed_wales






