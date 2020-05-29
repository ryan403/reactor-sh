import numpy as np
import pandas as pd
example = pd.DataFrame({
    'letters':['A','B','A','B','B'],
    'numbers':[1,2,1,3,3]
})
example
example.drop_duplicates()
