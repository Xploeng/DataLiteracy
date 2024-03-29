import pandas as pd
import datetime
from suncalc import get_position, get_times
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def get_dataframe(type='csv', solar_noon_altitudes=False, interpolate_data=False):
    '''
    @type 'csv' | 'xlsx'
    @solar_noon_altitudes default = True, determines whether to include solar/noon altitudes in df
    @interpolate_data default False, determines whether to use interpolated features SDK, RSK and TMK
    @return pv and weather data as pandas dataframe
    '''
    if interpolate_data:
        df =  pd.read_csv("../data/interpolated_pv_weather_data_2019_to_2022."+ type, sep=" ")
    else:
        df =  pd.read_csv("../data/pv_weather_data_2019_to_2022."+ type, sep=" ")
    if solar_noon_altitudes:
        df['SNA'] = _gen_solar_noon_altitudes(df)
        
    return df

def _gen_solar_noon_altitudes(df):
    # Load data:
    n_points = int(len(df))


    # Calculations:
    lat, lon = 48.174597740503394, 11.236288062447413 # From Google Maps, for Fuerstenfeldbruck
    #days = []
    #months = []
    #years = []
    dates = []

    for date in df['Datum und Uhrzeit']:
        day = int(date[0:2])
        month = int(date[3:5])
        year = int(date[6:10])
        #days.append(date[0:2])
        #months.append(date[3:5])
        #years.append(date[7:11])
        date = datetime.datetime(year, month, day)
        #date = date.replace(tzinfo=timezone.utc) # TODO (?)
        dates.append(date)

    longitudes = pd.Series(n_points * [lon])
    latitudes = pd.Series(n_points * [lat])

    # Calculate the times of solar noon and the corresponding altitudes / angles:
    solar_noon_times = get_times(dates, longitudes, latitudes)['solar_noon']
    solar_noon_altitudes = get_position(solar_noon_times, longitudes, latitudes)['altitude']

    return solar_noon_altitudes

def get_astronomical_seasons(row):
    if (row["Month"] == 11 and row["Day"] >= 7) or (row["Month"] == 1) or (row["Month"] == 12) or (row["Month"] == 2 and row["Day"] <= 4):
        return "winter"
    elif (row["Month"] == 2 and row["Day"] >= 5) or (row["Month"] == 3) or (row["Month"] == 4) or (row["Month"] == 5 and row["Day"] <= 5):
        return "spring"
    elif (row["Month"] == 5 and row["Day"] >= 6) or (row["Month"] == 6) or (row["Month"] == 7) or (row["Month"] == 8 and row["Day"] <= 7):
        return "summer"
    elif (row["Month"] == 8 and row["Day"] >= 8) or (row["Month"] == 9) or (row["Month"] == 10) or (row["Month"] == 11 and row["Day"] <= 6):
        return "fall"