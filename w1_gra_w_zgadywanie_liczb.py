#!/usr/bin/python3.7
from random import randint


def guess_1():
    correct_number = randint(1, 100)
    while True:
        given_number = int(input('Zgadnij liczbę: '))
        if given_number < correct_number:
            print('Za mało!')
            continue
        elif given_number > correct_number:
            print('Za dużo!')
            continue
        else:
            print('Zgadłeś')
            break


guess_1()
