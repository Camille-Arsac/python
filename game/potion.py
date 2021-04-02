from enum import Enum


class Potion:
    def __init__(self, name, effect, power):
        self.name = name
        self.effect = effect
        self.power = power

    def __str__(self):
        return self.name


class PotionEffect(Enum):
    heal = 1
    strength = 2
    defence = 3
