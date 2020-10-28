# Import dependencies
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# Save references to the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Flask Setup
app = Flask(__name__)


# Flask Routes
@app.route("/")
def home():
    # """List all available api routes."""
    print("Server received request for 'Home' page...")
    return (
        f"The available routes are:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start> and /api/v1.0/<start>/<end>"
    )


# Define what to do when a user hits the /about route
@app.route("/api/v1.0/precipitation")
def precipitation():
    print("Server received request for 'Precipitation' page...")
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # """Convert the query results to a dictionary using date as the key and prcp as the value."""
    # Query all dates and prcp
    results = session.query(Measurement.date, Measurement.prcp).all()
    session.close()

    # Create a dictionary from the row data and append to a list of all_precip
    precipitation = []
    for prcp in results:
        precip_dict = {}
        precip_dict["date"] = prcp
        precipitation.append(precip_dict)

    return jsonify(precipitation)


@app.route("/api/v1.0/stations")
def stations():
    print("Server received request for 'Stations' page...")
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # """Return a JSON list of stations from the dataset"""
    # Query all stations
    results = session.query(Measurement.station).distinct().all()
    session.close()

   # Convert list of tuples into normal list
    stations = list(np.ravel(results))

    return jsonify(stations)


@app.route("/api/v1.0/tobs")
def tobs():
    print("Server received request for 'Observed Temps' page...")
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # """Query the dates and temperature observations of the most active station for the last year of data."""
    # """Return a JSON list of temperature observations (TOBS) for the previous year."""
    # Query all stations
    sel = [Measurement.date, Measurement.tobs]
    results = session.query(*sel).\
    filter(Measurement.date <= '2017-08-23').\
    filter(Measurement.date >= '2016-08-23').\
    filter(Measurement.station == 'USC00519281').\
    group_by(Measurement.date).all()
    
    session.close()

   # Convert list of tuples into normal list
    tobs = list(np.ravel(results))

    return jsonify(tobs)


@app.route("/api/v1.0/<start>")
def start(start):
    print("Server received request for 'Start Date' page...")
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # """Return a JSON list of the min temp, the avg temp, and the max temp for a given start date."""
    # """Calculate TMIN, TAVG, and TMAX for all dates >= to the start date."""
    # Query TMIN, TAVG, and TMAX for start date
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).all()
    
    session.close()

   # Convert list of tuples into normal list
    start_date = list(np.ravel(results))

    return jsonify(start_date)



@app.route("/api/v1.0/<start>/<end>")
def date_range(start, end):
    print("Server received request for 'Date Range' page...")
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # """Return a JSON list of the min temp, the avg temp, and the max temp for a given start date."""
    # """Calculate the TMIN, TAVG, and TMAX for dates between the start/end date, inclusive."""
    # Query TMIN, TAVG, and TMAX for start date
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    
    session.close()

   # Convert list of tuples into normal list
    start_date = list(np.ravel(results))

    return jsonify(start_date)


if __name__ == "__main__":
    app.run(debug=True)