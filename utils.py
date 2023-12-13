import pandas as pd
import datetime
from suncalc import get_position, get_times

def get_dataframe(type='csv', solar_noon_altitudes=False):
    '''
    @type 'csv' | 'xlsx'
    @solar_noon_altitudes default = True, determines wether to include solar/noon altitudes in df
    @return pv and weather data as pandas dataframe
    '''
    df =  pd.read_csv("data/pv_weather_data_2019_to_2022."+ type, sep=" ")
    if solar_noon_altitudes:
        df['Solar noon altitudes'] = _gen_solar_noon_altitudes(df)
        
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
