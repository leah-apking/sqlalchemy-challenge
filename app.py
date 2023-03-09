import numpy as np
import pandas as pd
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
        f"Welcome to the API<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"api/v1.0/stations<br/>"
        f"api/v1.0/tobs"
    )

@app.route("api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    """Return the precipitation data for last 12 months"""

    end_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precip_data = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= end_date)
    session.close()

    precip = list(np.ravel(precip_data))

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
    """Return temperature data from Honolulu"""

    end_date = dt.date(2015, 10, 30) - dt.timedelta(days=365)
    station7_data = session.query(Measurement.date, Measurement.station, Measurement.tobs).\
    filter(Measurement.station == "USC00511918").\
    filter(Measurement.date >= end_date).all()
    session.close()

    temp = list(np.ravel(station7_data))

    return jsonify(temp)
@app.route("api/v1.0/<start>")
def start():
    """Fetch the maximum, minimum, and average temperature for provided date"""

if__name__ == "__main__":
    app.run(debug=True)