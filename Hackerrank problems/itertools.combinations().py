#Concept
from itertools import combinations
my_str, rep_size = input().split()

for num in range(1, int(rep_size)+1):
    possible_combs = combinations(sorted(my_str), num)
    for i in possible_combs:
        print(''.join(i))
