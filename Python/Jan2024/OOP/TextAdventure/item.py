class Item:
    def __init__(self, name, weapon_type, value, desc):
        self.name = name
        self.weapon_type = weapon_type
        self.value = value
        self.desc = desc

# create a weapon for characters to use
class Weapon(Item):
    def __init__(self, name: str, weapon_type: str, damage: int, value: int, desc: str):
        super().__init__(name=name, weapon_type=weapon_type, value=value, desc=desc)

        self.damage = damage
    
    def __str__(self):
        return f"{self.name}: {self.weapon_type} weapon that deals {self.damage} damage and is worth {self.value} gold. {self.desc}"


class Medicine(Item):
    def __init__(self, name: str, weapon_type: str, value: int, desc: str, hpRecover):
        super().__init__(name=name, weapon_type=weapon_type, value=value, desc=desc)

        self.hpRecover = hpRecover
    
    def __str__(self):
        return f"{self.name}: {self.weapon_type} Medicine that heals {self.hpRecover} health and is worth {self.value} gold. {self.desc}"

# Medicines
smallMed = Medicine(name="Small Med", weapon_type="support", hpRecover=5, value=10,desc="Those over-the-counter presecriptions that have been modified to regain health.")
mediumMed = Medicine(name="Medium Med", weapon_type="support", hpRecover=20, value=20, desc="For those times when you aren't that guy.")
largeMed = Medicine(name="Large Med", weapon_type="support", hpRecover=50, value=40, desc="Tis but a scratch")

# Weapons
nuke = Weapon(name="An Actual Nuke", weapon_type="ranged", damage=1000, value=999, desc="My best friend :>.")
iron_sword = Weapon(name="Iron Sword", weapon_type="melee", damage=15, value=50, desc="The standard for medieval battles.")
short_bow = Weapon(name="Short Bow", weapon_type="ranged", damage=5, value=20, desc="For when you don't like social contact.")
fists = Weapon(name="Fists", weapon_type="melee", damage=2, value=0, desc="For getting all personal.")