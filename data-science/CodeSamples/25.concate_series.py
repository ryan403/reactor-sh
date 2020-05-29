import numpy as np
import pandas as pd
series1=pd.Series({'王明':90,'柳宇':40,'張三':70})
series2=pd.Series({'范武':60,'陳實':30,'張揚':90})
series3=pd.concat([series1,series2])
series3
