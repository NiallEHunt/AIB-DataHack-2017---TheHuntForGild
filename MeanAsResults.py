import pandas as pd
import numpy as np
data = pd.read_csv("data")

average = data['Bikes'].mean

average = data['Bikes'].mean()

print(average)