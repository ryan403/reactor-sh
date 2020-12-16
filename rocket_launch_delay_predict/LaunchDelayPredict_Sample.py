#---import modules ----------------------------------

# Pandas library is used for handling tabular data
import pandas as pd
# NumPy is used for handling numerical series operations (addition, multiplication, and ...)
import numpy as np
# Sklearn library contains all the machine learning packages we need to digest and extract patterns from the data
from sklearn import linear_model, model_selection, metrics
from sklearn.metrics.classification import accuracy_score
from sklearn.model_selection import train_test_split

# Machine learning libraries used to build a decision tree
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

# Sklearn's preprocessing library is used for processing and cleaning the data 
from sklearn import preprocessing

# for visualizing the tree
import pydotplus
from IPython.display import Image

#---import dataset ----------------------------------

launch_data = pd.read_excel('RocketLaunchDataCompleted.xlsx')
launch_data.head()
launch_data.columns

#---deal with missing values ----------------------------------

launch_data.info()
launch_data.isnull().sum()

launch_data['Launched?'].value_counts()
launch_data['Launched?'].fillna('N',inplace=True)
launch_data['Launched?'].value_counts()

launch_data['Crewed or Uncrewed'].value_counts()
launch_data['Crewed or Uncrewed'].fillna('Uncrewed', inplace=True)
launch_data['Crewed or Uncrewed'].value_counts()

launch_data['Wind Direction'].value_counts()
launch_data['Wind Direction'].isnull().sum()
launch_data['Wind Direction'].fillna('unknown', inplace=True)

launch_data['Condition'].value_counts()
launch_data['Condition'].isnull().sum()
launch_data['Condition'].fillna('Fair',inplace=True)

launch_data.isnull().sum()
launch_data.fillna(0, inplace=True)


#---data transformation ----------------------------------

launch_data.info()
## As part of the data cleaning process, we have to convert text data to numerical because computers understand only numbers
label_encoder = preprocessing.LabelEncoder()
# Three columns have categorical text info, and we convert them to numbers
launch_data['Crewed or Uncrewed'].value_counts()
launch_data['Wind Direction'].value_counts()
launch_data['Condition'].value_counts()

launch_data['Crewed or Uncrewed'] = label_encoder.fit_transform(launch_data['Crewed or Uncrewed'])
launch_data['Wind Direction'] = label_encoder.fit_transform(launch_data['Wind Direction'])
launch_data['Condition'] = label_encoder.fit_transform(launch_data['Condition'])

#---ml model training ----------------------------------

# First, we save the output we are interested in. In this case, "launch" yes and no's go into the output variable.
y = launch_data['Launched?']
# Removing the columns we are not interested in
X = launch_data.drop(['Name','Date','Time (East Coast)','Location','Launched?','Hist Ave Sea Level Pressure','Sea Level Pressure','Day Length','Notes','Hist Ave Visibility', 'Hist Ave Max Wind Speed'],axis=1)
X.info()

tree_model = DecisionTreeClassifier(random_state=0, max_depth=5)

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=99)

tree_model.fit(X_train, y_train)


#---ml model using & prediction ------------------------

y_pred = tree_model.predict(X_test)
y_pred

tree_model.score(X_test, y_test)

# is equal to 
from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_pred)


#--- model visualization ----------------------------------

# Let's import a library for visualizing our decision tree.
from sklearn.tree import export_graphviz

def tree_graph_to_png(tree, feature_names, class_names):
    tree_str = export_graphviz(tree, feature_names=feature_names, class_names=class_names, filled=True, out_file=None)
    graph = pydotplus.graph_from_dot_data(tree_str)
    return Image(graph.create_png())

tree_graph_to_png(tree=tree_model, feature_names=X.columns.values, class_names=['No Launch','Launch'])


#--- model inference ----------------------------------

# ['Crewed or Uncrewed', 'High Temp', 'Low Temp', 'Ave Temp',
#        'Temp at Launch Time', 'Hist High Temp', 'Hist Low Temp',
#        'Hist Ave Temp', 'Precipitation at Launch Time',
#        'Hist Ave Precipitation', 'Wind Direction', 'Max Wind Speed',
#        'Visibility', 'Wind Speed at Launch Time', 'Condition']

data_input = [ 1.  , 75.  , 68.  , 71.  ,  0.  , 75.  , 55.  , 65.  ,  0.  , 0.08,  0.  , 16.  , 15.  ,  0.  ,  0. ]

tree_model.predict([data_input])