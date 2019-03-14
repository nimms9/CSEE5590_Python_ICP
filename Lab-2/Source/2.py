import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.datasets import load_wine



# reading collge dataseta
dataset = pd.read_csv('holiday.csv')
data_frame = dataset.iloc[:,[2,3,6]]
print(dataset.dtypes)
print(data_frame.describe())

#normalizing and preprocessing Data
x=((data_frame-data_frame.min())/(data_frame.max()-data_frame.min()))*20
print(x);
scaler = preprocessing.StandardScaler()
scaler.fit(x)
X_scaled_array = scaler.transform(xa)
X_scaled = pd.DataFrame(X_scaled_array, columns = x.columns)


#X_scaled.sample(5)
nclusters = 3# this is K
seed = 0

km = KMeans(n_clusters=nclusters, random_state=seed)
km.fit(X_scaled)

# predict the cluster for each data point
y_cluster_kmeans = km.predict(X_scaled)


#computing silhouette_score
from sklearn import metrics
score = metrics.silhouette_score(X_scaled, y_cluster_kmeans)
print('silhouette_score :', score)

wcss =[]
##elbow method to know the number of clusters
for i in range(1,11):
    kmeans = KMeans(n_clusters=i,init='k-means++',max_iter=300,n_init=10,random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

plt.plot(range(1,11),wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()


#Plotting Clusters
LABEL_COLOR_MAP = {0 : 'red',
                   1 : 'black',
                   2 : 'cyan',
                   3 : 'green',
                   4 : 'gold',
                   5 : 'grey',
                   6 : 'indigo',
                   7 : 'pink',
                   8 : 'lightblue',
                   9 : 'blue',
                   10: 'navy'
                   }
label_color = [LABEL_COLOR_MAP[l] for l in km.predict(X_scaled)]
plt.scatter(X_scaled_array[:, 0], X_scaled_array[:, 1], c=label_color)
#plt.title("clustering Based on Outstate and Room.Board data in college.csv")
plt.show()