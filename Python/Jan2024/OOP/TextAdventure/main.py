import os
import random

# import character class
from character import Hero, Enemy
from item import short_bow, iron_sword, nuke, smallMed, mediumMed, largeMed
from item import Weapon, Medicine

# create instances from character
hero = Hero(name="hero", health=100, coins=100, inventory=[smallMed, smallMed, short_bow])
hero.equip(iron_sword)
enemy = Enemy(name="Enemy", health=100, weapon=short_bow)

print(f"{enemy.name} was encountered!")

class Game:
    def __init__(self):

        # Player Idle
        while True:
            action = input("What would you like to do \n 1 - Encounter \n 2 - Check Inventory \n 3 - Check Weapon \n 4 - Check Coins \n q - Quit \n")

            # Encounter
            if action == "1":

                # get odds
                encounterRate = random.randint(0,101)
                nukeRate = [1, 21, 41, 61, 81, 99]
                coinRate = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
                enemyRate = [2, 15, 32, 45, 62, 75, 91, 98]

                if encounterRate in enemyRate:
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

                elif encounterRate in nukeRate and hero.weapon != nuke:
                    hero.equip(nuke)
                    print(f"{hero.name} picked up a {nuke.name}")

                elif encounterRate in coinRate:
                    hero.coins += encounterRate
                    print(f"{hero.name} picked up {encounterRate} Coins")

                else:
                    print("Nothing Found!")

            # access inventory
            elif action == "2":

                # Allow player to look at each ind. item
                while True:
                    hero.viewInv()
                    action = input("Input Index (Starting from 1) to look at an item - use e to exit \n")

                    if action == "e":
                        break

                    try:
                        # turn index into item
                        selectedItem  = hero.inventory[int(action)-1]
                        print(selectedItem)

                        while True:
                            # interact with item
                            action = input("What would you like to do with the item? \n"
                                           "1 - View Description \n"
                                           "2 - Use Item \n"
                                           "3 - Sell  \n"
                                           "q - Exit \n")
                            
                            if action == "1":
                                print(selectedItem)
                            
                            if action == "2":
                                # check if item is Med or Weapon
                                if type(selectedItem) is Medicine:
                                    hero.health += selectedItem.hpRecover

                                    if hero.health > hero.health_max:
                                        hero.health = hero.health_max

                                elif type(selectedItem) is Weapon:
                                        hero.equip(selectedItem)
                                else:
                                    print("error")

                                break
                            
                            if action == "3":
                        
                                action = input(f"Sell {selectedItem.name} for {selectedItem.value} coins? Y/N \n")

                                if action.upper() == "Y":
                                    hero.coins += selectedItem.value
                                    hero.inventory.remove(selectedItem)
                                    break
                                elif action.upper() == "N":
                                    continue

                            if action == "q":
                                break
                    except IndexError:
                        print("Invalid Index")

            # check weapon            
            elif action == "3":
                print(hero.weapon)

            # check coins
            elif action == "4":
                hero.checkCoins()
            
            # quit game
            elif action == "q":
                quit()
            
            else:
                print("Invalid Option")

if __name__ == "__main__":
    Game()