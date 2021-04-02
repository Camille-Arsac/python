from attack import Attack


class Monster:
    def __init__(self, name):
        self.name = name
        self.force = 50
        self.defence = 50
        self.life = 100
        self.attack = [Attack("coup de griffe", 8, 10), Attack("morsure", 5, 20), Attack("coup de patte", 9, 10)]

    def attack(self):
        return self.attack
