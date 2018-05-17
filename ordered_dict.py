from collections import OrderedDict
goods = OrderedDict()
for _ in range(int(input())):
    name, price = [s for s in input().rsplit(" ",1)]
    # a = " ".join((rec[:-1]))
    if  name in goods:
        goods[name] += int(price)
    else:
        goods[name] = int(price)
for k in goods:
    print("{} {}".format(k,goods[k]))


