import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn as sns

#Importing & Observing dataset

df = pd.read_csv("Housing_Dataset_Sample.csv")

df.head()
df.describe().T
df.info()
df.shape

sns.distplot(df['Price'])
sns.jointplot(df['Avg. Area Income'],df['Price'])

sns.pairplot(df)

#Prepare for model

X = df.iloc[:,:5]
y = df['Price']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 54)

#Choose ML model

from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(X_train, y_train)

predictions = reg.predict(X_test)
predictions

from sklearn.metrics import r2_score
r2_score(y_test, predictions)
plt.scatter(y_test, predictions, color='blue', alpha=0.1)