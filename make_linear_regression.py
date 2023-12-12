import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from suncalc import get_position, get_times
import datetime
from datetime import timezone
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.preprocessing import normalize

import get_project_data

# Load data:
df = get_project_data.df
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

df['Solar noon altitudes'] = solar_noon_altitudes

#print(max(solar_noon_altitudes))
#print(dates[solar_noon_altitudes.idxmax()])

X = df.drop(['RSKF', 'Datum und Uhrzeit', 'Gesamtanlage[kWh]'], axis=1) # TODO: Use RSKF
columns = X.columns
X = normalize(X, axis=0)
y = df['Gesamtanlage[kWh]']

alpha = 2.5e-3 # Regularization factor
reg = Lasso(alpha).fit(X, y)

coefficients = pd.concat([pd.DataFrame(columns),pd.DataFrame(np.transpose(reg.coef_))], axis = 1)

print("Regularization factor: ", alpha)
print(coefficients)
print("R^2: ", reg.score(X,y))