import numpy as np
array = np.fromiter((list(map(float,input().split()))), dtype=np.float)

print (np.floor(array))
print (np.ceil(array))
print (np.rint(array))