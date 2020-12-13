# 2D Array - DS
'''
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
An hourglass in  is a subset of values with indices falling in this pattern in 's graphical representation:

a b c
  d
e f g
There are  hourglasses in . An hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum. The array will always be .
'''

arr = [list(map(int, input().split())) for _ in range(6)]
a =[]
for x in range(4):
    for y in range(4):
        a.append(sum(arr[x][y:y+3]) + arr[x+1][y+1] + sum(arr[x+2][y:y+3]))
print(max(a))

