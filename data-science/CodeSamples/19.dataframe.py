import pandas as pd
population_dict = {
    'France':65429495,
    'Germany':82408706,
    'Russia':143910127,
    'Japan':126922333,
    'Italy':12345678
}
population = pd.Series(population_dict)
area_dict = {
    'France':643801,
    'Germany':357386,
    'Russia':17125200,
    'Japan':377972
}
area = pd.Series(area_dict)

countries = pd.DataFrame({'Area':area,'Population':population})
print(countries)
print(countries['Area'])
print(countries.iloc[:4,:2]) # 列,欄
print(countries.loc[:'Germany',:'Population']) #印到指定國家、指定欄位
