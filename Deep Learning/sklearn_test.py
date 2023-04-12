import matplotlib.pyplot as plt
import numpy as np
# from sklearn.datasets._samples_generator import make_blobs
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

""" tutorial: Blockchain Data Analytics, for Dummies"""

k = [2,3,4,5,6,7,8]

X, y_true = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# kmeans = KMeans(n_clusters=5)
# kmeans.fit(X)
# y_kmeans = kmeans.predict(X)

# plt.subplot(121)
# plt.scatter(X[:, 0], X[:, 1], s=50, c=y_kmeans, cmap='viridis')
# plt.xlabel('Rating')
# plt.ylabel('Months as Customer')
# plt.show()


wss = []
for i in k:
    km = KMeans(n_clusters=1, max_iter=1000, random_state=47)
    km.fit(X)
    wss.append(km.inertia_)
# plt.subplot(122)
plt.plot(k, wss)
plt.xlabel("Value for k")
plt.ylabel("WSS")
plt.show()