import random
# Monster Card Base
class monstercard:
    def __init__(self,name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense
    def attack(self,attack,defense):
        return
# Player 1

# Game Settings
run = 1
HeavyAllowed = 2
MidAllowed = 6
LightAllowed = 12
SpellsAllowed = 5
while run == 1:
    # Open a booster pack
    # Ask to play again
    print("Type 1 to play again. Type 0 to quit")
    run = int(input())