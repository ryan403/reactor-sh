import numpy as np
import pandas as pd
from sklearn import datasets
iris = datasets.load_iris()
iris_df = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                     columns= iris['feature_names'] + ['class'])
iris_df.head()
iris_df.tail()
iris_df.info()
iris_df.shape
iris_df['sepal length (cm)'].mean()