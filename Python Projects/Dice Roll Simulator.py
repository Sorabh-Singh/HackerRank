import random

roll_again = 'yes'

# while roll_again != "end" or roll_again != "quit":
while roll_again =="yes" or roll_again =="y":

    print("rollling the dice...")
    print("Values are : ")
    print(random.randint(1, 6))
    print(random.randint(1, 6))
   
    roll_again = input("Enter yes or y for rolling dice again, any other key will terminate the loop! : ")
    # print("user provided input", roll_again)
print("Thanks for your participation")