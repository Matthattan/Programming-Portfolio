import os
import random

# import character class
from character import Hero, Enemy
from item import short_bow, iron_sword, nuke, smallMed, mediumMed, largeMed

# create instances from character
hero = Hero(name="hero", health=100, inventory=[smallMed, smallMed, short_bow])
hero.equip(iron_sword)
enemy = Enemy(name="Enemy", health=100, weapon=short_bow)

print(f"{enemy.name} was encountered!")

class Game:
    def __init__(self):

        # Player Idle
        while True:
            action = input("What would you like to do \n 1 - Encounter \n 2 - Check Inventory \n 3 - Check Weapon \n 4 - Quit \n")

            # Encounter
            if action == "1":

                # get odds
                encounterRate = random.randint(1,2)
                nukeRate = random.randint(1,5)

                if encounterRate == random.randint(1,5):
                    print(f"You encountered {enemy.name}!")

                    enemy.health = enemy.health_max
                    enemy.health_bar.update()

                    hero.health_bar.draw()
                    enemy.health_bar.draw()

                    while enemy.health > 0 and hero.health > 0:

                        input()

                        hero.attack(enemy)
                        enemy.attack(hero)

                        hero.health_bar.draw()
                        enemy.health_bar.draw()

                    # check who won
                    if enemy.health <= 0:
                        print(f"{enemy.name} was defeated!")

                    elif hero.health <= 0:
                        print(f"{hero.name} was defeated!")

                        hero.health = hero.health_max
                        hero.health_bar.update()

                elif nukeRate == random.randint(1,10):
                    print(f"{hero.name} picked up a {nuke.name}")
                    hero.equip(nuke)

                else:
                    print("Nothing Found!")

            # access inventory
            elif action == "2":
                hero.viewInv()

            # check weapon            
            elif action == "3":
                print(hero.weapon)
            
            # quit game
            elif action == "4":
                quit()

if __name__ == "__main__":
    Game()
