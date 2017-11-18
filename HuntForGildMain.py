import numpy as np
import pandas as pd
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

#ID,Weekday,Month,AWND,PRCP,SNOW,SNWD,TAVG,TMAX,TMIN,Holiday
trainingData = pd.read_csv("trainingData.csv")
#bikesFrame = pd.DataFrame(bikes['Bikes'])
mainDf = pd.DataFrame(trainingData,columns=['ID','Weekday','Month','AWND','PRCP','SNOW','SNWD','TAVG','TMAX','TMIN','Holiday','Bikes'])
#mainDf['ID'] = mainDf.ID.astype(np.int64)
for i in range(0, len(bikes)-1):
    # Handle ID
    # Handle Weekday Month Holiday Bikes using Bikes.csv
    #Bikes.csv - bikes
    #Date,Bikes
    #01/01/2015,2611
    t = pd.to_datetime(bikes.iloc[i]['Date'],format="%d/%m/%Y")
    #t.strftime('%a-%b-%Y')
    weekday = t.weekday()
    print(t)
    print("Weekday")
    print(t.weekday())
    print("Month")
    print(t.month)
    print(weekday)
    mainDf.set_value(i,'Weekday',weekday)
    #mainDf.iloc[i]['Weekday'] = (weekday)
    month = t.month
    mainDf.set_value(i,'Month',month)
    #print(mainDf.loc[holidays.Date == t, 'Holiday'])

    # Handle AWND PRCP SNOW SNWD TAVG TMAX TMIN from Weather.csv
    awnd=weather.loc[i]['AWND']
    mainDf.set_value(i,'AWND',awnd)
    prcp=weather.loc[i]['PRCP']
    mainDf.set_value(i,'PRCP',prcp)
    print(i)
    snow=weather.loc[i]['SNOW']
    mainDf.set_value(i,'SNOW',snow)
#   mainDf.iloc[i]['SNWD']=bikes.iloc[i]['Bikes']
    tavg=weather.loc[i]['TAVG']
    mainDf.set_value(i,'TAVG',tavg)
    tmax = weather.loc[i]['TMAX']
    mainDf.set_value(i,'TMAX',tmax)
    tmin=weather.loc[i]['TMIN']
    mainDf.set_value(i,'TMIN',tmin)
    bikesNum = bikes.loc[i]['Bikes']
    mainDf.set_value(i,'Bikes',bikesNum)
    #Holiday

    holidayvalue = 0
    for i in range(0, len(holidays)):
        if (holidayvalue == 0):
            holiday = pd.to_datetime(holidays.iloc[i]['Date'], format="%d/%m/%Y")
            if (holiday == t):
                print(holiday)
                print(holidays.iloc[i])
                print(holidays.iloc[i]['Date'])
                holidayvalue = 1
    mainDf.set_value(i, 'Holiday', holidayvalue)

    #sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']
#print(bikes) # 2016-11-11 - Friday - 4
print("hi")
print(mainDf)

mainDf.to_csv("data")

##For loop check through dates in bikes to check are they a holiday if so true holiday boolean in main dataframe