import random
result = random.randint(1,3)
print("ROCK PAPER SCISSORS! Choose R, P, or S")
player = input()
if player != "R" or player != "P" or player != "S":
    print("Clearly you don't know how to play. See Ya!")
else:
    if player == "R":
        print("You chose rock")
    if player == "P":
        print("You chose paper")
    if player =="S":
        print("You chose Scissors")
if result == 1:
    print("Opponent chooses Rock")
elif result == 2:
    print("Opponent chooses paper")
elif result == 3:
    print("Opponent chooses Scissors")
if player == "R" and result == 1:
    print("DRAW!")
elif player == "R" and result == 2:
    print("YOU LOSE!")
elif player == "R" and result == 3:
    print("YOU WIN!")
elif player == "P" and result == 1:
    print("YOU WIN!")
elif player == "P" and result == 2:
    print("DRAW!")
elif player == "P" and result == 3:
    print("YOU LOSE!")
elif player == "S" and result == 1:
    print("YOU LOSE!")
elif player == "S" and result == 2:
    print("YOU WIN!")
elif player == "S" and result == 3:
    print("DRAW!")