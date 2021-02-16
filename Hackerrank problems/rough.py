'''
It must contain at least  2 uppercase English alphabet characters.
It must contain at least 3 digits ( - ).
It should only contain alphanumeric characters ( - ,  -  &  - ).
No character should repeat.
There must be exactly  10 characters in a valid UID.
'''
import re
cust_count = int(input())

for _ in range(cust_count):
    ccNumber = input()

    PU = re.compile(r'[A-Z]')
    first_check = PU.findall(ccNumber)

    PD = re.compile(r'\d')
    second_check = PD.findall(ccNumber)

    PA = re.compile(r'\W')
    third_check = PA.findall(ccNumber)

    if len(first_check) >2 and len(second_check) >3 and len(third_check)==0:
        if (len(set(first_check)) + len(set(second_check)) == len(ccNumber)) and len(ccNumber)==10:
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")


    # print(first_check,second_check, third_check , sep = '\n')

# import re

# for _ in range(int(input())):
#     u = ''.join(sorted(input()))
#     try:
#         assert re.search(r'[A-Z]{2}', u)
#         assert re.search(r'\d\d\d', u)
#         assert not re.search(r'[^a-zA-Z0-9]', u)
#         assert not re.search(r'(.)\1', u)
#         assert len(u) == 10
#     except:
#         print('Invalid')
#     else:
#         print('Valid')




