import random

class Garden():
    def __init__(self):
        self.trees = []
        self.gnomes = []
        self.woodchucks = []
        self.water = 100

class Tree():
    def __init__(self):
        self.shade = 2
    
class Gnome():
    def __init__(self):
        self.luck = 5
    
class Woodchuck():
    def __init__(self):
        self.luck = 5
    
garden = Garden()
day = 0
goal = 10
rainChance = 0
chompChance = 0
waterTaken = 0
while(True):
    day += 1
    print(f"It is now day {day}!")
    
    if day % 10 == 0:
        # Random chance of earning another Tree or Gnome
        if random.randrange(1,3) <= 1:
            if random.randrange(1,6) <= 3 :
                print("A tree has been added to your garden. Lucky!")
                garden.trees.append(Tree())
            else:
                print("A gnome has been added to your garden. Lucky!")
                garden.gnomes.append(Gnome())
    
    # Random chance of woodchuck moving in
    if random.randrange(1,101) <= 1:
        print("A woodchuck has moved into your garden. Watch out!")
        garden.woodchucks.append(Woodchuck())
    
    # Random chance of rain occuring
    rainChance = random.randrange(1,101)
    for gnome in garden.gnomes:
        rainChance += gnome.luck
    if random.randrange(1,101) <= rainChance:
        print("It rained! Your garden's water level has increased")
        garden.water += 20
    
    # Check if the garden survives to live another day
    waterTaken = random.randrange(1,10)
    for tree in garden.trees:
        waterTaken -= tree.shade
    garden.water -= waterTaken
    if garden.water <= 0:
        print("Your garden has run out of water! Game over.")
        break
    
    # Check if a woodchuck eats one of the trees
    chompChance = 0
    for woodchuck in garden.woodchucks:
        chompChance += woodchuck.luck
    if random.randrange(1,101) <= chompChance:
        if len(garden.trees) > 0: garden.trees.pop()
        print(f"Oh no! A woodchuck has eaten one of your trees. {len(garden.trees)} trees remaining.")
    
    # Check if we have reached the goal amount of trees
    if len(garden.trees) >= goal:
        print(f"You have reached {goal} trees! Congratulations!")
        break