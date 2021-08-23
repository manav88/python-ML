x=[[0],[18],[28],[36],[45],[52],[70],[100]]
y=[98,98,95,88,78,70,47,32]

from sklearn.neighbors import KNeighborsClassifier
nei=KNeighborsClassifier(n_neighbors=5)
nei.fit(x,y)
print(nei.predict([[20],[30],[5],[89]]))