from random import choice

from attack import Attack


class Monster:
    def __init__(self, name, strength, defence, life, attack, loot=None):
        self.name = name
        self.strength = strength
        self.defence = defence
        self.life = life
        self.attack = attack
        self.loot = loot

    def __str__(self):
        return self.name + " a " + str(self.life) + " points de vie"

    def create_dragon():
        attacks = [Attack("Coup de griffe", 8, 10), Attack("Crache des flammes", 5, 20), Attack("Coup de patte", 9, 5)]
        return Monster("Dragon", 100, 50, 200, attacks)

    def choose_attack(self):
        return choice(self.attack)

    def damage(self, damage):
        damage -= self.defence
        if damage > 0:
            self.life -= damage
