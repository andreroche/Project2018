# André Roche 12-Apr-18. This is a test using code taken from various pages at Stack Overflow. I am not the author of this.
# This is a test to see if Pandas is functioning and graphical output works on this PC.

import pandas

from pandas import scatter_matrix
import matplotlib.pyplot as plt



dataset = pandas.read_csv('data/iris_dataset.csv', header = None,
names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])


dataset.describe() #to give a statistical summary about the dataset
print(dataset.describe())
dataset.skew()
dataset.kurtosis()
print(dataset.skew())
print(dataset.kurtosis())

# box and whisker plots
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()

# histograms
dataset.hist()
plt.show()

# scatter plot matrix
scatter_matrix(dataset)
plt.show()