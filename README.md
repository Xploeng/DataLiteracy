# DataLiteracy

project for data literacy module

## Source for weather data

[Datasource](https://www.dwd.de/DE/leistungen/cdc/climate-data-center.html;jsessionid=620CDE4EACF97A8A00479EB9AF4A955E.live11054?nn=495662)

## Dataset: Meaning of each column

| Collumn | Description |
| :--- | :--- |
| Datum und Uhrzeit | Year, day and time on which the data was collected
| Gesamtanlage[kWh] | generated energy in kWh by the photovoltaik module
|FX | daily maximum wind speed in m/s
| FM | daily mean wind speed in m/s
| RSK | daily precipitation/rainfall in mm
| RSKF | form of precipitation in numerical code (0:no precipitation, 4: form not known, but precipitation was recorded , 6: only rain, 7: only snow, 8: rain and snow, and/or Sleet)
| SDK | daily hours of sunshine in h
| SHK_TAG | daily value of height of snow in cm
| NM | daily value of cloud cover in 1/8 (= degree of cloudiness)(0/8: no clouds, 1/8 to 3/8: slightly cloudy, 4/8 to 6/8: cloudy, 7/8: very cloudy, 8/8: overcast)
| VPM | daily value of vapor pressure in hPa
| PM | daily mean of vapor pressure in hPa
| TMK | daily mean of air temperature in 2m height in °C
| UPM | daily mean of relative humidity in %
| TXK | daily maximum of air temperature in 2m height in °C
| TNK | daily minimum of air temperature in 2m height in °C
| TGK | minimum of air temperature at the ground in 5cm height in °C
| SNA | peak of sun altitude in rad
