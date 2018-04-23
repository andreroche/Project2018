# André Roche 21-Apr-18 - testing on scitik learn and guessing species from inputs.

from sklearn.datasets import load_iris

iris = load_iris()

type (iris)

print ('The features values are:')
print (iris.data)  # print the iris data set
print('')
print ('The feature names and units of measurement are:')
print (iris.feature_names) # print the feature names
print('')
print ('The species target identity values are:') 
print (iris.target) # print the target values - either a 0,1 or 2 (the species)
print('')
print ('The species names are as follows:')
print (iris.target_names) # print hte names of the species

print('')
print (type(iris.data)) # what type is the data (it should be an numpy array)
print (type(iris.target)) # print what type is the target (it should be a numpy array)

print (iris.data.shape) # print the shape of the data (it should be 150 by 4)
print (iris.target.shape) # print he shape of the target (it should be 150)

X = (iris.data) # assign X to the data (the feature data)
y = (iris.target) # assign y to the target (the species)



print (X.shape) # print the shape of X
print (y.shape) # print he shape of y
print('')

# using stats for classification. first method is K nearest neighbors
from sklearn.neighbors import KNeighborsClassifier  # import 
knn= KNeighborsClassifier(n_neighbors=1) # define and use K = 1

print (knn) # print 

knn.fit(X,y) # fit
X_old = ([[1,2,3,4]])

print('The results of the prediction are as follows:')

knn.predict(X) # predict from this array
print (knn.predict(X_old)) # print the prediction to screen

X_new = ([[3,5,4,2], [5,4,3,2]])
knn.predict (X_new)
print (knn.predict(X_new)) # print the prediction to screen

knn = KNeighborsClassifier(n_neighbors = 3) # change k to K= 3
knn.fit(X,y)
knn.predict(X_new)
print (knn.predict(X_new))  # the results from the new prediction where this time K=3


# different method for classification. it is not similiar to linear regression 

from sklearn.linear_model import LogisticRegression # import
logreg = LogisticRegression() # define
logreg.fit(X,y) # perform the fit 
logreg.predict(X_new) # make the prediction for X_new with this method 

print(logreg.predict(X_new)) # print the prediction to screen

print ('Where 0 = Setosa, 1 = Versicular, 2 = Virginica ')



