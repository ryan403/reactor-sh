height = 1.78
weight = 72.0
bmi = weight / height **2
print('你的BMI值為'+"%.2f" % bmi)
if bmi <18.5:
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
