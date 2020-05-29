import numpy as np
dataTypes = [('name','S10'),('score',int)]
dataValues = [('John',80),('Marry',60),('Ryan',90),('Leon',40)]
originalArray = np.array(dataValues, dtype=dataTypes)
sortedArray = np.sort(originalArray,order='score')[::-1]
