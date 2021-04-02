from dog import Dog

dog1 = Dog("Carpette", 3, ["Yvette"], ["assie", "couché", "donne la patte"])
dog2 = Dog("Chiffon", 8, ["Jean", "Jeannette"], ["assie", "reviens", "couché"])
print(dog1.same_trick(dog2))
dog1.learn('reviens')
print(dog1.same_trick(dog2))
