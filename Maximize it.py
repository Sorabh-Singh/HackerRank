# Sample Input

# 3 1000
# 2 5 4
# 3 7 8 9 
# 5 5 7 8 9 10 
# Sample Output

# 206


# k , M = (map(int, input().split()))
# maxNum_from_list = [max(list(map(int, input().split()))) for _ in range(k)]
# print(sum([i*i for i in maxNum_from_list ])%M)

k , M = (map(int, input().split()))
print(sum([i*i for i in [max(list(map(int, input().split()))) for _ in range(k)]])%M)
# print(sum([i*i for i in maxNum_from_list ])%M)
