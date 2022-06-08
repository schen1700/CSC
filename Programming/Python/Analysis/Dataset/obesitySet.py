import pandas as pd
import sklearn
import numpy as np
import csv
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist

frame = pd.read_csv('file.csv')       # Filename: ObesityDataSet.csv

### Declare Variables
# Takes original size of dataframe, adds a new report for NObeyesdad and 
# creates a nww size of dataframe.
ALPHA = 0.05
size = len(frame)

H = 'Height'
W = 'Weight'
N = 'NObeyesdad'

labels = [H, W, N]
for i in frame.columns:
    if i not in labels:
        frame.drop(i, axis = 1, inplace = True)

new_size = len(frame)
kMeansInit = 150
### Analysis
# Creates new dataframe for BMI values.
frame['BMI'] = frame['Weight'] / frame['Height'] ** 2
test_frame = pd.DataFrame(frame['BMI'])

# Creates the model using KMeans.
# Loop ranges from 2 through 10.
distortions = []
a = range(2, 11)
for k in a:
    clusters = KMeans(n_clusters = k, n_init = kMeansInit, random_state = 42).fit(test_frame)
    cmap = clusters.predict(test_frame)
    distortions.append(clusters.inertia_)
    meanDistortion = sum(np.min(cdist(test_frame,clusters.cluster_centers_, 'euclidean'), axis = 1)) / test_frame.shape[0]
    centroids = clusters.cluster_centers_[:10, 0]
    print(f"\nValue of k = {k}\nCentroid: {centroids}\nDistortion: {round(meanDistortion, 2)}")

# Plot ranges from 2 through 10.
# Labels for X and Y.
plt.plot(range(2, 11), distortions)
plt.xlabel('Cluster (K)')
plt.ylabel('Distortions')
plt.show()

NObese = len(frame['NObeyesdad'].unique())

### Output Streams
print(f"\nOriginal size: {size}")
print(f"Final data set of (n): {new_size}")

print("\nThe elbow graph is available for inspection.")
print("\nI. CDC 6-level obesity levels.\nII. or the study-specific ordinal levels.")
print("\nIn the plot, we can see that 4 is the optimal number of clusters for the dataset.")
print("\nAt k = 4 increases, then slowly decreases. The NObeyesdad count is: {NObese}")