import random
Approach 1:

roll_again = 'yes'

# while roll_again != "end" or roll_again != "quit":
while roll_again == "yes" or roll_again == "y":

    print("rollling the dice...")
    print("Values are : ")
    print(random.randint(1, 6))
    print(random.randint(1, 6))

    roll_again = input(
        "Enter yes or y for rolling dice again, any other key will terminate the loop! : ")
    # print("user provided input", roll_again)
print("Thanks for your participation")

Approach: 2

# importing module for random number generation

# range of the values of a dice
min_val = 1
max_val = 6

# to loop the rolling through user input
roll_again = "yes"

# loop
while roll_again == "yes" or roll_again == "y":
    print("Rolling The Dices...")
    print("The Values are :")

    # generating and printing 1st random integer from 1 to 6
    print(random.randint(min_val, max_val))

    # generating and printing 2nd random integer from 1 to 6
    print(random.randint(min_val, max_val))

    # asking user to roll the dice again. Any input other than yes or y will terminate the loop
    roll_again = input("Roll the Dices Again?")
