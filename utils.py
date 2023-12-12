import pandas as pd

def get_dataframe(type='csv'):
    return pd.read_csv("data/pv_weather_data_2019_to_2022."+ type, sep=" ")
