# Approach:1
a , b = map(int, input().split())
words_a=[input() for _ in range(a)]
words_b=[input() for _ in range(b)]

for i in words_b:
    for index, char in enumerate(words_a):
        if i==char:
            print(index+1, end=' ')
        elif i not in words_a:
            print('-1')
    print()

# Approach:2
from collections import defaultdict

# Inputs
# ------
n, m = map(int, input().split(' '))

# Let's get the groups as lists
# -----------------------------
#input1 = ['a', 'a', 'b', 'a', 'b']
#input2 = ['a', 'b']
input1 = list()
for i in range(n):
    input1.append(input())

    input2 = list()
for i in range(m):
    input2.append(input())

# Calculate Output
# ----------------
d = defaultdict(list)

# Fill d with input1 values
for i in range(n):
    d[input1[i]].append(i+1)
#print(d) --> defaultdict(<class 'list'>, {'a': [1, 2, 4], 'b': [3, 5]})

# Apply the logic for printing
for i in input2:    
    if i in d:
        print(*d[i])
    else:
        print(-1)

        



        


