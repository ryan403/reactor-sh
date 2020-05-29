import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
#產生月份數字 [1,2,3,4,5,6,7,8,9,10,11,12]
month_array = np.arange(1,13)
dad_weight_history_array = np.array([76.4, 75.8, 77.3, 77.2, 77.3, 77.5,
                                     77.8, 77.7, 78.4, 78.0, 78.2, 80.0])
#畫出點
plt.scatter(month_array, dad_weight_history_array)
#畫出折線
plt.plot(month_array, dad_weight_history_array)
#塗上顏色
plt.fill_between(month_array, dad_weight_history_array, 74, color='pink')
#決定X軸每個月份都顯示, y軸只顯示四個數字
plt.xticks(month_array)
plt.yticks([74, 76, 78, 80])
#加上x軸標題、y軸標題、大標題
plt.xlabel('Month at 2019')
plt.ylabel('Weight in KG')
plt.title("Dad's Weight @ 2019")
#顯示圖表-非互動模式才需要
plt.show()
