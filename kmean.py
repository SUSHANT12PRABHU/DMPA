import csv
import random
import itertools
def formClusters(Centroids,dataset):
	cluster = {}
	for point in dataset:
		cdist = []
		for c in Centroids:
			dist= 0
			dist = round((sum([(x-y)**2 for x,y in zip(point,c)]))**0.5,2)
			cdist.append(dist)
		print("Distance vector is: ",cdist)
		cluster[point] = cdist.index(min(cdist))
	return cluster

def compCentroid(points,n):
	if points != []:
		centroid = []
		for i in range(n):
			val = round(sum([axis[i] for axis in points]) / len(points) ,2)
			centroid.append(val)
		return(tuple(centroid))

# FileInput
filename = input("Enter Dataset Filename to apply K-Mean: ")
attributes = []
data = []
# FileRead
with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file)
    attributes = next(csv_reader)
    for row in csv_reader:
        row = tuple(map(float,row))
        data.append(row[1:])

# DataValues
print("Datapoints extracted from file are: ",data)

# ClusterSize
k = int(input("Enter Number of Clusters required: "))
centroids=[]
i = 0
while i != k:
	point = tuple(data[random.randint(0,(len(data)-1))])
	if point not in centroids:
		centroids.append(point)
		i = i + 1

print("Randomly assigned Centroids are: ",centroids)
old_clusters = formClusters(centroids,data)
print("First cluster: ",old_clusters)
counter = 0
new_clusters = old_clusters
while True:
	centroids = []
	new_k_cent = []
	for i in range(k):
		k_th_clus = [x for x,y in new_clusters.items() if y == i]
		new_k_cent.append(compCentroid(k_th_clus,(len(attributes)-1)))
	print("New centroids: ",new_k_cent)
	old_clusters = new_clusters
	new_clusters = formClusters(new_k_cent,data)
	print("New cluster: ",new_clusters)
	if new_clusters == old_clusters:
		counter = counter + 1
		if counter == 2:
			break
print("Centroids are : ",new_k_cent)
ans=[]
print("Final cluster obtained is : ",new_clusters)
for k in new_clusters :
	print(" ",new_clusters[k]," ",k)
