import numpy as np
import pandas as pd

df = pd.DataFrame(
    {
        "A":[5,3,None,4],
        "B":[None,2,4,3],
        "C":[4,3,8,5],
        "D":[5,4,2,None]
    }
)

df
df.bfill(axis=1)