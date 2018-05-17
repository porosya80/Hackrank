import math

ab = int(input())
bc = int(input())


print (str(int(round(math.degrees(math.atan2(ab,bc)))))+u'\u00b0')

# a_angle = math.tan(ab/bc)

# print (math.degrees(a_angle))

