import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import Lasso
from sklearn.preprocessing import normalize

from utils import get_dataframe

# Load data:
df = get_dataframe(solar_noon_altitudes=True)

X = df.drop(['RSKF', 'Datum und Uhrzeit', 'Gesamtanlage[kWh]'], axis=1) # TODO: Use RSKF
columns = X.columns
X = normalize(X, axis=0)
y = df['Gesamtanlage[kWh]']

alpha = 2.5e-3 # Regularization factor
reg = Lasso(alpha).fit(X, y)

coefficients = pd.concat([pd.DataFrame(columns),pd.DataFrame(np.transpose(reg.coef_))], axis = 1) # Normalize features to get an idea about their importance.

print("Regularization factor: ", alpha)
print(coefficients)
print("R^2: ", reg.score(X,y))