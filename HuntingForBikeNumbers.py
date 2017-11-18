import pandas as pd
import seaborn as sns

data = pd.read_csv("data", index_col=0)

print(data.head())
print(data.tail())
print(data.shape)

sns.pairplot(data, x_vars=['Weekday','Month','AWND','PRCP','SNOW','SNWD','TAVG','TMAX','TMIN','Holiday'], y_vars='Bikes', size=7, aspect=0.7, kind='reg')