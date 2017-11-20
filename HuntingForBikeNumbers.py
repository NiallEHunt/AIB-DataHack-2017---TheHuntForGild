import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression

verbose = True

# Reading in data
data = pd.read_csv("data.csv", index_col=0)
if verbose:
    print("Reading data.csv ...")

# The following two lines are used to graphically represent the relation between the listed features (x_vars) and
# the numbers of Bikes borrowed on the same day
# sns.pairplot(data, x_vars=['Weekday', 'Month', 'Holiday'], y_vars='Bikes', size=7, aspect=0.7, kind='reg')
# plt.show()

feature_cols = ['Weekday', 'Month', 'AWND', 'PRCP', 'SNOW', 'TAVG', 'TMAX', 'TMIN', 'Holiday']
X = data[feature_cols]

Y = data[['Bikes']]

# The following line is used to split our training data into initial training and testing data
# X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state=1)

# Creating out linear regression model and training with the whole data set.
linreg = LinearRegression()

linreg.fit(X, Y)
if verbose:
    print("Training linear regression model ...")

# Training with our split training and testing data
# linreg.fit(X_train, y_train)

# Predicting bike numbers based on our test data
# y_pred = linreg.predict(X_test)

# Reading in the given test data
testing_data = pd.read_csv("Final Test.csv", index_col=0)
testing_data_feature_cols = testing_data[feature_cols]
if verbose:
    print("Reading final test data ...")

results = linreg.predict(testing_data_feature_cols)
if verbose:
    print("Predicting bike numbers ...")

# Writing our results given in an array to a .csv file
prevResults = pd.read_csv("Results.csv", index_col=0)
ourResults = pd.DataFrame(prevResults, columns=['ID', 'Total'])
for i in range(0, len(results)):
    ourResults.set_value(i, 'ID', i+1)
    ourResults.set_value(i, 'Total', results[i])
ourResults.to_csv("Final Results.csv", index=False)
if verbose:
    print("Writing results to Final Results.csv ...")

print("Results written to Final Results.csv")
