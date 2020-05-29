import numpy as np
myList = [True, "Bob", 3.0, 4]
myListTypeList = [type(item) for item in myList]

myArray = np.array([True, "Bob", 3.0, 4]);
myArrayTypeList = [type(item) for item in myArray]