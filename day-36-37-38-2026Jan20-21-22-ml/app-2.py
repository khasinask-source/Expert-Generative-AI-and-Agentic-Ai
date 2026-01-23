import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('Investment.csv')

X = dataset.iloc[:, :-1]
y = dataset.iloc[:, 1]

X = pd.get_dummies(X, dtype=int)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

