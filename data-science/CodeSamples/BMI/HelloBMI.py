'''
height = 1.78
weight = 73.7
bmi = weight / height **2
print('你的BMI值為'+'%.2f' %bmi)
if bmi < 18.5:
    print('體重過輕')
elif 18.5 <= bmi < 24.0:
    print('正常範圍')
elif 24.0 <= bmi < 27.0:
    print('體重過重')
elif 27.0 <= bmi < 30.0:
    print('輕度肥胖')
elif 30.0 <= bmi < 35.0:
    print('中度肥胖')
else:
    print('重度肥胖')
'''

family_data = [
    ['Dad',178,72],
    ['Mom',155,44],
    ['Kid',117,19]
]

for each_one in family_data:
    this_bmi = each_one[2] / ((each_one[1]/100)**2)
    each_one.append(this_bmi)

family_data

for each_one in family_data:
    if each_one[3] < 18.5:
        bmi_index = '體重過輕'
    elif 18.5 <= each_one[3] < 24.0:
        bmi_index = '正常範圍'
    elif 24.0 <= each_one[3] < 27.0:
        bmi_index = '體重過重'
    elif 27.0 <= each_one[3] < 30.0:
        bmi_index = '輕度肥胖'
    elif 30.0 <= each_one[3] < 35.0:
        bmi_index = '中度肥胖'
    else:
        bmi_index = '重度肥胖'
    each_one.append(bmi_index)

family_data

for each_one in family_data:
    if each_one[4] == "正常範圍":
        is_normal = True
    else:
        is_normal = False
    each_one.append(is_normal)

family_data

for each_one in family_data[0]:
    print(type(each_one))

family_data[1:]

import numpy as np

family_name_array = np.array([family_data[0][0],family_data[1][0],family_data[2][0]])
family_height_array = np.array([family_data[0][1],family_data[1][1],family_data[2][1]])
family_weight_array = np.array([family_data[0][2],family_data[1][2],family_data[2][2]])
family_bmi_array = np.array([family_data[0][3],family_data[1][3],family_data[2][3]])
family_bmi_index_array = np.array([family_data[0][4],family_data[1][4],family_data[2][4]])

family_name_array

np.mean(family_height_array)
np.median(family_weight_array)
np.corrcoef(family_weight_array, family_bmi_array)[1,0]

import matplotlib.pyplot as plt
#%matplotlib inline
plt.scatter(family_height_array, family_weight_array)
plt.xlabel('Height')
plt.ylabel('Weight')
plt.title('Numbers in family')
plt.show()

#月份:1~12
month_array = np.arange(1,13)
#產生12筆資料，隨機在75.5~80.0之間
dad_weight_history_array = []
for i in range(0,12):
    #指定範圍、到小數點後幾位數
    x = round(np.random.uniform(75.5, 80.0),2)
    dad_weight_history_array.append(x)

plt.scatter(month_array, dad_weight_history_array)
plt.plot(month_array, dad_weight_history_array)
plt.fill_between(month_array, dad_weight_history_array, 74, color='pink')
plt.xticks(month_array)
plt.yticks(np.arange(74,81,2))

plt.xlabel('Month at 2019')
plt.ylabel('Weight in KG')
plt.title("Dad's weight @ 2019 ")

import pandas as pd
kid_bmi_standard_english = pd.read_csv('bmirecommendation-English.csv')
kid_bmi_standard_english.head()

family_gender_array = np.array(['Male','Female','Female'])
family_age_array = np.array([38,37,6])

for this_index, each_age in enumerate(family_age_array):
    if each_age < 18:
        #看看是第幾個未滿18歲
        print('第'+str(this_index)+'個的年齡是'+str(each_age)+'小於18歲')
        #找出比對資料的該年齡那一列
        only_this_age = kid_bmi_standard_english['Age']==each_age
        this_bmi_standard = kid_bmi_standard_english[only_this_age]
        #取得這一個未滿18歲孩子的性別
        this_gender = family_gender_array[this_index]
        #只取出該性別的那三項指標(會從Normal Male/Female Should Between開始)
        this_bmi_standard_gender = this_bmi_standard.loc[:,'Normal '+this_gender+' Should Between':this_gender+" Fat if Higher"]
        #開始跟篩選過的DataFrame進行比對
        
        if family_bmi_array[this_index]>float(this_bmi_standard_gender.iloc[0,2]): 
            family_bmi_index_array[this_index] = '肥胖' #Fat if Higher
        elif family_bmi_array[this_index]>float(this_bmi_standard_gender.iloc[0,1]):
            family_bmi_index_array[this_index] = '體重過重' #Over Weight if Higher
        elif family_bmi_array[this_index]>float(this_bmi_standard_gender.iloc[0,0][:4]):
            family_bmi_index_array[this_index] = '正常範圍' #Normal Should Between
        else:                                              #取出xx.x-xx.x中的前4字元
            family_bmi_index_array[this_index] = '體重過輕'

family_bmi_index_array