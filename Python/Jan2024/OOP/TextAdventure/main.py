import os
import random

# import character class
from character import Hero, Enemy
from weapon import short_bow, iron_sword, nuke

# create instances from character
hero = Hero(name="hero", health=100)
hero.equip(iron_sword)
enemy = Enemy(name="Enemy", health=100, weapon=short_bow)

print(f"{enemy.name} was encountered!")

# Player Idle
while True:
    action = input("What would you like to do \n 1 - Encounter \n 2 - Check Weapon \n 3 - Quit \n")

    # Encounter
    if action == "1":
        while True:
            # get odds
            encounterRate = random.randint(1,128)

            if encounterRate == random.randint(1,128):
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
                    break

                elif hero.health <= 0:
                    print(f"{hero.name} was defeated!")
                    break

            elif encounterRate == random.randint(1,256):
                print(f"{hero.name} picked up a {nuke.name}")
                hero.equip(nuke)
                break

    # check weapon            
    elif action == "2":
        print(hero.weapon)
    
    # quit game
    elif action == "3":
        quit()