import random
from class_card import card
from func_loto import *


def close():
    while True:
        choice_1 = input('Зачеркнуть цифру? y/n')
        if choice_1 == 'y':
            if bochonok in my_card.numbers:
                for i, n in enumerate(my_card.numbers):
                    if n == bochonok:
                        my_card.numbers[i] = '-'
                        return my_card.numbers
            else:
                print('Вы проиграли')
                break
        elif choice_1 == 'n':
            if bochonok in my_card.numbers:
                print('Вы проиграли')
                break
            else:
                continue
        else:
            print('Введите правильный символ')
    return my_card.numbers

while True:
    print('1. Игра с компьютером')
    print('2. Выход')

    choice=int(input('Выберите пункт '))
    list_boch=list(range(1,91)) #список всех бочонков
    my_card=card() #карточка игрока
    comp_card=card() #карточка компьютера
    if choice==1:
        while True:
            bochonok=random.choice(list_boch)
            list_boch.remove(bochonok)
            print(f"Новый бочонок: {bochonok} (осталось {len(list_boch)})")
            print_mycard(my_card.numbers)
            print_compcard(comp_card.numbers)
            choice_1 = input('Зачеркнуть цифру? y/n')
            if choice_1 == 'y':
                if bochonok in my_card.numbers:
                    for i, n in enumerate(my_card.numbers):
                        if n == bochonok:
                            my_card.numbers[i] = '-'
                            break
                else:
                    print('Вы проиграли')
                    break
            elif choice_1 == 'n':
                if bochonok in my_card.numbers:
                    print('Вы проиграли')
                    break
                else:
                    continue
            if bochonok in comp_card.numbers:
                for i, n in enumerate(comp_card.numbers):
                    if n == bochonok:
                        comp_card.numbers[i] = '-'
            if all(x=='-' for x in comp_card.numbers):
                print('Победа компьютера')
                break
            if all(x=='-' for x in my_card.numbers):
                print('Вы победили')
                break

    elif choice == 2:
        break









