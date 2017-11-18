import numpy as np
import pandas as pd
import seabird as sb
#from pandas.tseries.holiday import USFederalHolidayCalendar as calendar
import datetime

def check_date(date):
    correctDate = None
    try:
        newDate = date
        correctDate = True
    except ValueError:
        correctDate = False
    return correctDate
bikes = pd.read_csv("Bikes.csv")
holidays = pd.read_csv("Holidays.csv")
weather = pd.read_csv("Weather.csv")
holidays = pd.read_csv("Holidays.csv")
final_test = pd.read_csv("Final Test.csv")


#print("Bikes Dataset Head:")
#print(bikes.head())
#print(bikes)

#print("Holidays Dataset Head:")
#print(holidays.head())

#print("Weather Dataset Head:")
#print(weather.head())

#print("Final Test Dataset Head:")
#print(final_test.head())
#print(holidays["Date"])

holidays['Date']=pd.to_datetime(holidays['Date'], unit='s')
#print(holidays['Date'])

#print(bikes)
#sal[sal['Year']==2013]['JobTitle']
validDates = 0
for i in range(0, len(holidays)):
    t = holidays.iloc[i]['Date']
    print(t.weekday())
    print(t.month())
    print(holidays.iloc[i]['Date'])

#print(bikes) # 2016-11-11 - Friday - 4


##For loop check through dates in bikes to check are they a holiday if so true holiday boolean in main dataframe