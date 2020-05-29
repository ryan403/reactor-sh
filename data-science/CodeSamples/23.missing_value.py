import numpy as np
import pandas as pd
example = pd.DataFrame([0, np.nan, '', None])
example
example.isnull()
example.dropna()
example.fillna(0)