import numpy as np

res_ar = [float(s) for s in input().split()]
x = int(input())

print(np.polyval(res_ar,x))