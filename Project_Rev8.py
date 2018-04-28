# André Roche - 23-Apr-18. Importing Pandas. Iris dataset testing for project 2018.

#using pandas to import and print the Iris Dataset on-screen.
import pandas as pd
from pandas import scatter_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats


from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

from scipy.stats import skew, kurtosis, normaltest


df=pd.read_csv('data/iris_dataset.csv', header = None,
names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])

print (df.corr())







