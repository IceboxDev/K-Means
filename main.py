from sklearn.cluster import KMeans
from numpy import array

data = [int(i.strip()) for i in input("Data: ").strip().split(",")]
X = array(data).reshape(-1,1)
R = KMeans(n_clusters=2).fit(X)
print(R.cluster_centers_, end="\n\n")

LOW = [point for index, point in enumerate(data) if R.labels_[0] == R.labels_[index]]
HIGH = [point for index, point in enumerate(data) if R.labels_[-1] == R.labels_[index]]

print(*LOW, "|", *HIGH)