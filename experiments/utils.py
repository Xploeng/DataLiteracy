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

def draw_scatter_plot(df, save=False, continuous=False, name='kWh-sunshine-scatter.png'):
    n_days = len(df)
    
    color_gradient = []

    if continuous:
        for k in range(n_days):
            if k > 365 + 59: # adjusts count to gap year
                k -= 1
            if k % 365 < np.ceil(365/2):
                color_gradient.append(k % 365)
            else:
                color_gradient.append(365 - (k % 365))
    else:
        for k in range(n_days):
            color_gradient.append(6 - np.abs(int(df["Datum und Uhrzeit"][k][3:5])-6))
            
    # Tests gap year calc
    assert(color_gradient[0* 365 + 20] == color_gradient[1* 365 + 20] == color_gradient[2* 365 + 21])
    assert(df["Datum und Uhrzeit"][0* 365 + 20][:5] == df["Datum und Uhrzeit"][1* 365 + 20][:5] == df["Datum und Uhrzeit"][2* 365 + 21][:5])
    
        
    

    # Plotting:
    fig, ax = plt.subplots()

    
    sc = plt.scatter(df["SDK"], df["Gesamtanlage[kWh]"], c=color_gradient, cmap='jet')

    cbar = plt.colorbar(sc)
    cbar.ax.get_yaxis().set_ticks([])

    for j, month in enumerate(['Dec','Nov/Jan','Oct/Feb','Sep/Mar','Aug/Apr','Jul/May','Jun']):
        cbar.ax.text(1.5, j * color_gradient[30], month, ha='left', va='center')
        #cbar.ax.text(1.5, 6/7*(j + .5), month, ha='left', va='center')

    plt.xlabel("Hours of sunshine")
    plt.ylabel("Electricity produced in kWh")

    if save:
        plt.savefig("report/fig/" + name)
    plt.show()
