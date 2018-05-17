n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
plus, minus , zero = 0,0,0
for i in arr:
    if i > 0:
        plus += 1
    elif i < 0:
        minus += 1
    elif i == 0:
        zero += 1

print("{:f}".format(plus/n))
print("{:f}".format(minus/n))
print("{:f}".format(zero/n))
