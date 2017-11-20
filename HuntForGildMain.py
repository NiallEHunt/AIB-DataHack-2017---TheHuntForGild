import numpy as np
import pandas as pd
import datetime

verbose = True

def check_date(date):
    correct_date = None
    try:
        newDate = date
        correct_date = True
    except ValueError:
        correct_date = False
    return correct_date


# Reading given data
bikes = pd.read_csv("Bikes.csv")
holidays = pd.read_csv("Holidays.csv")
weather = pd.read_csv("Weather.csv")
final_test = pd.read_csv("Final Test.csv")

if verbose:
    print("Reading in given data ...")

holidays['Date'] = pd.to_datetime(holidays['Date'], unit='s')

# Formatting data into one .csv file with only the relevant features
# ID,Weekday,Month,AWND,PRCP,SNOW,SNWD,TAVG,TMAX,TMIN,Holiday
trainingData = pd.read_csv("SetupForTrainingData.csv")
mainDf = pd.DataFrame(trainingData,
                      columns=['ID', 'Weekday', 'Month', 'AWND', 'PRCP', 'SNOW',
                               'SNWD', 'TAVG', 'TMAX', 'TMIN', 'Holiday', 'Bikes'])

for i in range(0, len(bikes)-1):

    # Handling date from Bikes.csv
    t = pd.to_datetime(bikes.iloc[i]['Date'], format="%d/%m/%Y")

    weekday = t.weekday()
    mainDf.set_value(i, 'Weekday', weekday)

    month = t.month
    mainDf.set_value(i, 'Month', month)

    # Handling AWND PRCP SNOW SNWD TAVG TMAX TMIN from Weather.csv
    awnd = weather.loc[i]['AWND']
    mainDf.set_value(i, 'AWND', awnd)

    prcp = weather.loc[i]['PRCP']
    mainDf.set_value(i, 'PRCP', prcp)

    snow = weather.loc[i]['SNOW']
    mainDf.set_value(i, 'SNOW', snow)

    tavg = weather.loc[i]['TAVG']
    mainDf.set_value(i, 'TAVG', tavg)

    tmax = weather.loc[i]['TMAX']
    mainDf.set_value(i, 'TMAX', tmax)

    tmin = weather.loc[i]['TMIN']
    mainDf.set_value(i, 'TMIN', tmin)

    bikesNum = bikes.loc[i]['Bikes']
    mainDf.set_value(i, 'Bikes', bikesNum)

    # Handling holidays
    holidayvalue = 0
    for i in range(0, len(holidays)):
        if holidayvalue == 0:
            holiday = pd.to_datetime(holidays.iloc[i]['Date'], format="%d/%m/%Y")
            if holiday == t:
                holidayvalue = 1
    mainDf.set_value(i, 'Holiday', holidayvalue)

if verbose:
    print("Adding weekday and month to final table ...")
    print("Adding weather stats to final table ...")
    print("Adding holidays to the final table ...")

# Writing data to .csv
mainDf.to_csv("data.csv", index=False)
if verbose:
    print("Writing final table to data.csv ...")

print("Data table written to data.csv")
