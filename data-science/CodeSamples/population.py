import numpy as np
import pandas as pd
population_dict = {
    'France':65429495,
    'Germany':82408706,
    'Russia':143910127,
    'Japan':126922333
}
population = pd.Series(population_dict)
population
population.index
#取出國家名稱index進行排序
country_name_sorted = np.sort(population.index)
country_name_sorted
#搭配已經排序好的國家名稱來建立Series
population_sorted = pd.Series(population_dict,country_name_sorted) 
population_sorted
#照人口數來進行排序
population_sorted.sort_values(ascending=False)

#幫Series加上name屬性
population_sorted.name = 'Population'
#幫Series的index加上name屬性
population_sorted.index.name = 'Country Name'

area_dict = {
    'France':643801,
    'Germany':357386,
    'Russia':17125200,
    'Japan':377972
}
area = pd.Series(area_dict)

countries = pd.DataFrame({'Area':area,'Population':population_sorted})
countries


iso_code_dict = {
    'France':'FR',
    'Germany':'DE',
    'Russia':'RU',
}
iso_code = pd.Series(iso_code_dict)

countries['ISO Code']=iso_code
countries

countries['Area']

countries.iloc[:3,:2]

countries.loc[:'Russia',:'Population']

countries['many_people'] = countries.Population >= 100000000

del countries['many_people']