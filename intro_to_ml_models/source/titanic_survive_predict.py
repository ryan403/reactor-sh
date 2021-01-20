import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn as sns
from sklearn.metrics.classification import recall_score

#Importing & Observing dataset
df = pd.read_csv("train_data_titanic.csv")
df.head()
df.info()

df.drop(['Name','Ticket'], axis=1, inplace=True)
df.head()

sns.pairplot(df[['Survived','Age']],dropna=True)
sns.pairplot(df[['Survived','Pclass']],dropna=True)
sns.pairplot(df[['Survived','Fare']],dropna=True)
sns.pairplot(df[['Survived','SibSp']],dropna=True)
sns.pairplot(df[['Survived','Parch']],dropna=True)

df.groupby('Survived').mean()

df.head()

df['SibSp'].value_counts()
df['Parch'].value_counts()
df['Sex'].value_counts()

#Dealing with missing values

df.isnull().sum()
len(df)
len(df)/2
df.isnull().sum()>(len(df)/2)

df.drop('Cabin',axis=1, inplace=True)
df.head()
df['Age'].isnull().sum()
df['Age'].isnull().value_counts()
df.info()
df['Age'].value_counts()
df.groupby('Sex')['Age'].median()

df['Age'] = df.groupby('Sex')['Age'].apply(lambda x:x.fillna(x.median()))

df.isnull().sum()
df['Embarked'].value_counts()
df.info()

df['Embarked'].value_counts().idxmax()
df['Embarked'].fillna(df['Embarked'].value_counts().idxmax(),inplace=True)
df['Embarked'].value_counts()

df.isnull().sum()

#Transforming data types

df = pd.get_dummies(data=df, columns=['Sex','Embarked'])
df.drop(['Sex_female'],axis=1,inplace=True)


#Prepare for model

df.corr()

X = df.drop(['Survived','Pclass'],axis=1)
y = df['Survived']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state = 67)

#Choose ML model 1

from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()

lr.fit(X_train, y_train)
predictions = lr.predict(X_test)

from sklearn.metrics import confusion_matrix, accuracy_score, recall_score, precision_score

accuracy_score(y_test, predictions)
recall_score(y_test, predictions)
precision_score(y_test, predictions)

pd.DataFrame(confusion_matrix(y_test,predictions), columns=['Predict not Survived','Predict Survived'],index=['True not Survived','True Survived'])

#Choose ML model 2

from sklearn import tree
tr = tree.DecisionTreeClassifier(random_state=0, max_depth=5)
tr.fit(X_train, y_train)
tr_predictions = tr.predict(X_test)

accuracy_score(y_test, tr_predictions)
recall_score(y_test, tr_predictions)
precision_score(y_test, tr_predictions)

pd.DataFrame(confusion_matrix(y_test,tr_predictions), columns=['Predict not Survived','Predict Survived'],index=['True not Survived','True Survived'])

import graphviz

dot_file = tree.export_graphviz(tr, out_file=None, feature_names=X.columns, class_names=['Not Survived','Survived'], filled=True, rounded=False)

graph = graphviz.Source(dot_file)
graph