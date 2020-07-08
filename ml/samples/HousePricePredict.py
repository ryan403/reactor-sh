#import modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn as sns

#import dataset

df = pd.read_csv("data/Housing_Dataset_Sample.csv")

#observing dataset
df.head()
df.describe().T
df.isnull().sum()
sns.distplot(df['Price'])
sns.jointplot(df['Avg. Area Income'],df['Price'])

#prepare to train model
#x是所有可能的影響變因
#取得所有的列的0,1,2,3,4欄位
X = df.iloc[:,:5]
#y是目標值
y = df['Price']

#split to training data & testing data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=54)

#using linear regression model
from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(X_train, y_train)

#get the result
predictions = reg.predict(X_test)
predictions

from sklearn.metrics import r2_score
r2_score(y_test, predictions)
plt.scatter(y_test, predictions, color='blue')