import numpy as np
a=np.array([1,-4,6,-7])
b=np.array([0,-5,-8,7])
a=np.sign(a)
b[b>0]=1
b[b<0]=-1
print(b)
print(a)
print(b)
