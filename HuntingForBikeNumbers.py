import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv("data", index_col=0)

print(data.head())
print(data.tail())
print(data.shape)

#,ID,Weekday,Month,AWND,PRCP,SNOW,SNWD,TAVG,TMAX,TMIN,Holiday,Bikes

sns.pairplot(data, x_vars=['Weekday', 'Month', 'AWND'], y_vars='Bikes', size=7, aspect=0.7, kind='reg')
plt.show()

X = data[['Weekday', 'Month', 'AWND', 'PRCP', 'SNOW', 'TAVG', 'TMAX', 'TMIN']]

print(X.head())

Y = data[['Bikes']]

print(type(X))
print(X.shape)

print(Y.head())

print(type(Y))
print(Y.shape)


X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state=1)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

linreg = LinearRegression()

linreg.fit(X_train, y_train)

print(linreg.intercept_)
print(linreg.coef_)
