from itertools import permutations
my_str, rep_size = input().split()

# for num in range(1, int(rep_size)+1):
possible_combs = permutations(sorted(my_str), int(rep_size))
for i in possible_combs:
    print(''.join(i))