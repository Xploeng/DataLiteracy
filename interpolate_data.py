import pandas as pd
from get_project_data import get_weather_data
import numpy as np

def IDW_interpolation(distances, feature_values, power):
    # calculate weighted sum of known values based on distances
    num = np.sum(feature_values/(distances**power))
    # calculate sum of weights (inverse of distances)
    weights = np.sum(1/(distances**power))
    # calculate the interpolated value
    interpolated_value = num/weights
    return(interpolated_value)

def IDW_interpolation_all_values(distances, station_1, station_2, station_3, power):
    interpolated_values = []
    i = 0
    while i < station_1.size:
        feature_values = np.array([station_1[i], station_2[i], station_3[i]])
        interpolated_value = IDW_interpolation(distances, feature_values, power)
        interpolated_values.append(interpolated_value)
        i = i + 1
    return(interpolated_values)

## Interpolate feature SDK = tägliche Sonnenscheindauer in h
## Get weather data from station 'München Stadt', Stations_id: 03379
station_muenchen = get_weather_data("data/produkt_klima_tag_19540601_20221231_03379.txt", station_id='03379')
## Get weather data from station 'Augsburg', Stations_id: 00232
station_augsburg = get_weather_data('data/produkt_klima_tag_19470101_20221231_00232.txt', station_id='00232')
## Get weather data from station 'Kaufbeuren-Oberbeuren', Stations_id: 15555
station_kaufbeuren = df = get_weather_data('data/produkt_klima_tag_20160501_20221231_15555.txt', station_id='15555')





