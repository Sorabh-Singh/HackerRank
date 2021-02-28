# Approach:1
'''
9587456281
1252478965
'''
import re
for _ in range(int(input())):
    if re.match(r'[789]\d{9}$',input()):   
        print('YES')  
    else:  
        print('NO')

# Approach:2
# count = int(input())
# for _ in range(count):
#     raw_number = input()
#     if len(raw_number)==10 and raw_number[0] in ['7', '8', '9'] and raw_number.isnumeric():
#         print("YES")
#     else:
#         print("NO")

