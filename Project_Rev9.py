# André Roche 27-Apr-2018 Project Final  - Programming and Scripting, Fisher's IRIS Data Set.
# The program / script was developed in blocks or segments as learning and investigation continued. 
# This includes learning of python as a tool in addition to the investigation of the dataset.
# For ease of review, each block will be named and will correspond with description of data in the final report.


# Block 1 - basic attempt to get some inforamtion from the dataset

import numpy # import the numpy library

# Please ensure that the iris dataset is loaded in working directory as presented in next line.
data = numpy.genfromtxt('data/iris_Dataset.csv', delimiter =',') # import dataset, genfromtxt function used to creat arrays from tabular data
from scipy import stats # import the scipy library , from that import the statistics module
from scipy.stats import skew, kurtosis, normaltest  # from the statistics module, import skew, kurtosis and normaltest

# Define each column. Assign data to these.The first column is the data in the first column and so on.
firstcol = data[:,0]  
secondcol = data[:,1] 
thirdcol = data[:,2]
fourthcol = data[:,3]

# Using numpy.mean to calculate the mean value of each column.
meanfirstcol = numpy.mean(data[:,0])
meansecondcol = numpy.mean(data[:,1])
meanthirdcol = numpy.mean(data[:,2])
meanfourthcol = numpy.mean(data[:,3])

# Using numpy.min to calculate the minimum value of each column.
minfirstcol = numpy.min(data[:,0])
minsecondcol = numpy.min(data[:,1])
minthirdcol = numpy.min(data[:,2])
minfourthcol = numpy.min(data[:,3])

# Using numpy.max to calculate the max value of each column. 
maxfirstcol = numpy.max(data[:,0])
maxsecondcol = numpy.max(data[:,1])
maxthirdcol = numpy.max(data[:,2])
maxfourthcol = numpy.max(data[:,3])

# Using numpy.std to calculate the standard deviation or spread value of each column.
stdfirstcol = numpy.std(data[:,0])
stdsecondcol = numpy.std(data[:,1])
stdthirdcol = numpy.std(data[:,2])
stdfourthcol = numpy.std(data[:,3])

# Using numpy.median to calculate the median value of each column.
medianfirstcol = numpy.median(data[:,0])
mediansecondcol = numpy.median(data[:,1])
medianthirdcol = numpy.median(data[:,2])
medianfourthcol = numpy.median(data[:,3])

# From the scipy library, using the stats module to calculate the skew of each column.
skewfirstcol = skew(data[:,0])
skewsecondcol = skew(data[:,1])
skewthirdcol = skew(data[:,2])
skewfourthcol = skew(data[:,3])

# From the scipy library, using the stats module to calculate the kurtosis of each column.
kurtfirstcol = kurtosis(data[:,0])
kurtsecondcol = kurtosis(data[:,1])
kurtthirdcol = kurtosis(data[:,2])
kurtfourthcol = kurtosis(data[:,3])

# From the scipy library, using the stats module to check 'normality' of the distribution of each column.
normfirstcol = normaltest(data[:,0])
normsecondcol = normaltest(data[:,1])
normthirdcol = normaltest(data[:,2])
normfourthcol = normaltest(data[:,3])


# Printing quality solution indicators/summary of data to screen.
print ('The Summary for Sepal Length is as follows:')
print ('Max =', maxfirstcol)
print ('Min =', minfirstcol)
print ('Mean =', meanfirstcol)
print ('Standard Deviation =', stdfirstcol)
print ('Median =', medianfirstcol)
print ('Skew =', skewfirstcol)
print ('Kurtosis = ', kurtfirstcol)
print ('Normality = ', normfirstcol)

print('')  # just print a line space on screen

print ('The Summary for Sepal Width is as follows:')
print ('Max =', maxsecondcol)
print ('Min =', minsecondcol)
print ('Mean =', meansecondcol)
print ('Standard Deviation =', stdsecondcol)
print ('Median =', mediansecondcol)
print ('Skew =', skewsecondcol)
print ('Kurtosis = ', kurtsecondcol)
print ('Normality = ', normsecondcol)

print('')  # just print a line space on screen

print ('The Summary for Petal Length is as follows:')
print ('Max =', maxthirdcol)
print ('Min =', minthirdcol)
print ('Mean =', meanthirdcol)
print ('Standard Deviation =', stdthirdcol)
print ('Median =', medianthirdcol)
print ('Skew =', skewthirdcol)
print ('Kurtosis = ', kurtthirdcol)
print ('Normality = ', normthirdcol)

print('')  # just print a line space on screen

print ('The Summary for Petal Width is as follows:')
print ('Max =', maxfourthcol)
print ('Min =', minfourthcol)
print ('Mean =', meanfourthcol)
print ('Standard Deviation =', stdfourthcol)
print ('Median =', medianfourthcol)
print ('Skew =', skewfourthcol)
print ('Kurtosis = ', kurtfourthcol)
print ('Normality = ', normfourthcol)

print('') # just print a line space on screen

