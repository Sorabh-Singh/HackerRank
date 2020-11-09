eng_num = int(input())
e = set(map(int, input().split()))

french_num = int(input())      
f = set(map(int, input().split()))
print(len(e-f))

# Set .union() Operation

eng_num = int(input())
e = set(map(int, input().split()))

french_num = int(input())      
f = set(map(int, input().split()))
print(len(e.union(f)))

