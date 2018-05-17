import numpy as np

row=int(input())
res_ar = np.array([[float(s) for s in input().split()]for j in range(row)])

print(np.linalg.det(res_ar))