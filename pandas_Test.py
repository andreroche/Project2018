# André Roche 12-Apr-18. This is a test using code taken from various pages at Stack Overflow. I am not the author of this.
# This is a test to see if Pandas is functioning and graphical output works on this PC.

import pandas

from pandas import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


dataset = pandas.read_csv('data/iris_dataset.csv')

dataset.head() #to check the first 10 rows of the data set
dataset.tail() #to check out last 10 row of the data set
dataset.describe() #to give a statistical summary about the dataset



# box and whisker plots
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()

# histograms
dataset.hist()
plt.show()

# scatter plot matrix
scatter_matrix(dataset)
plt.show()