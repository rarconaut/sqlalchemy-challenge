# sqlalchemy-challenge
SQLAlchemy Challenge Homework 10 - Surfs Up!

To help plan a long holiday vacation in Honolulu, Hawaii, this project does some climate analysis on the local weather to help with the trip planning. What follows is an outline for the project: 

STEP 1 - Climate Analysis and Exploration
To begin, Python and SQLAlchemy are used to do basic climate analysis and data exploration of the Hawaii climate database. All of the following analysis were completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

Precipitation Analysis
Designed a query to retrieve the last 12 months of precipitation data.
Used Pandas to print the summary statistics for the precipitation data.

Station Analysis
Designed a query to calculate the total number of stations.
Designed a query to find the most active stations.
Designed a query to retrieve the last 12 months of temperature observation data (TOBS), filtered by the station with the highest number of observations, and plotted the results as a histogram.



STEP 2 - Climate App
After completing the initial analysis, a Flask API was designed to share the results, based on the queries that were developed in Step 1. 



BONUS - Other Recommended Analyses
Temperature Analysis II
Used the calc_temps function with a start date and end date to return the minimum, average, and maximum temperatures for that range of dates for a Hawaii trip using the matching dates from a previous year (i.e., using "2017-01-01" if the trip start date was "2018-01-01").
Plotted the min, avg, and max temperature from the query as a bar chart.

Daily Rainfall Average
Calculated the rainfall per weather station using the previous year's matching dates.
Calculated the daily normals, which are the averages for the min, avg, and max temperatures.
Used Pandas to plot an area plot the daily normals.
