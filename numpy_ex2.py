import numpy
array1= []
array2= []

# row,column=map(int,input().split())
row = int(input())
for i in range(2):
    if i == 0:
        for j in range(row):
            array1.append(list(map(int, input().split())))
    if i == 1:
        for j in range(row):
            array2.append(list(map(int, input().split())))

a = numpy.array(array1)
b = numpy.array(array2)

print(numpy.dot(a,b))
# print (numpy.add(a,b),a -b ,a*b,a//b,a%b,a**b, sep= "\n" )

# import numpy as np
# n, m = (int(s) for s in input().split())
# a, b = (np.fromiter((s for _ in range(n) for s in input().split()), dtype=np.int64).reshape((n, m)) for _ in range(2))
# print("\n".join(str(op(a, b)) for op in (np.add, np.subtract, np.multiply, np.floor_divide, np.mod, np.power)))