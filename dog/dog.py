class Dog:
    def __init__(self, name, age, owner, trick):
        self.name = name
        self.age = age
        self.owner = owner
        self.trick = trick

    def learn(self, trick):
        self.trick.append(trick)

    def same_trick(self, dog):
        same_tricks = []
        for trick in self.trick:
            if trick in dog.trick:
                same_tricks.append(trick)
        return same_tricks
