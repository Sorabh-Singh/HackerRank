from itertools import product
a = list(map(int, input().split()))
b = list(map(int, input().split()))
re = list(product(a, b))
print(*re)

# Explanation:-
# itertools.product() is equal to nested loop. it is an inbuilt function and works faster than nested loop
# It gives output in iterable object so we used list to covert it into list and then we used * to unpack the list
