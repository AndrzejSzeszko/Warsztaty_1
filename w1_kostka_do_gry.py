#!/usr/bin/python3.7
from re import match
from random import randint


def dice(input_string):
    allowed_dice_types = [3, 4, 6, 10, 12, 20, 100]
    dice_throw_pattern = r'(\d*)D(' + '|'.join(str(_) for _ in allowed_dice_types) + r')([+-]\d+)?$'
    try:
        elements = match(dice_throw_pattern, input_string).groups()
        elements_int = [int(_) if (_ != '' and _ is not None) else (1 if _ == '' else 0) for _ in elements]
        no_of_throws = elements_int[0]
        dice_type = elements_int[1]
        modifier = elements_int[2]
        return sum(randint(1, dice_type) for _ in range(no_of_throws)) + modifier
    except AttributeError:
        print('The string you have provided does not fit the valid dice throw pattern!')


test_throw1 = '2D10+10'
result1 = dice(test_throw1)
assert 12 <= result1 <= 30
print(result1)

test_throw2 = 'D6'
result2 = dice(test_throw2)
assert 1 <= result2 <= 6
print(result2)

test_throw3 = '2D3'
result3 = dice(test_throw3)
assert 2 <= result3 <= 6
print(result3)

test_throw4 = 'D12-1'
result4 = dice(test_throw4)
assert 0 <= result4 <= 11
print(result4)

test_throw5 = 'ofnweonv'
dice(test_throw5)
