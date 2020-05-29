import numpy as np
import pandas as pd

population_dict = {
    'France':65429495,
    'Germany':82408706,
    'Russia':143910127,
    'Japan':126922333,
}
population = pd.Series(population_dict)
area_dict = {
    'France':643801,
    'Germany':357386,
    'Russia':17125200,
    'Japan':377972
}
area = pd.Series(area_dict)
country_code_dict = {
    'France':33,
    'Germany':49,
    'Russia':7,
    'Japan':81
}
countries1 = pd.DataFrame({'Area':area,'Population':population})
countries2 = pd.DataFrame({'Population':population,'Country_Code':country_code_dict})
countries3 = pd.merge(countries1, countries2, left_index=True,right_index=True,on='Population')
countries3