# https://www.hackerrank.com/challenges/30-2d-arrays/problem

    # 1 1 1 0 0 0
    # 0 1 0 0 0 0
    # 1 1 1 0 0 0
    # 0 0 2 4 4 0
    # 0 0 0 2 0 0
    # 0 0 1 2 4 0

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
        
    res = []

    for x in range(0, 4):
        for y in range(0, 4):
            s = sum(arr[x][y:y+3]) + arr[x+1][y+1] + sum(arr[x+2][y:y+3])
            res.append(s)

    print(max(res))
