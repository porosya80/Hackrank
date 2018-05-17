from collections import OrderedDict
words = OrderedDict()
for _ in range(int(input())):
    name = input().strip()
    if name in words:
        words[name] += 1
    else:
        words[name] = 1

print(len(words))
print(" ".join(map(str,words.values())))


