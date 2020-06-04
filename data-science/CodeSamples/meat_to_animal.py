import numpy as np
import pandas as pd

df = pd.DataFrame(
    {
        'food':['bacon','pulled pork','bacon',
                'Pastrami','corned beef','Bacon',
                'pastrami','honey ham', 'nova lox'],
        'ounces':[4,3,12,6,7.5,8,3,5,6]
    }
)
df

lowercased = df['food'].str.lower()
lowercased

meat_to_animal = {
    'bacon':'pig',
    'pulled pork':'pig',
    'pastrami':'cow',
    'corned beef':'cow',
    'honey ham':'pig',
    'nova lox':'salmon'
}
meat_to_animal
type(meat_to_animal)

df['animal'] = lowercased.map(meat_to_animal)
df
