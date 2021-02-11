# Given  sets of integers,  and , print their symmetric difference in ascending order. 
# The term symmetric difference indicates those values that exist in either  or  but do not exist in both.
# Sample input
# 4
# 2 4 5 9
# 4
# 2 4 11 12
# # Saple output
# 5
# 9
# 11
# 12

# >> a = {2, 4, 5, 9}
# >> b = {2, 4, 11, 12}
# >> a.union(b) # Values which exist in a or b
# {2, 4, 5, 9, 11, 12}
# >> a.intersection(b) # Values which exist in a and b
# {2, 4}
# >> a.difference(b) # Values which exist in a but not in b
# {9, 5}

# >>> a , b =[list(map(int, input().split())) for _ in range(2)]
# 1 2 3  5 5 66 6 6 6
# 6455 43  354  3 2 312 3  3 3
# >>> a
# [1, 2, 3, 5, 5, 66, 6, 6, 6]
# >>> b
# [6455, 43, 354, 3, 2, 312, 3, 3, 3]
# >>> 

# code bigins here
# Approach- 1
# la = int(input())
# a = set(map(int, input().split())) for _ in range(input())
# lb = int(input())
# b= set(map(int, input().split()))

# for i in sorted(a.difference(b)):
#     print(i)

# for i in sorted(b.difference(a)):
#     print(i)


# Approach:2

a,b = [set(map(int, input().split())) for _ in range(4)][1::2]
result = sorted(a^b, key=int)
print(*result, sep='\n')