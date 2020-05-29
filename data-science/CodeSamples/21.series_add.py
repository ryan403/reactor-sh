import pandas as pd
series1 = pd.Series([25,10,50],index=[0,1,2])
series2 = pd.Series([5,70,40],index=[1,2,3])
series3 = series1 + series2
series3_good = series1.add(series2, fill_value=0)
