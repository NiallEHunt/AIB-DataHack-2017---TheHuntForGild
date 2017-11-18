import numpy as np
import pandas as pd
from pandas.tseries.holiday import USFederalHolidayCalendar as calendar
import datetime

bikes = pd.read_csv("Bikes.csv")
holidays = pd.read_csv("Holidays.csv")
weather = pd.read_csv("Weather.csv")
holidays = pd.read_csv("Holidays.csv")
final_test = pd.read_csv("Final Test.csv")


#print("Bikes Dataset Head:")
#print(bikes.head())
#print(bikes)

print("Holidays Dataset Head:")
print(holidays.head())

#print("Weather Dataset Head:")
#print(weather.head())

#print("Final Test Dataset Head:")
#print(final_test.head())
#print(holidays["Date"])


#print(df)
#df['Date'] = datetime.date.fromordinal(holidays['Date'])
#df['Date'] = pd.to_datetime(holidays['Date'], format='%Y%m%d.0')
#print (df)