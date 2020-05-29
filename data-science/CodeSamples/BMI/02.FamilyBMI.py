
family_data = [
    ['Dad',178,72],
    ['Mom',155,44],
    ['Kid',117,19]
]

for each_one in family_data:
    this_bmi = each_one[2] / ((each_one[1]/100) **2)
    each_one.append(this_bmi)

for each_one in family_data:
    if each_one[3] <18.5:
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

for each_one in family_data:
    if each_one[4] == '正常範圍':
        is_normal = True
    else:
        is_normal = False
    each_one.append(is_normal)

for each_one in family_data[0]:
    print(type(each_one))

family_data[0:2]
family_data[:2]
family_data[1:]
family_data

import numpy as np
family_name_array = np.array([family_data[0][0],family_data[1][0],family_data[2][0]])
family_height_array = np.array([family_data[0][1],family_data[1][1],family_data[2][1]])
family_weight_array = np.array([family_data[0][2],family_data[1][2],family_data[2][2]])
family_bmi_array = np.array([family_data[0][3],family_data[1][3],family_data[2][3]])
family_bmi_index_array = np.array([family_data[0][4],family_data[1][4],family_data[2][4]])
np.mean(family_height_array)
np.median(family_weight_array)
np.corrcoef(family_weight_array, family_bmi_array)[1,0]

import matplotlib.pyplot as plt
#%matplotlib inline 有執行過即可
plt.scatter(family_height_array, family_weight_array)
plt.xlabel('Height')
plt.ylabel('Weight')
plt.title('Numbers in family')
plt.show()

import pandas as pd
kid_bmi_standard_english = pd.read_csv('bmirecommendation-English.csv')
kid_bmi_standard_english.head()

family_gender_array = np.array(['Male', 'Female', 'Female'])
family_age_array = np.array([38, 37, 6])

for this_index, each_age in enumerate(family_age_array):
    if each_age < 18:
        #找到是第幾個
        print('第'+str(this_index)+'個的年齡是'+str(each_age)+'小於18歲')
        #只取該年紀的列
        only_this_age = kid_bmi_standard_english['Age']==each_age
        this_bmi_standard = kid_bmi_standard_english[only_this_age]
        #找到該性別的欄位
        compare_gender_index = [(family_gender_array[this_index]+" Fat if Higher"), 
        (family_gender_array[this_index]+" Over Weight if Higher"), 
        ('Normal '+family_gender_array[this_index]+" Should Between")]
        
        #開始進行比對
        if family_bmi_array[this_index] > float(this_bmi_standard[compare_gender_index[0]]):
            family_bmi_index_array[this_index] = '肥胖'
        elif family_bmi_array[this_index] > float(this_bmi_standard[compare_gender_index[1]]):
            family_bmi_index_array[this_index] = '體重過重'
        elif family_bmi_array[this_index] > float(this_bmi_standard[compare_gender_index[2]].values[0][:4]):
            family_bmi_index_array[this_index] = '正常範圍'
        else:
            family_bmi_index_array[this_index] = '體重過輕'

family_bmi_index_array

family_data_frame = pd.DataFrame(data=family_bmi_index_array, 
                                 index= family_name_array, 
                                 columns = ['BMI指標'])
family_data_frame['年齡'] = family_age_array
family_data_frame
