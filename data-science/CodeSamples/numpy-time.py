import numpy as np

my_list = list(range(1000000))
#%time my_list2 = [x*2 for x in my_list]

my_arr = np.array(my_list)
#%time my_arr = my_arr*2


