import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings("ignore")

dataset = pd.read_csv('College.csv')
x = dataset.iloc[:,[4,5,6,7]]

# Create a minimum and maximum processor object
scaler = preprocessing.MinMaxScaler()
# Create an object to transform the data to fit minmax processor
X_scaled_array = scaler.fit_transform(x)
# Run the normalizer on the dataframe
X_scaled = pd.DataFrame(X_scaled_array, columns = x.columns)
print(X_scaled)


nclusters = 4 # this is the k in kmeans
seed = 10

km = KMeans(n_clusters=nclusters, random_state=seed)
km.fit(X_scaled)

# predict the cluster for each data point
y_cluster_kmeans = km.predict(X_scaled)

#Calculate silhouette score
from sklearn import metrics
score = metrics.silhouette_score(X_scaled, y_cluster_kmeans)
print('silhouette_score :', score)


LABEL_COLOR_MAP = {0 : 'r',
                   1 : 'k',
                   2: 'g',
                   3: 'y'
                   }
label_color = [LABEL_COLOR_MAP[l] for l in km.predict(X_scaled)]
plt.scatter(X_scaled_array[:, 0], X_scaled_array[:, 1], c=label_color)
plt.title("Clustering based on enrollment,Freshman.Undergrad and \nthe Top 10 percentile,25 percentile in students")
plt.show()