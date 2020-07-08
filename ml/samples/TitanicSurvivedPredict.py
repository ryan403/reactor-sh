#import modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn as sns

#import dataset

df = pd.read_csv("data/train_data_titanic.csv")
df.head()
df.info()

#Remove the columns model will not use
df.drop(['Name','Ticket'],axis=1,inplace=True)
df.head()

sns.pairplot(df[['Survived','Fare']], dropna=True)

#data observing
df.groupby('Survived').mean()
df.head()
df['SibSp'].value_counts()
df['Parch'].value_counts()
df['Sex'].value_counts()

df.info()
#Handle missing values
df.isnull().sum()>(len(df)/2)
#Cabin has too many missing values
df.drop('Cabin',axis=1,inplace=True)
df.head()
df['Age'].isnull().value_counts()

#Age is also have some missing values
df.groupby('Sex')['Age'].median().plot(kind='bar')

#缺失值男生就用男生的平均、女生就用女生的平均值來填補
df['Age'] = df.groupby('Sex')['Age'].apply(lambda x: x.fillna(x.median()))

df.isnull().sum()
#發現還有Embarked還有缺2個
df['Embarked'].value_counts()
#找出第一個次數最多的，發現是S
df['Embarked'].value_counts().idxmax()
df['Embarked'].fillna(df['Embarked'].value_counts().idxmax(),inplace=True)
df['Embarked'].value_counts()
#所有缺失值搞定!
df.isnull().sum()

#將Sex, Embarked進行轉換
#Sex轉換成是否為男生、是否為女生，Embarked轉換為是否為S、是否為C、是否為Q
df = pd.get_dummies(data=df, columns=['Sex','Embarked'])
df.head()
#是否為男生與是否為女生只要留一個就好，留下是否為男生
df.drop(['Sex_female'], axis=1, inplace=True)
df.head()

df.corr()
#Preare training data
#把Survived, Pclass丟掉
X = df.drop(['Survived','Pclass'],axis=1)
y = df['Survived']

#split to training data & testing data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=67)

#using Logistic regression model
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(X_train, y_train)
predictions = lr.predict(X_test)

#Evaluate
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
#support是個別tag的真實個數
print(classification_report(y_test,predictions))
print(accuracy_score(y_test, predictions))
print(confusion_matrix(y_test, predictions))
pd.DataFrame(confusion_matrix(y_test, predictions), columns=['True Survived', 'True not Survived'], index=['Predict Survived','Predict  not Survived'])
