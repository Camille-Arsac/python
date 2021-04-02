from enum import Enum

from attack import Attack
from utils import print_list
from potion import PotionEffect


class PlayerRPG:
    def __init__(self, rpg_type):
        self.life = 100
        self.inventory = []
        self.rpg_type = rpg_type
        self.attack = []
        if rpg_type == RPGType.warrior:
            self.strength = 10
            self.defence = 5
            self.attack.append(Attack("Coup de bouclier", 7, 15))
            self.attack.append(Attack("Coup d'épée", 6, 20))
        elif rpg_type == RPGType.mage:
            self.strength = 5
            self.defence = 3
            self.attack.append(Attack("Eclair", 3, 50))
            self.attack.append(Attack("Boule de feu", 8, 20))

    def choose_attack(self):
        print_list(self.attack)
        print("Choississez une attaque : ")
        user_choice = int(input())
        while user_choice < 0 or user_choice >= len(self.attack):
            user_choice = int(input())
        return self.attack[user_choice]

    def drink_potion(self, id_inventory):
        if self.inventory[id_inventory].effect == PotionEffect.heal:
            self.life += self.inventory[id_inventory].power
        elif self.inventory[id_inventory].effect == PotionEffect.strength:
            self.life += self.inventory[id_inventory].power
        elif self.inventory[id_inventory].effect == PotionEffect.defence:
            self.defence += self.inventory[id_inventory].power
        self.inventory.pop(id_inventory)


class RPGType(Enum):
    warrior = 1
    mage = 2
