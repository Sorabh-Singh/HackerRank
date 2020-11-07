from itertools import product
a = list(map(int, input().split()))
b = list(map(int, input().split()))
re = list(product(a, b))

result = ''
for i in re:
    result += str(i) + ' '
print(result)

