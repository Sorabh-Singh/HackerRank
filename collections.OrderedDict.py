# Approach without using collections
from collections import OrderedDict
my_order = {}

for _ in range(int(input())):
    item = list(map(str, input().split()))
    item_name = ' '.join(item[:-1])
    item_price = int(item[-1])

    if item_name not in my_order.keys():
        my_order.update({item_name: item_price})
    else:
        net_price = my_order[item_name] + item_price
        my_order[item_name] = net_price

for key, value in my_order.items():
    print(key, value)

# Approach:2
d = OrderedDict()
for _ in range(int(input())):
    items = input().split(' ')
    item = ' '.join(items[:-1])
    d[item] = d.get(item, 0)+int(items[-1])
for i in d.items():
    print(*i)
