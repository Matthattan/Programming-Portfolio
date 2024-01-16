# import character class
from character import Hero, Enemy
from weapon import short_bow, iron_sword

# create instances from character
hero = Hero(name="hero", health=100)
hero.equip(iron_sword)
enemy = Enemy(name="Enemy", health=100, weapon=short_bow)

while hero.health > 0:
    hero.attack(enemy)
    enemy.attack(hero)

