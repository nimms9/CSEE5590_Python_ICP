import warnings
warnings.filterwarnings("ignore")
from keras.models import Sequential
from keras.layers.core import Dense, Activation
import pandas as pd
from sklearn.preprocessing import LabelEncoder
# load dataset
from sklearn.model_selection import train_test_split
dataset = pd.read_csv("Breas Cancer.csv")
dataset=dataset.drop('fractal_dimension_worst',axis=1)
x1=dataset.drop('diagnosis',axis=1)
y1=dataset['diagnosis']
Lbely=LabelEncoder()
y1=Lbely.fit_transform(y1)
y1=pd.DataFrame(y1)
import numpy as np
X_train, X_test, Y_train, Y_test = train_test_split(x1, y1,
                                                    test_size=0.25, random_state=87)
np.random.seed(155)
my_first_nn = Sequential() # create model
my_first_nn.add(Dense(50, input_dim=30, activation='relu')) # hidden layer
my_first_nn.add(Dense(60,activation='sigmoid'))# added another hidden layer
my_first_nn.add(Dense(1, activation='sigmoid')) # output layer
my_first_nn.compile(loss='binary_crossentropy', optimizer='adam')
my_first_nn_fitted = my_first_nn.fit(X_train, Y_train, epochs=100,verbose=0,
                                     initial_epoch=0)
print(my_first_nn.summary())
print(my_first_nn.evaluate(X_test, Y_test,verbose=0))