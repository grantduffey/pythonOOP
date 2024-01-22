import random
class Character():
    def __init__(self, health, defense, attack, speed, luck, name):
        self.health = health
        self.defense = defense
        self.attack = attack
        self.speed = speed
        self.luck = luck
        self.name = name
        self.ff = False
    
    def alive(self):
        if self.health > 0: return False
        return True

    def status(self):
        print(f"\n{self.name}'s stats:\nHealth: {self.health}\nDefense: {self.defense}\nAttack: {self.attack}\nSpeed: {self.speed}\nLuck: {self.luck}\n")

    def normAttack(self, enemy):
        damage = self.attack - enemy.defense
        if damage > 0:
            enemy.health -= damage
            if enemy.health < 0: enemy.health = 0
            print(f"{enemy.name} took {damage} damage from {self.name}'s normal attack! {enemy.name} has {enemy.health} health.\n")
        else:
            print(f"{self.name}'s attack did no damage!\n")
    
    def reckAttack(self, enemy):
        damage = self.attack + int(round((self.attack/2))) - enemy.defense
        if damage > 0:
            enemy.health -= damage
            if enemy.health < 0: enemy.health = 0
            print(f"{enemy.name} took {damage} damage from {self.name}'s reckless attack! {enemy.name} has {enemy.health} health.\n")
        else:
            print(f"{self.name}'s attack did no damage!\n")
            
        if random.randrange(1, 101) + self.luck >= 60:
            pass
        else:
            self.health -= int(round(damage/2))
            if self.health < 0: self.health = 0
            print(f"{self.name}'s reckless attack hurt them in the process! {self.name} has {self.health} health!\n")
        
    
    def stunAttack(self, enemy):
        damage = int(round((self.attack - enemy.defense)/2))
        if damage > 0:
            enemy.health -= damage
            if enemy.health < 0: enemy.health = 0
            print(f"{enemy.name} took {damage} damage from {self.name}'s stun attack! {enemy.name} has {enemy.health} health.\n")
        else:
            print(f"{self.name}'s attack did no damage!\n")
        
        if random.randrange(1, 101) + self.luck >= 50:
            print(f"{enemy.name} has been stunned! {self.name} get's an extra turn.\n")
            self.action(enemy)
    
    def focus(self):
        print("(1) Attack    (2) Defense    (3) Speed    (4) Luck")
        choice = input("Which stat would you like to increase? | ")
        
        if choice == "1":
            self.attack += 5 + random.randrange(1, self.luck+1)
            print(f"{self.name}'s attack is now {self.attack}!\n")
        
        elif choice == "2":
            self.defense += 5 + random.randrange(1, self.luck+1)
            print(f"{self.name}'s defense is now {self.defense}!\n")
        
        elif choice == "3":
            self.speed += 5 + random.randrange(1, self.luck+1)
            print(f"{self.name}'s speed is now {self.speed}!\n")
        
        elif choice == "4":
            self.luck += 5 + random.randrange(1, self.luck+1)
            print(f"{self.name}'s luck is now {self.luck}!\n")
    
        else:
            print(f"\n{self.name} has not input a valid option and has forfeited their turn!\n")
    
    def rest(self):
        self.health += 10 + random.randrange(1, self.luck+1)
        if self.health > 100: self.health = 100
        print(f"{self.name}'s health is now {self.health}!\n")
    
    def action(self, enemy):
        # Calls move function within the Character class.
        print(f"{self.name}, it's your turn! Choose your move:")
        print("(1) Normal Attack    (2) Reckless Attack    (3) Stun Attack")
        print("(4) Focus            (5) Rest               (6) Forfeit\n")
        choice = input("What will you do? | ")
        if choice == "1":
            self.normAttack(enemy)
            
        elif choice == "2":
            self.reckAttack(enemy)
            
        elif choice == "3":
            self.stunAttack(enemy)
            
        elif choice == "4":
            self.focus()
            
        elif choice == "5":
            self.rest()
            
        elif choice == "6":
            self.ff = True
            
        else:
            print(f"\n{self.name} has not input a valid option and has forfeited their turn!\n")

def changeStat(stat, statName, baseStat, minPoints, points):
    choice = input(f"Would you like to (1) Increase your {statName} or (2) Decrease your {statName}? ({statName} must be at least {(baseStat - minPoints)})| ")
        
    if choice == "1":
        if points == 0:
            print(f"\nYou have no points to increase your {statName} with. Please decrease points from another stat first!\n")
            return stat
        amount = int(input(f"\nYou have {points} points remaining. By how much would you like to increase your {statName}? | "))
        if amount > points:
            print("\nYou have exceeded the number of points you have available. Please only attempt to use the points you have!\n")
            return stat
        stat += amount
    
    if choice == "2":
        amount = int(input(f"\nYou have {stat} {statName}. By how much would you like to decrease your {statName}? (Minimum {(baseStat-minPoints)}) | "))
        if (stat - amount) < (baseStat - minPoints):
            print(f"\nYou took away too much! Please only take away at most {minPoints} points from a given stat\n")
            return stat
        stat -= amount
            
    return stat

def createChar():
    baseHealth = health = 100
    baseDefense = defense = 5
    baseAttack = attack = 10
    baseSpeed = speed = 10
    baseLuck = luck = 10
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
        
    return Character(health, defense, attack, speed, luck, name)

def main():
    print("Player 1, create your character!")
    p1 = createChar()

    print("Player 2, create your character!")
    p2 = createChar()

    while(not p1.alive() and not p2.alive()):
        p1.status()
        p2.status()
        if p1.speed >= p2.speed: # Figure out a better way to determine who goes first in a speed tie. For now P1 just goes first
            # P1 Does their move first
            p1.action(p2)
            if p1.ff == True: 
                print(f"\n{p2.name} is the winner!")
                break
            if p2.alive():
                print(f"\n{p1.name} is the winner!")
                break
            p2.action(p1)
            if p2.ff == True: 
                print(f"\n{p1.name} is the winner!")
                break
            if p1.alive():
                print(f"\n{p2.name} is the winner!")
                break
        else:
            # P2 Does their move first
            p2.action(p1)
            if p2.ff == True: 
                print(f"\n{p1.name} is the winner!")
                break
            if p1.alive():
                print(f"\n{p2.name} is the winner!")
                break
            p1.action(p2)
            if p1.ff == True: 
                print(f"\n{p2.name} is the winner!")
                break
            if p2.alive():
                print(f"\n{p1.name} is the winner!")
                break

main()