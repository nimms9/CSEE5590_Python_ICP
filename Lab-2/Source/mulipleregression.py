import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import warnings
warnings.filterwarnings("ignore")

# Importing the dataset
dataset = pd.read_csv('servo.csv')
print(dataset.corr())


y = dataset.iloc[:,2].values
X = dataset.drop(['pgain'],axis=1)




#categorizing data
X = pd.get_dummies(X, columns=["motor","screw"])

print(X.isnull().sum())

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 35)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
model = regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

#Evaluating the model
from sklearn.metrics import mean_squared_error, r2_score
print("Variance score: %.2f" % r2_score(y_test,y_pred))
print("Mean squared error: %.2f" % mean_squared_error(y_test,y_pred))
plt.scatter(y_pred, y_test, alpha=.75,
            color='b')  # alpha helps to show overlapping data
plt.xlabel('Predicted ')
plt.ylabel('Actual ')
plt.title('Multiple Linear Regression Model')
plt.show()