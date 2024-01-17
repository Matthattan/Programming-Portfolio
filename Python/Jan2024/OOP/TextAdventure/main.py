import os

# import character class
from character import Hero, Enemy
from weapon import short_bow, iron_sword

# create instances from character
hero = Hero(name="hero", health=100)
hero.equip(iron_sword)
enemy = Enemy(name="Enemy", health=100, weapon=short_bow)

print(f"{enemy.name} was encountered!")

while enemy.health > 0:
    os.system("cls")

    hero.attack(enemy)
    enemy.attack(hero)

    hero.health_bar.draw()
    enemy.health_bar.draw()

    input()

print(f"{enemy.name} was defeated!")
