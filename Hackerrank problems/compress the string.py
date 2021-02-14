from itertools import groupby

for key, group in groupby(input("Enter string here : ")): 
    # print(key, group)
    key= int(key)
    count = len(list(group))
    print((count,key),end=" ")