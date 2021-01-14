import numpy as np
import pandas as pd
from sklearn import datasets

#==== iris dataset observation ======

iris = datasets.load_iris()

iris_df = pd.DataFrame(data=np.c_[iris['data'],iris['target']],columns=iris['feature_names']+['class'])

iris_df.head()
iris_df.tail()
iris_df.info()
iris_df.shape
iris_df['sepal length (cm)'].mean()

#==== deal with missing values ======
import numpy as np
example1 = np.array([2,None,6,8])
example1.sum()
example2 = np.array([2,np.nan,6,8])
example2.sum()


import numpy as np
import pandas as pd
example3 = pd.Series([0,np.nan,'',None])

import numpy as np
import pandas as pd
example4 = pd.DataFrame([[1,np.nan,7],[2,5,8],[np.nan,6,9]])
example4[3] = np.nan
example4.dropna(axis='rows',thresh=3)


example5 = pd.Series([1,np.nan,2,None,3],index=list('abcde'))
example5

example5.fillna(0)

example5.fillna(method='ffill')
example5.fillna(method='bfill')

example4
example4 = example4.fillna(method='ffill')
example4 = example4.fillna(method='ffill',axis=1)


#=== Deal with duplicates==

df5 = pd.DataFrame({'ColA':[1,np.nan,np.nan,4,5,6,7],'ColB':[1,1,1,1,2,2,2]})
df5
df5.fillna(value=df5.mean())

import numpy as np
import pandas as pd
example6 = pd.DataFrame({'letters':['A','B']*2 + ['B'],'numbers':[1,2,1,3,3]})
example6

example6.duplicated()

example6.drop_duplicates()

example6.drop_duplicates(['letters'])
example6.drop_duplicates(['numbers'])

#== Concatenate ==========

import numpy as np
array_one = np.array([1,2,3])
array_two = np.array([4,5,6])
array_concate = np.concatenate([array_one,array_two])
array_concate
array_stack = np.array([array_one,array_two])
array_stack

import numpy as np
import pandas as pd
df0a = pd.DataFrame({'employee':['Gary','Stu'],'group':['Accounting','Marketing']})
df0b = pd.DataFrame({'employee':['Mary','Sue'],'group':['Marketing','HR']})
df1 = df0a.append(df0b,ignore_index=True)
df1 = pd.concat([df0a,df0b],ignore_index=True)
df1

import numpy as np
import pandas as pd
df1 = pd.DataFrame({'employee':['Gary','Stu','Mary','Sue'],'group':['Accounting','Marketing','Marketing','HR']})
df1
df2 = pd.DataFrame({'employee':['Gary','Stu','Mary','Sue'],'hire_date':[2008,2012,2017,2018]})
df2
df3 = pd.merge(df1,df2)
df3

df4 = pd.DataFrame({'group':['Accounting','Marketing','HR'],'supervisor':['Carlos','Giada','Stephanie']})
df4
pd.merge(df3,df4,on='group')

df5 = pd.DataFrame({'group':['Accounting','Accounting','Marketing','Marketing','HR','HR'],'core_skills':['math','spreadsheets','writing','communication','spreadsheets','organization']})
df1
df5
pd.merge(df1,df5,on='group')

df6 = pd.DataFrame({'name':['Gary','Stu','Mary','Sue'],'salary':[70000,80000,120000,90000]})
df6
df1
df7 = pd.merge(df1,df6,left_on='employee',right_on='name')
df7
df7.drop('name',axis=1,inplace=True)

df1
df1a = df1.set_index('employee')
df1a
df2a = df2.set_index('employee')
df2a

pd.merge(df1a,df2a,left_index=True,right_index=True)


df1a
df6
df7 = pd.merge(df1a,df6,left_index=True,right_on='name')
df7 = df7.set_index('name')
df7.index.name = 'employee'
df7

df1
df5 = pd.DataFrame({'group':['Engineering','Marketing','Sales'],'core_skills':['math','writing','communication']})
df5
pd.merge(df1,df5,on='group',how='inner')
pd.merge(df1,df5,on='group',how='outer')
pd.merge(df1,df5,how='left')
pd.merge(df1,df5,how='right')

df_rank1 = pd.DataFrame({'name':['Gary','Stu','Mary','Sue'],'rank':[1,2,3,4]})
df_rank2 = pd.DataFrame({'name':['Gary','Stu','Mary','Sue'],'rank':[3,1,4,2]})
df_rank1
df_rank2
pd.merge(df_rank1,df_rank2,on='name')
pd.merge(df_rank1,df_rank2,on='name', suffixes=['_A','_B'])


import numpy as np
import pandas as pd
df10 = pd.DataFrame({'A':['a','d'],'B':['b','e'],'C':['c','f']})
df11 = pd.DataFrame({'B':['u','x'],'C':['v','y'],'D':['w','z']})

df10
df11

pd.concat([df10,df11])
pd.concat([df10,df11],join='inner')