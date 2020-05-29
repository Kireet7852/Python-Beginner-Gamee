import random
lst = {"s","w","g"}
chance=10
no_of_chance=0
computer_point=0
player_point=0

print("\t \t \t \t SNAKE,WATER,GUN GAME \n\n")
print("S for snake \nW for water \nG for gun \n")

#making the game in while

while no_of_chance<chance:
    _input = input("Snake,Water,Gun")
    _random = random.choice(lst)

    if _input == _random:
        print("Tie!!! Both 0 point to each \n")

    #if user input s.
    if _input == "s" and _random == "g":
        computer_point = computer_point +1
        print(f"Your guess is {_input} and computer guess is {_random}\n")
        print("Computer wins 1 point \n")
        print(f"Computer_point is {computer_point} and  your point is {player_point} \n")

    elif _input == "s" and _random == "w":
        player_point = player_point +1
        print(f"Your guess is {_input} and computer guess is {_random}\n")
        print("User wins 1 point \n")
        print(f"Computer_point is {computer_point} and your point is {player_point} \n")

    #if user input w
    if _input == "w" and _random == "s":
        computer_point =  computer_point +1
        print(f"Your guess is {_input} and computer guess is {_random}\n")
        print("Computer wins 1 point \n")
        print(f"Computer_point is {computer_point} and your point is {player_point} \n")

    elif _input == "w" and _random == "g":
        player_point = player_point +1
        print(f"Your guess is {_input} and computer guess is {_random}\n")
        print("User wins 1 point \n")
        print(f"Computer_point is {computer_point} and your point is {player_point} \n")

    #if user input g
    if _input == "g" and _random == "s":
        player_point = player_point
        print(f"Your guess is {_input} and computer guess is {_random}\n")
        print("User wins 1 point \n")
        print(f"Computer_point is {computer_point} and your point is {player_point} \n")

    elif _input == "g" and _random == "w":
        computer_point = computer_point +1
        print(f"Your guess is {_input} and computer guess is {_random}\n")
        print("Computer wins 1 point \n")
        print(f"Computer_point is {computer_point} and your point is {player_point} \n")

    else:
        print("!!!!You have input wrong answer!!!!\n")

    no_of_chance = no_of_chance +1
    print(f"{chance - no_of_chance} is left out of {chance}\n")

print("GAME OVER")

if computer_point > player_point:
     print("Computer win and You loose")

if computer_point < player_point:
     print("You win and Computer loose")

print(f"Your point is {player_point} and Computer point is {computer_point}")
