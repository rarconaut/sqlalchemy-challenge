# sqlalchemy-challenge
SQLAlchemy Challenge Homework 10 - Surfs Up!

To help plan a long holiday vacation in Honolulu, Hawaii, this project does some climate analysis on the local weather to help with the trip planning. What follows is an outline for the project: <br><br>

STEP 1 - Climate Analysis and Exploration <br>
To begin, Python and SQLAlchemy are used to do basic climate analysis and data exploration of the Hawaii climate database. All of the following analysis were completed using SQLAlchemy ORM queries, Pandas, and Matplotlib. <br>

Precipitation Analysis <br>
Designed a query to retrieve the last 12 months of precipitation data. <br>
Used Pandas to print the summary statistics for the precipitation data. <br>

Station Analysis <br>
Designed a query to calculate the total number of stations. <br>
Designed a query to find the most active stations. <br>
Designed a query to retrieve the last 12 months of temperature observation data (TOBS), filtered by the station with the highest number of observations, and plotted the results as a histogram.
<br><br><br>


STEP 2 - Climate App <br>
After completing the initial analysis, a Flask API was designed to share the results, based on the queries that were developed in Step 1. 
<br><br><br>


BONUS - Other Recommended Analyses <br>
Temperature Analysis II <br>
Used the calc_temps function with a start date and end date to return the minimum, average, and maximum temperatures for that range of dates for a Hawaii trip using the matching dates from a previous year (i.e., using "2017-01-01" if the trip start date was "2018-01-01"). <br>
Plotted the min, avg, and max temperature from the query as a bar chart. <br>

Daily Rainfall Average <br>
Calculated the rainfall per weather station using the previous year's matching dates. <br>
Calculated the daily normals, which are the averages for the min, avg, and max temperatures. <br>
Used Pandas to plot an area plot the daily normals.
