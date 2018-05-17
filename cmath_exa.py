import cmath

z_com = complex(input())

result = cmath.polar(z_com)
first = str(result[0])
second = str(result[1])
print (first)
print(second)


print("\n".join(map(str, cmath.polar(complex(input())))))