import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

app = Flask(__name__)

@app.route("/")
def welcome():
    """List of all available api routes."""
    return(
        f"Welcome to the Hawaiian climate API<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"api/v1.0/stations<br/>"
        f"api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"Note: please enter start date in YYYY-MM-DD format.<br/>"
        f"/api/v1.0/start/end<br/>"
        f"Note: please enter start date first and end date last in YYYY-MM-DD/YYYY-MM-DD format.<br/>"
    )

# create a dictionary
@app.route("api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    """Return the precipitation data for most recent 12 months"""

    end_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= end_date)
    
    session.close()

    precip = []
    for date, prcp in results:
        precip_dict = {}
        precip_dict["date"] = date
        precip_dict["prcp"] = prcp
        precip.append(precip_dict)

    return jsonify(precip)

@app.route("api/v1.0/stations")
def stations():
    session = Session(engine)
    """Return information on stations"""

    station_data = session.query(Station)
    session.close()

    stations = list(np.ravel(station_data))
    return jsonify(stations)

@app.route("api/v1.0/tobs")
def tobs():
    session = Session(engine)
    """Return temperature data from Waihee"""

    end_date = dt.date(2015, 10, 30) - dt.timedelta(days=365)
    station7_data = session.query(Measurement.date, Measurement.station, Measurement.tobs).\
    filter(Measurement.station == "USC00519281").\
    filter(Measurement.date >= end_date).\
    order_by(Measurement.date).all()
    session.close()

    temp = list(np.ravel(station7_data))
    return jsonify(temp)

@app.route("api/v1.0/<start>")
def start(start_date):
    session = Session(engine)
    """Fetch the minimum, average, and maximum temperature for provided date"""

    start_results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
    filter(Measurement.date >= start_date).all()
    session.close()

    date_data = list(np.ravel(start_results))
    return jsonify(date_data)

@app.route("api/v1.0/<start>/<end>")
def start(start_date, end_date):
    session = Session(engine)
    """Fetch the minimum, average, and maximum temperature for provided date range"""

    range_results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
    filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
    session.close()

    range_data = list(np.ravel(range_results))
    return jsonify(range_data)

if __name__ == "__main__":
    app.run(debug=True)