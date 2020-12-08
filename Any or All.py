# 5
# 12 9 61 5 14 
# Condition 1: All the integers in the list are positive.
# Condition 2: 5 is a palindromic integer.

n, arr = int(input()), input().split()

# True if all({i>0 for i in lt) and (any(i==i[::-1] for i in lt)) else False
    
print(all(int(i)>=0 for i in arr) and any(i == i[::-1]for i in arr))