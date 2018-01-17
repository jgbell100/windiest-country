# windiest-country
Uses the Open Weather Map API to report which of the countries of the UK are currently the windiest, on average.

Quick hack.

* For each country in the UK, takes a list of all the towns within that country and uses the [Open Weather Map API](https://openweathermap.org/api) to find out the current wind speed in these towns. 
* Calculates the average (mean) wind speed across these towns
* prints which country has the highest average wind speed and what its value is (in mph)

Uses [csv of Towns in the UK](https://www.paulstenning.com/wp-content/uploads/2015/05/Towns_List.csv) created by Paul Stenning.

## Requirements 

* Google Maps API key
* Open Weather Map API key

## Usage

To generate a csv file which contains the latitude and longitude of the towns in the UK:

`python get-lat-long.py <csv file containing list of towns>` (see above)

To report on which country is the windiest:

`python wind-comparison.py <csv file containing list of towns with lat and long>`

