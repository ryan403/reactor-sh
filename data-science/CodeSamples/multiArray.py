import numpy as np
name = np.array(["張山","李潔","王武","陳至","何美"])
gender = np.array(["male","female","male","male","female"])
height = np.array([172,155,183,153,168,160])
weight = np.array([75.2,45.6,84.3,72.1,51.0])
score_math = np.array([45,74,62,89,32,55])
score_english = np.array([92,85,28,61,78])
score_chinese = np.array([88,55,70,61,98])

name[gender=="female"]
score_chinese[gender!='female'].mean()
name[score_chinese<60]

