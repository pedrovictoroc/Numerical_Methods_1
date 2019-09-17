from bissection import *
from altered_bissection import *

import time

#func = [3,-9,0,1]

func = [-30,31,-10,1]

a = 0

b = 3

e = 0.00000001

maxIte = 10

t1 = time.time()
altered_bissection(func,a,b,e,maxIte)
t2 = time.time()
print(t2-t1)
t3 = time.time()
bissection(func,a,b,e,maxIte)
t4 = time.time()
print(t4-t3)