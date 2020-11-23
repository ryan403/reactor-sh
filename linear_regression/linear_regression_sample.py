#--------------import modules---------------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from sklearn import metrics
from sklearn.metrics import r2_score

from sklearn.datasets import load_iris
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
from sklearn.decomposition import PCA

#----------------------------------------------------

mammals = pd.read_csv('Data/mammals.csv')
mammals.head()

mammals.plot.scatter(x='body',y='brain')

mammals[mammals['brain']>1000]

#loglog: both x and y take log
mammals.plot.scatter(x='body',y='brain',loglog=True)

mammals['body_log'] = np.log(mammals['body'])
mammals['brain_log'] = np.log(mammals['brain'])

#------ Linear Regression --------------------------

X = mammals[['body_log']]
y = mammals['brain_log']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state = 0)

reg = LinearRegression()

reg.fit(X_train, y_train)

r2_score(y_test, reg.predict(X_test))

plt.scatter(y_test, reg.predict(X_test))
plt.plot(y_test, y_test, color='red')

#------Project 2----------------------------------

lynx = pd.read_csv('Data/lynx.csv')
lynx.head()
lynx.info()
lynx.describe()

lynx.plot(x='Year',y='Lynx')

X_lynx = lynx[['Year']]
y_lynx = lynx['Lynx']

X_lynx_train, X_lynx_test, y_lynx_train, y_lynx_test = train_test_split(X_lynx, y_lynx, test_size = 0.3, random_state=0)

lr = LinearRegression()
lr.fit(X_lynx_train, y_lynx_train)

r2_score(y_lynx_test, lr.predict(X_lynx_test))

#-----------Project 3---------------------------------

iris = load_iris()
iris
iris_df = pd.DataFrame(data = np.c_[iris['data'],iris['target']], columns = iris['feature_names']+['class'])

iris_df.info()
iris_df.head()
iris_df.describe()

#------Try KMeans------------------------------------

X_iris = iris_df[['sepal length (cm)','sepal width (cm)','petal length (cm)','petal width (cm)']]
y_iris = iris_df['class']

X_iris_train, X_iris_test, y_iris_train, y_iris_test = train_test_split(X_iris, y_iris, test_size = 0.3, random_state=0)

this_KMeans = KMeans(n_clusters=3, random_state=0)
this_km = this_KMeans.fit(X_iris_train)
y_pred = this_km.predict(X_iris_test)

metrics.accuracy_score(y_iris_test,y_pred)

#-----Try KNC---------------------------------------

X_iris_train, X_iris_test, y_iris_train, y_iris_test = train_test_split(X_iris, y_iris, test_size = 0.3, random_state=0)

this_KNC = KNeighborsClassifier(n_neighbors=5)
this_KNC_model = this_KNC.fit(X_iris_train, y_iris_train)
y_knc_pred = this_KNC_model.predict(X_iris_test)

metrics.accuracy_score(y_iris_test,y_knc_pred)

#------Cross Validation----------------------------

scores = cross_val_score(this_KNC_model,X_iris, y_iris, cv=10, scoring='accuracy')
scores.mean()

#------Find the best n_neighbors ------------------

k_range = list(range(1,26))
k_dict = {}
for k in k_range:
    this_KNC = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(this_KNC,X_iris, y_iris, cv=10, scoring='accuracy')
    k_dict[k] = scores.mean()

scores_max = max(k_dict, key=k_dict.get)
print(scores_max, k_dict[scores_max])

#-----PCA, 3D Visualization---------------------------------

X_iris_reduced = PCA(n_components=3).fit_transform(X_iris)

fig = plt.figure(1, figsize=(8,6))
ax = Axes3D(fig, elev=-150, azim=110)
ax.scatter(X_iris_reduced[:, 0],X_iris_reduced[:,1],X_iris_reduced[:,2],c=y_iris, cmap='viridis',edgecolors='k',s=40)