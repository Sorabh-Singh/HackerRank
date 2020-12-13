'''
Input Format

The first line contains integers  and  separated by a space.
The second line contains  integers, the elements of the array.
The third and fourth lines contain  integers,  and , respectively.

Output Format

Output a single integer, your total happiness.

Sample Input

3 2
1 5 3
3 1
5 7
Sample Output

1
'''
n,m = map(int,input().split())
N = list(map(int,input().split()))
A = set(map(int,input().split()))
B = set(map(int,input().split()))
print(A, B)

happiness_level= 0

for i in N:
    if i in A:
        print("A before", i, happiness_level)
        happiness_level = happiness_level + 1
        print("A after", i, happiness_level)
    
    elif i in B:
        print("B before", i, happiness_level)
        happiness_level = happiness_level - 1
        print("B after ", i, happiness_level)
print(happiness_level)



