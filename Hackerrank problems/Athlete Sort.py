N, M = map(int, input().split())
arr = []
# arr = [list(map(int, input().split())) for _ in range(n)]
for _ in range(N):
    arr.append(list(map(int, input().split())))

k = int(input())

arr = sorted(arr, key=lambda x: x[k])
for i in arr:
    print(*i)
