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

happiness_level= 0

for i in N:
    if i in A:
        happiness_level = happiness_level + 1
    
    elif i in B:
        happiness_level = happiness_level - 1

print(happiness_level)



