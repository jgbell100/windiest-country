# windiest-country
Uses the Open Weather Map API to report which of the countries of the UK are currently the windiest.

Quick hack.

* For each country in the UK, takes a list of all the towns within that country and uses the [Open Weather Map API](https://openweathermap.org/api) to 
find out the current wind speed in these towns. 
* Calculates the average (mean) wind speed across these towns
* prints which country has the highest average wind speed and what its value is (in mph)

Uses [csv of Towns in the UK](https://www.paulstenning.com/wp-content/uploads/2015/05/Towns_List.csv) created by Paul Stenning.

## Usage

`python <csv file containing list of towns>` (see above)

You will need an Open Weather Map API key.
