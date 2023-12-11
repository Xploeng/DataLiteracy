import matplotlib.pyplot as plt
import numpy as np

import get_project_data

# Load data:
df = get_project_data.df


# Group by month:
n_days = len(df)

months_from_june = []
for k in range(n_days):
    months_from_june.append(6 - np.abs(int(df["Datum und Uhrzeit"][k][3:5])-6))


# Plotting:
fig, ax = plt.subplots()

sc = plt.scatter(df[" SDK"], df["Gesamtanlage[kWh]"], c=months_from_june, cmap='jet')

cbar = plt.colorbar(sc)
cbar.ax.get_yaxis().set_ticks([])

for j, month in enumerate(['Dec','Nov/Jan','Oct/Feb','Sep/Mar','Aug/Apr','Jul/May','Jun']):
    cbar.ax.text(1.5, j, month, ha='left', va='center')
    #cbar.ax.text(1.5, 6/7*(j + .5), month, ha='left', va='center')

plt.xlabel("Hours of sunshine")
plt.ylabel("Electricity produced in kWh")

plt.show()