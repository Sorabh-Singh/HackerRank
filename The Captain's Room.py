
# 5
# 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 
# 8
groups = int(input())
rooms = list(map(int, input().split()))

dict1 = {i:rooms.count(i) for i in rooms}

for key, value in dict1.items():
    if value ==1:
        print("captain is staying in room no: ", key)


