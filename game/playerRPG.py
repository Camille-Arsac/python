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

    def __str__(self):
        return "Vous avez " + str(self.life) + " points de vie"

    def drink_potion(self, potion):
        if potion.effect == PotionEffect.heal:
            self.life += self.potion.power
        elif potion.effect == PotionEffect.strength:
            self.life += potion.power
        elif potion.effect == PotionEffect.defence:
            self.defence += potion.power
        self.inventory.remove(potion)

    def damage(self, damage):
        damage -= self.defence
        if damage > 0:
            self.life -= damage


class RPGType(Enum):
    warrior = 1
    mage = 2
