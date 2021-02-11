import random
print('Welcome to our game world, designed by Singh.')
player_score, computer_score = 0, 0


while True:
    computer = random.choice(['rocks', 'paper', 'scissors'])
    player = input("Player's option :")

    if player == computer:
        print("Tie")
        print("player chosen option :", player, "computer chosen option :", computer)
        print("player score :", player_score, "computer score :", computer_score)

    elif player == "rocks":
        if computer == "paper":
            player_score += 1
            print("player chosen option :", player, "computer chosen option :", computer)
            print("player score :", player_score, "computer score :", computer_score)

        else:
            player_score += 1
            print("player chosen option :" , player, "computer chosen option :", computer)
            print("player score :", player_score, "computer score :", computer_score)

    elif player == "paper":
        if computer == "rocks":
            computer_score += 1
            print("player chosen option :" ,player, "computer chosen option :", computer)
            print("player score :", player_score,  "computer score :", computer_score)

        else:
            computer_score += 1
            print("player chosen option :", player, "computer chosen option :", computer)
            print("player score :", player_score,  "computer score :", computer_score)

    elif player == "scissors":
        if computer == "paper":
            player_score += 1
            print("player chosen option :", player, "computer chosen option :", computer)
            print("player score :", player_score,  "computer score :", computer_score)

        else:
            computer_score += 1
            print("player chosen option :", player, "computer chosen option :", computer)
            print("player score :", player_score,  "computer score :", computer_score)

    elif player == "end":
        if player_score > computer_score:
            print("Player won the match.")
            break
        
        elif player_score == computer_score:
            print("match tied")
            break

        else:
            print("Player lost the match.")
            break


        

