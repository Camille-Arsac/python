from random import randint


class Attack:
    def __init__(self, name, lucky, damage):
        self.name = name
        self.lucky = lucky
        self.damage = damage

    def __str__(self):
        return self.name

    def hit(self):
        return randint(0, 10) < self.lucky