# Anova test of multiple means (means of all four columns / all four feature characteristics)
stats.f_oneway(data[:,0],data[:,1], data[:,2],data[:,3]) # Anova (analysis of variance) test for more than two samples i.e. all features.
print('') # just print a line space on screen
print( 'Anova Results Are As Follows:') 
print(stats.f_oneway(data[:,0],data[:,1], data[:,2],data[:,3]))
print('')


import matplotlib.pyplot as pl  # import of matplotlib.pyplot library as pl alias. This is required for graphs.

pl.hist(firstcol)  # plot a histogram of the first column.
pl.show() # show the histogram

pl.hist(secondcol) # plot a histogram of the second column.
pl.show() # show the histogram

pl.hist(thirdcol) # plot a histogram of the third column.
pl.show() # show the histogram

pl.hist(fourthcol) # plot a histogram of the fourth column.
pl.show() # show the histogram


# Block 2 - use of librarys and associated modules for efficiency and more powerful tools.

# Using pandas to import and print the Iris Dataset on-screen.
import pandas as pd # import pandas library with pd alias
from pandas import scatter_matrix # import the scatter matrix tool
import seaborn as sns # import seaborn as sns alias
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import skew, kurtosis, kurtosistest, normaltest



df = sns.load_dataset('iris') # dataframe using seaborn to import the iris dataset. grouping the data by species column. 
df.groupby('species').mean() 
df.groupby('species').std()
df.groupby('species').median()
df.groupby('species').max()
df.groupby('species').min()

df.describe() #to give a statistical summary about the dataset
df.skew()
df.kurtosis()
print('')
print('Summary for the Dataset is as follows:')
print(df.describe())
#print(df.skew())
#print(df.kurtosis())
print('')
# Printing the quality solution indicators for each feature but grouped by species.
print('The Mean of each feature across species is as follows:')
print(df.groupby('species').mean())  
print('')
print('The Standard Deviation of each feature across species is as follows:')
print(df.groupby('species').std())
print('')
print('The Median of each feature across species is as follows:')
print(df.groupby('species').median())
print('')
print('The Max of each feature across species is as follows:')
print(df.groupby('species').max())
print('')
print('The Min of each feature across species is as follows:')
print(df.groupby('species').min())

print('')
print('The correlation of features across species is as follows:')
print(df.corr()) # printing a correlation between featues across the dataset


df.groupby('species').boxplot()
plt.show()


df.groupby('species').hist()
plt.show()

df.groupby('species').sepal_length.hist()
plt.show()

df.groupby('species').sepal_width.hist()
plt.show()

df.groupby('species').petal_length.hist()
plt.show()

df.groupby('species').petal_width.hist()
plt.show()

pd.plotting.scatter_matrix(df)
plt.show()

# Block 3 - using Seaborn for more powerful and descriptive pairplots to better visualise dataset

import pandas as pd
from pandas import scatter_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import skew, kurtosis, normaltest


df=pd.read_csv('data/iris_dataset.csv', header = None,
names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])

import seaborn as sns
sns.set(style = "ticks", color_codes = True)
iris = sns.load_dataset("iris")
p = sns.pairplot(iris)
plt.show()

import seaborn as sns
sns.set(style = "ticks", color_codes = True)
iris = sns.load_dataset("iris")
d = sns.pairplot(iris, hue = "species")
plt.show()

import seaborn as sns
sns.set(style = "ticks", color_codes = True)
iris = sns.load_dataset("iris")
f = sns.pairplot(iris, hue = "species", kind = "reg")
plt.show()

# Block 4  - Classification methods

from sklearn.datasets import load_iris

iris = load_iris()

type (iris)

print ('The features values are:') # print to screen the text in inverted commas
print (iris.data)  # print the iris data set
print('')
print ('The feature names and units of measurement are:')
print (iris.feature_names) # print the feature names
print('')
print ('The species target identity values are:') 
print (iris.target) # print the target values - either a 0,1 or 2 (the species)
print('')
print ('The species names are as follows:')
print (iris.target_names) # print the names of the species

print('')
print (type(iris.data)) # what type is the data (it should be an numpy array)
print (type(iris.target)) # print what type is the target (it should be a numpy array)

print (iris.data.shape) # print the shape of the data (it should be 150 by 4)
print (iris.target.shape) # print he shape of the target (it should be 150)

X = (iris.data) # assign X to the data (the feature data)
y = (iris.target) # assign y to the target (the species)



print (X.shape) # print the shape of X
print (y.shape) # print the shape of y
print('')

# using stats for classification. first method is K nearest neighbors.
from sklearn.neighbors import KNeighborsClassifier  # from library sklearn, import the function KNN or K nearest Neighbours  
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


# Different method for classification. Logistic Regression is not similiar to Linear Regression. 

from sklearn.linear_model import LogisticRegression # import
logreg = LogisticRegression() # define
logreg.fit(X,y) # perform the fit 
logreg.predict(X_new) # make the prediction for X_new with this method 

print(logreg.predict(X_new)) # print the prediction to screen

print ('Where: 0 = Setosa, 1 = Versicular, 2 = Virginica ') 