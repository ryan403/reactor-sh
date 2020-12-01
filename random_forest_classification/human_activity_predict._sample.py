#------ import modules ---------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.linear_model import LogisticRegression, LogisticRegressionCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_fscore_support as error_metric
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, f1_score,recall_score
from sklearn.feature_selection import VarianceThreshold

#---- read data set files ------------
train = pd.read_csv("Data/train.csv")
test = pd.read_csv("Data/test.csv")

#---- data observation ---------------
train.head()

train.isnull().sum()
test.isnull().sum()
train.isnull().values.any()
test.isnull().values.any()

train.info()
test.info()

#---- remove un-related columns ----------

train.drop('subject',axis=1, inplace=True)
test.drop('subject',axis=1, inplace=True)

rem_cols2 = train.columns.tolist()

train.describe()

is_object_type_feature = train.dtypes == np.object
train.columns[is_object_type_feature]

train['Activity'].value_counts()
train.Activity.value_counts()

#---- transform to numeric values -------

le = LabelEncoder()
for x in [train, test]:
    x['Activity'] = le.fit_transform(x['Activity'])

#---- find correlation -----------------
corr_val = train.corr()
corr_val_activity_abs = corr_val['Activity'].abs()
corr_val_activity_abs_sort = corr_val_activity_abs.sort_values(ascending=False)
corr_val_activity_abs_sort[corr_val_activity_abs_sort>0.84]


#---- ready for train & test -----------

feature_cols = train.columns[:-1]
split_data = StratifiedShuffleSplit(n_splits=3, test_size=0.3, random_state=42)
train_idx, val_idx = next(split_data.split(train[feature_cols],train.Activity))

X_train = train.loc[train_idx, feature_cols]
y_train = train.loc[train_idx, 'Activity']

X_val = train.loc[val_idx, feature_cols]
y_val = train.loc[val_idx, 'Activity']

y_train.value_counts()
y_train.value_counts(normalize=True)
y_val.value_counts(normalize=True)

#---- Compare few models -------------

lr = LogisticRegression()
lr_l2 = LogisticRegressionCV()
rf = RandomForestClassifier()

lr_model = lr.fit(X_train, y_train)
lr_l2_model = lr_l2.fit(X_train, y_train)
rf_model = rf.fit(X_train, y_train)

lr_model_predict = lr_model.predict(X_val)
lr_l2_model_predict = lr_l2_model.predict(X_val)
rf_model_predict = rf_model.predict(X_val)

three_model_predict_df = pd.DataFrame({'lr':lr_model_predict,'lr_l2':lr_l2_model_predict,'rf':rf_model_predict})


lr_model_proba = lr_model.predict_proba(X_val).max(axis=1)
lr_l2_model_proba = lr_l2_model.predict_proba(X_val).max(axis=1)
rf_model_proba = rf_model.predict_proba(X_val).max(axis=1)

three_model_proba_df = pd.DataFrame({'lr':lr_model_proba,'lr_l2':lr_l2_model_proba,'rf':rf_model_proba})

#---- Compare results--------------------

accurcy_lr = accuracy_score(y_val, lr_model_predict)
accurcy_lr_l2 = accuracy_score(y_val, lr_l2_model_predict)
accurcy_rf = accuracy_score(y_val, rf_model_predict)

three_model_report = pd.DataFrame(data={'Accuracy':[accurcy_lr,accurcy_lr_l2,accurcy_rf]},index=['lr','lr_l2','rf'])

#---- Compare other matrics ------------

precision_lr = precision_score(y_val, lr_model_predict, average='weighted')
precision_lr_l2 = precision_score(y_val, lr_l2_model_predict, average='weighted')
precision_rf = precision_score(y_val, rf_model_predict, average='weighted')

three_model_report['Precision'] = [precision_lr,precision_lr_l2,precision_rf]

recall_lr = recall_score(y_val, lr_model_predict, average='weighted')
recall_lr_l2 = recall_score(y_val, lr_l2_model_predict, average='weighted')
recall_rf = recall_score(y_val, rf_model_predict, average='weighted')

three_model_report['Recall'] = [recall_lr,recall_lr_l2,recall_rf]

f1score_lr = f1_score(y_val, lr_model_predict, average='weighted')
f1score_lr_l2 = f1_score(y_val, lr_l2_model_predict, average='weighted')
f1score_rf = f1_score(y_val, rf_model_predict, average='weighted')

three_model_report['F1 Score'] = [f1score_lr,f1score_lr_l2,f1score_rf]

cm_lr = confusion_matrix(y_val, lr_model_predict)
cm_lr_l2 = confusion_matrix(y_val, lr_l2_model_predict)
cm_rf = confusion_matrix(y_val, rf_model_predict)

sns.heatmap(cm_lr,annot=True,fmt="d")
sns.heatmap(cm_lr_l2, annot=True, fmt="d")
sns.heatmap(cm_rf, annot=True, fmt="d")