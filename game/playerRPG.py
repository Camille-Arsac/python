from enum import Enum
from attack import Attack
from potion import PotionEffect


class PlayerRPG:
    def __init__(self, rpg_type):
        self.life = 100
        self.inventory = []
        self.rpg_type = rpg_type
        if rpg_type == RPGType.warrior:
            self.strength = 10
            self.defence = 5
            self.attack = [Attack("coup d'épée horizontal", 7, 15), Attack("coup d'épée vertical", 6, 20)]
        elif rpg_type == RPGType.mage:
            self.strength = 5
            self.defence = 3
            self.attack = [Attack("sort puissant", 3, 50), Attack('sort rapide', 8, 20)]

    def open_inventory(self):
        for i in range(0, len(self.inventory), 1):
            print(i, " : ", self.inventory[i])

    def drink_potion(self, id_inventory):
        if self.inventory[id_inventory].effect == PotionEffect.heal:
            self.life += self.inventory[id_inventory].power
        elif self.inventory[id_inventory].effect == PotionEffect.strength:
            self.life += self.inventory[id_inventory].power
        elif self.inventory[id_inventory].effect == PotionEffect.defence:
            self.defence += self.inventory[id_inventory].power
        self.inventory.pop(id_inventory)

    def attack(self):
        return self.attack


class RPGType(Enum):
    warrior = 1
    mage = 2
