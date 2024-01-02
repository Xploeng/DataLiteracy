import pandas as pd
from get_project_data import get_weather_data
import numpy as np

## Interpolate feature SDK = tägliche Sonnenscheindauer in h
## Get weather data from station 'München Stadt', Stations_id: 03379
station_muenchen = get_weather_data("data/produkt_klima_tag_19540601_20221231_03379.txt", station_id='03379')
print(station_muenchen)
## Get weather data from station 'Augsburg', Stations_id: 00232
station_augburg = get_weather_data('data/produkt_klima_tag_19470101_20221231_00232.txt', station_id='00232')
print(station_augburg)
## Get weather data from station 'Kaufbeuren-Oberbeuren', Stations_id: 15555
station_kaufbeuren = df = get_weather_data('data/produkt_klima_tag_20160501_20221231_15555.txt', station_id='15555')
print(station_kaufbeuren)




## Get weather data from station 'Lechfeld', Stations_id: 02905
#station_lechfeld = get_weather_data("data/produkt_klima_tag_19690101_20221231_02905.txt", station_id='02905')



