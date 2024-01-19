class Character():
    def __init__(self, health, defense, attack, speed, luck, name):#, movelist):
        self.health = health
        self.defense = defense
        self.attack = attack
        self.speed = speed
        self.luck = luck
        self.name = name
        # self.movelist = movelist
    
    def alive(self):
        if self.health > 0: return False
        return True

    def status(self):
        print(f"\n{self.name}'s stats:\nHealth: {self.health}\nDefense: {self.defense}\nAttack: {self.attack}\nSpeed: {self.speed}\nLuck: {self.luck}\n")

    def action(self, enemy):
        # Calls move function within the Character class.
        pass
# class Action():
#     def __init__(self):
#         pass

def changeStat(stat, statName, baseStat, minPoints, points):
    choice = input(f"Would you like to (1) Increase your {statName} or (2) Decrease your {statName}? ({statName} must be at least {(baseStat - minPoints)})| ")
        
    if choice == "1":
        if points == 0:
            print(f"\nYou have no points to increase your {statName} with. Please decrease points from another stat first!")
            return stat
        amount = int(input(f"\nYou have {points} points remaining. By how much would you like to increase your {statName}? | "))
        if amount > points:
            print("\nYou have exceeded the number of points you have available. Please only attempt to use the points you have!")
            return stat
        stat += amount
    
    if choice == "2":
        amount = int(input(f"\nYou have {stat} {statName}. By how much would you like to decrease your {statName}? (Minimum {(baseStat-minPoints)}) | "))
        if (stat - amount) < (baseStat - minPoints):
            print(f"\nYou took away too much! Please only take away at most {minPoints} points from a given stat")
            return stat
        stat -= amount
            
    return stat

def createChar():
    baseHealth = health = 100
    baseDefense = defense = 5
    baseAttack = attack = 10
    baseSpeed = speed = 10
    baseLuck = luck = 10
    # movelist = []
    points = 10
    minPoints = 5
    choice = ""
    condition = True
    
    # Choose stats
    while(condition):
        print(f"\nCurrent stats:\nHealth: {health}\nDefense: {defense}\nAttack: {attack}\nSpeed: {speed}\nLuck: {luck}\n")
        print(f"You have {points} points remaining. Which stat would you like to increase/decrease?\n")
        print("(1) Health\n(2) Defense\n(3) Attack\n(4) Speed\n(5) Luck\n(6) Finish Character Creation\n")
        choice = input("Choice | ")
        if choice == "1":
            prev = health
            health = changeStat(health, "Health", baseHealth, minPoints, points)
            points += prev - health
        
        if choice == "2":
            prev = defense
            defense = changeStat(defense, "Defense", baseDefense, minPoints, points)
            points += prev - defense
        
        if choice == "3":
            prev = attack
            attack = changeStat(attack, "Attack", baseAttack, minPoints, points)
            points += prev - attack
        
        if choice == "4":
            prev = speed
            speed = changeStat(speed, "Speed", baseSpeed, minPoints, points)
            points += prev - speed
        
        if choice == "5":
            prev = luck
            luck = changeStat(luck, "Luck", baseLuck, minPoints, points)
            points += prev - luck
        
        if choice == "6":
            condition = False
            name = input("Give your character a name: ")
            print(f"\n{name} Created!\n")
        
    return Character(health, defense, attack, speed, luck, name) #, movelist)

def main():
    print("Player 1, create your character!")
    p1 = createChar()

    print("Player 2, create your character!")
    p2 = createChar()

    while(p1.alive() and p2.alive()):
        p1.status()
        p2.status()
        if p1.speed > p2.speed:
            # P1 Does their move first
            p1.action(p2)
            if p2.alive():
                print(f"{p1.name} is the winner!")
                break
            p2.action(p1)
            if p1.alive():
                print(f"{p2.name} is the winner!")
                break
        else:
            # P2 Does their move first
            p2.action(p1)
            if p1.alive():
                print(f"{p2.name} is the winner!")
                break
            p1.action(p2)
            if p2.alive():
                print(f"{p1.name} is the winner!")
                break

main()