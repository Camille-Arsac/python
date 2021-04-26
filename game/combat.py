from utils import choose_item


def combat(player, monster):
    print(player)
    print("VS")
    print(monster)

    while player.life > 0 and monster.life > 0:
        print(player)
        print("VS")
        print(monster)
        print("Que voulez vous faire ?")
        print("1 : Attaquer")
        print("2 : Boire une potion")
        print("3 : Rien du tout")
        user_choice = int(input())
        if user_choice == 1:
            attack = choose_item(player.attack)
            if attack.hit():
                monster.damage(attack.damage)
        elif user_choice == 2:
            potion = choose_item(player.inventory)
            player.drink_potion(potion)

        attack = monster.choose_attack()
        if attack.hit():
            player.damage(attack.damage)

    print("Fin du combat !")
    print(player)
    print("VS")
    print(monster)

