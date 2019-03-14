import pandas as pd
import math as ma
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
import warnings
warnings.filterwarnings("ignore")
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)
data=pd.read_csv('patient.csv')
f1=data['COMFORT']
b=f1.mean(skipna=True)
b=ma.ceil(b)
data['COMFORT']=data['COMFORT'].fillna(b)
X=data.drop('COMFORT',axis=1)
X=pd.get_dummies(X,columns=["L-CORE","L-SURF","L-O2","L-BP","SURF-STBL","CORE-STBL","BP-STBL","DECISION"])
y=data.iloc[:, 7].values
# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=20)
# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
#Training the Gaussian Naive bayes classifier
model=GaussianNB()
model.fit(X_train,y_train)
#Making Predictions for gaussian Naive bayes
y_pred1=model.predict(X_test)
#Printing the accuracy of Gaussian Naive Bayes
gan_acc=round(model.score(X_train,y_train)*100, 2)
print("Gaussian Naive Bayes accuracy is:",gan_acc)
#Training the svc classifier
clf=SVC(kernel='linear',C=1).fit(X_train,y_train)
#Making predictions for SVC classifier
y_pred2=clf.predict(X_test)
#printing the accuracy of SVC classifier
acc_svc = round(clf.score(X_train, y_train) * 100, 2)
print("svm accuracy is:", acc_svc)
#KNN classifier fitting,prediction and displaying accuracy
knn = KNeighborsClassifier(n_neighbors = 3)
knn.fit(X_train, y_train)
y_pred3 = knn.predict(X_test)
acc_knn = round(knn.score(X_train, y_train) * 100, 2)
print("KNN accuracy is:",acc_knn)