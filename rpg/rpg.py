class Character():
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name

    def alive(self):
        if self.health > 0: return True
        return False
    
    def status(self):
        print("%s has %d health and %d power." % (self.name, self.health, self.power))
        
    def attack(self, opp):
        opp.health -= self.power
        print("%s does %d damage to %s." % (self.name, self.power, opp.name))
        if opp.health <= 0:
            print(f"{opp.name} is dead.")

# class Hero(Character):
        
#     def attack(self, goblin):
#         goblin.health -= self.power
#         print("You do %d damage to the goblin." % self.power)
#         if goblin.health <= 0:
#             print("The goblin is dead.")
        
    
# class Goblin(Character):
        
#     def attack(self, hero):
#         hero.health -= self.power
#         print("The goblin does %d damage to you." % self.power)
#         if hero.health <= 0:
#             print("You are dead.")
        
def main():
    hero_health = 10
    hero_power = 5
    hero_name = "Hero"
    goblin_health = 6
    goblin_power = 2
    goblin_name = "Goblin"

    hero = Character(hero_health, hero_power, hero_name)
    goblin = Character(goblin_health, goblin_power, goblin_name)

    while goblin.alive() and hero.alive():
        hero.status()
        goblin.status()
        print()
        print("What do you want to do?")
        print(f"1. fight {goblin_name}")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin.health > 0:
            # Goblin attacks hero
            goblin.attack(hero)

main()