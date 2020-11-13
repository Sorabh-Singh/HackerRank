
phoneBook={}
for _ in range(int(input())):
    phoneNumber, name =input().split()
    phoneBook.update({phoneNumber:name})
# print(phoneBook)

while(True):
phoneBook={}
for _ in range(int(input())):
    phoneNumber, name =input().split()
    phoneBook.update({phoneNumber:name})

while True:
    try:
        name = input()
        if name in phoneBook:
            # print('%s=%s' % (name, phoneBook[name]))
            print(name, phone_book[name],sep="=")
        else:
            print('Not found')
    except:
        break