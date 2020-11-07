# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections
no_of_shoes = int(input())
sizes_in_stock = collections.Counter(map(int, input().split()))
# print(sizes_in_stock )
numCust = int(input())
total_revenue =0

for _ in range(numCust):
    size, price = map(int, input().split())
    # print('1', size, price)
    if sizes_in_stock[size]:
        # print(sizes_in_stock[size])
        total_revenue += price
        sizes_in_stock[size] -= 1
        # print(sizes_in_stock[size])
print(total_revenue)
