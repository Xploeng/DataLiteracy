import pandas as pd

## get&filter pv data
def get_pv_data(PATH):
    df = pd.read_excel(PATH)
    # delete first row, which is metadata
    df = df.drop([0], axis=0)
    df.reset_index(inplace=True)
    del df["index"]
    # delete last row, which is the 1.1. of the next year, for leap year 2020 index of last row is 266, not 265
    if(PATH == "data/20-21.xlsx"):
        df = df.drop([366], axis=0)
    else:
        df = df.drop([365], axis=0)
    # exclude columns we don't need
    df = pd.concat([df["Datum und Uhrzeit"], df["Gesamtanlage"]], axis=1)
    return(df)

# get&filter weather data
def get_weather_data(PATH, station_id):
    df = pd.read_csv(PATH, sep=";")
    # extract years 2019-2022 from the dataset
    if station_id == '03379':
        df = df.iloc[23590:25051]
    elif station_id == '02905':
        df = df.iloc[17165:18626]
    elif station_id == '00232':
        df = df.iloc[26298:27759]
    elif station_id == '15555':
        df = df.iloc[975:2436]
    df.reset_index(inplace=True)
    # delete columns we don't need
    del df["index"]
    del df["STATIONS_ID"]
    del df["MESS_DATUM"]
    del df["eor"]
    del df["QN_3"]
    del df["QN_4"]
    remove_colname_spaces(df)
    return(df)

# remove the spaces in the column names of the dataset
def remove_colname_spaces(df):
    column_names = []
    for name in df.columns:
        name = name.lstrip()
        column_names.append(name)
    df.columns = column_names


def combine_pv_and_weather_data():
    ## get photovoltaik data
    # get pv data for year 2019
    df19 = get_pv_data("data/19-20.xlsx")
    # get pv data for year 2020, ATTENTION, 2020 was a schaltjahr with 366 days instead of 365
    df20 = get_pv_data("data/20-21.xlsx")
    # get pv data for year 2021
    df21 = get_pv_data("data/21-22.xlsx")
    # get pv data for year 2022
    df22 = get_pv_data("data/22-23.xlsx")
    # combine all years to one dataset 
    pv_df = pd.concat([df19, df20, df21, df22])
    pv_df.reset_index(inplace=True)
    del pv_df["index"]

    ## Get weather data 
    weather_df = get_weather_data("data/produkt_klima_tag_19540601_20221231_03379.txt", station_id='03379')

    ## Combine photovoltaik data and weather data to one dataset
    final_df = pd.concat([pv_df, weather_df], axis=1)
    final_df.rename(columns={"Gesamtanlage": "Gesamtanlage[kWh]"}, inplace=True)
    return(final_df)

## write dataset into a csv file
#final_df = combine_pv_and_weather_data()
#print(final_df)
#final_df.to_csv("data/pv_weather_data_2019_to_2022.csv", sep=" ", index=False, columns=final_df.columns)
