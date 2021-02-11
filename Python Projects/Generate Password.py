import random
password_length = int(input("length of password : "))
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
flag = ''
while flag != "y":

    temp_password = random.sample(s, password_length)
    print(''.join(temp_password))
    print('''do you want more password created?
if yes, enter 'c' or enter 'q' to quit.''')
    flag = input("enter your choice :")

    if flag == 'c':
        continue
    else:
        print("Thanks for using our services!!")
        exit()
