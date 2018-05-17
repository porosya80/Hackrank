import math
coords = [list(map(int, n.split())) for n in [input() for i in range(int(input()))]]
result = 0
for i in range(1, len(coords)):
    # print(i, len(coords)-1)
    result += math.sqrt(((coords[i][0]-coords[i-1][0])**2)+((coords[i][1]-coords[i-1][1])**2))
    # print(math.sqrt(((coords[i][0]-coords[i-1][0])**2)+((coords[i][1]-coords[i-1][1])**2)))

result += math.sqrt(((coords[-1][0]-coords[0][0])**2)+((coords[-1][1]-coords[0][1])**2))


print(int(result))