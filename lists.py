# easy, getattr() concept
if __name__ == '__main__':
    N = int(input())
    lis = []

    for _ in range(N):
        command, *value = input().split()

        if command == "print":
            print(lis)

        else:
            getattr(lis, command)(*(map(int, value)))
