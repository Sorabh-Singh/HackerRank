# You are given a set  and  other sets.
# Your job is to find whether set  is a strict superset of each of the  sets.

# Print True, if  is a strict superset of each of the  sets. Otherwise, print False.

# A strict superset has at least one element that does not exist in its subset.

# Example
# Set is a strict superset of set.
# Set is not a strict superset of set.
# Set is not a strict superset of set.

# Input Format

# The first line contains the space separated elements of set .
# The second line contains integer , the number of other sets.
# The next  lines contains the space separated elements of the other sets.

# 1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
# 2
# 1 2 3 4 5
# 100 11 12

setA = set(map(int, input().split()))
res =[]
for _ in range(int(input())):
    a=set(map(int, input().split()))
    res.append(setA.issuperset(a))

print(all(i==True for i in res))


# seta = set(map(input().split()))
# print(all([seta.issuperset(set(map(int, input().split()))) for i in range(int(input()))]))
