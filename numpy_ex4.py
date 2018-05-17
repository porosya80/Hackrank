import numpy as np
row,column=map(int,input().split())
res_ar = np.array([[int(s) for s in input().split()]for j in range(row)])
# print(np.prod((np.sum(res_ar,axis = 0)), axis = 0))
# print(np.max(np.min(res_ar, axis = 1)))
print (np.mean(res_ar, axis = 1))
print (np.var(res_ar, axis = 0))
print (np.std(res_ar))
