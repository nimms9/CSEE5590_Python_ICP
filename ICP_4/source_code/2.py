from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
import pandas as pd
#Reading the 'iris' dataset
ds=pd.read_csv("iris.csv")
#Preprocessing
x=ds.drop('class',axis=1)
y=ds['class']
#Train Test Split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=20)
#Training the classifier
clf=SVC(kernel='linear',C=1).fit(x_train,y_train)
#Making Predictions
y_pred=clf.predict(x_test)
#Computed the confusion matrix to evaluate the accuracy of a classification
print("Confusion matrix:\n",confusion_matrix(y_test,y_pred))