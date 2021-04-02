def print_list(list_print):
    for i in range(0, len(list_print), 1):
        print(i, " : ", list_print[i])


def choose_item(item):
    print_list(item)
    print("Choississez une option suivante : ")
    user_choice = int(input())
    while user_choice < 0 or user_choice >= len(item):
        user_choice = int(input())
    return item[user_choice]

