# André Roche - 23-Apr-18. Importing Pandas. Iris dataset testing for project 2018.

#using pandas to import and print the Iris Dataset on-screen.
import pandas as pd
import seaborn as sns
df = sns.load_dataset('iris')
df.groupby('species').mean()
df.groupby('species').std()
df.groupby('species').median()
df.groupby('species').max()
df.groupby('species').min()

#df=pd.read_csv('data/iris_dataset.csv', header = None,
#names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])

print(df.groupby('species').mean()) # 'groupby species' learned from www.stackoverflow.com 
print('')
print(df.groupby('species').std())
print('')
print(df.groupby('species').median())
print('')
print(df.groupby('species').max())
print('')
print(df.groupby('species').min())













 