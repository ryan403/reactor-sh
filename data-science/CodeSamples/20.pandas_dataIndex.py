import pandas as pd
numberList = [-0.5, 0.75, 1.0, -2]
series_example = pd.Series(numberList, index = ['a','b','c','d'])
ind = series_example.index
print(series_example['b'])
print(series_example[0:2])
