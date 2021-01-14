import numpy as np
import pandas as pd

df = pd.read_csv('housing_dataset.csv')

df.head()
df.info()
df.describe().T
df.shape

df['MEDV'].mean()
df['MEDV'].max()
df['AGE'].median()
df['AGE'].count()

df.groupby(['AGE'])['MEDV'].mean()

#practice

df['AGE_50'] = df['AGE'].apply(lambda x: x>50)

df['AGE_50'].value_counts()

df.groupby(['AGE_50'])['MEDV'].mean()

groupby_three = df.groupby(['AGE_50','RAD','CHAS'])['MEDV'].mean()

groupby_three.unstack(-2)

#==Data Visualization=========

df['CHAS'].unique()
df['CHAS'].value_counts()
#%matplotlib inline
df['CHAS'].value_counts().plot(kind='bar')

corr = df.corr(method='pearson')
corr_with_homevalue = corr.iloc[-2]
corr_with_homevalue.sort_values(ascending=False)

import seaborn as sns
sns.heatmap(df.corr(),cmap=sns.cubehelix_palette(n_colors=20,light=0.95,dark=0.15))

import matplotlib.pyplot as plt
plt.hist(df['MEDV'],bins=50)

sns.distplot(df['MEDV'])

sns.pairplot(df[['RM','AGE','LSTAT','DIS','MEDV']],kind='reg',plot_kws={'line_kws':{'color':'red'},'scatter_kws':{'alpha':0.1}})