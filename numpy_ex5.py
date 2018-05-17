import numpy as np
res_ar = np.array([int(s) for s in input().split()])
res_ar2 = np.array([int(s) for s in input().split()])

print(np.inner(res_ar, res_ar2))
print(np.outer(res_ar, res_ar2))