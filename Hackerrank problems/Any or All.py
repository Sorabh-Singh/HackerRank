# 5
# 12 9 61 5 14 
# Condition 1: All the integers in the list are positive.
# Condition 2: 5 is a palindromic integer.

n, my_list = int(input()), input().split()    
print(all(int(i)>=0 for i in my_list) and any(i == i[::-1]for i in my_list))