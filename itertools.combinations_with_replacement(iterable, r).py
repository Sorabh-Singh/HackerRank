Approach:1
from itertools import combinations_with_replacement
inp=input().split()
x=combinations_with_replacement(sorted(inp[0]),int(inp[1]))
for i in x:
    print(''.join(i))
# Tip:-
#        combinations_with_replacement('ABC',2) gives AA AB AC BB BC CC
#        combinations('ABC',2) gives AB AC BC
#        observe the diffrences between them.

Approach:2
from itertools import combinations_with_replacement
my_str, rep_size = input().split()

possible_combs = combinations_with_replacement(sorted(my_str), int(rep_size))

for i in possible_combs:
    print(''.join(i))