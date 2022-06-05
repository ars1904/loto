import numpy as np
import random

def separators_my(f):
    def inner(numbers):
        print('-'*3,'Ваша карточка','-'*3)
        result=f(numbers)
        print('-' * 18)
        return result
    return inner

def separators_comp(f):
    def inner(numbers):
        print('-'*2,'Карточка компьютера','-'*2)
        result=f(numbers)
        print('-' * 20)
        return result
    return inner


@separators_my
def print_mycard(numbers):
    print(numbers[:5])
    print(numbers[5:10])
    print(numbers[10:])

@separators_comp
def print_compcard(numbers):
    print(numbers[:5])
    print(numbers[5:10])
    print(numbers[10:])
