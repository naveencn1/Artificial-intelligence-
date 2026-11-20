# CSA17 - Artificial Intelligence | Experiment 32 (Manual Ex. 4.2): Linear Regression
# Name            : V V Naveen Kumar
# Register Number : 192321018

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

rng = np.random.RandomState(42)
X = rng.uniform(0, 10, size=(100, 1)) # e.g. hours studied
y = 3.5 * X.ravel() + 8 + rng.normal(0, 2, size=100) # e.g. marks, with noise

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

model = LinearRegression()
model.fit(X_train, y_train)

pred = model.predict(X_test)
print("Slope (coefficient): %.3f" % model.coef_[0])
print("Intercept : %.3f" % model.intercept_)
print("MSE : %.3f" % mean_squared_error(y_test, pred))
print("R-squared : %.3f" % r2_score(y_test, pred))
print("Prediction for x = 7.5 :", round(float(model.predict([[7.5]])[0]), 2))


# ============================================================
# OUTPUT
# ============================================================
# Slope (coefficient): 3.357
# Intercept : 8.609
# MSE : 2.954
# R-squared : 0.975
# Prediction for x = 7.5 : 33.79
