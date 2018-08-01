#!/usr/bin/python3.7
from random import sample


def lotto():

    class OutOfRangeError(Exception):
        pass

    class RepeatedNumberError(Exception):
        pass

    winning_numbers = sample(range(1, 49), 6)
    numerals = ('pierwszą', 'drugą', 'trzecią', 'czwartą', 'piątą', 'szóstą')
    print('Podaj sześć liczb naturalnych z przedziału 1-49: ')

    numbers = []
    while len(numbers) < 6:
        try:
            number = int(input(f'Podaj {numerals[len(numbers)]} liczbę:' ))
            if number not in range(1, 50):
                raise OutOfRangeError
            if number in numbers:
                raise RepeatedNumberError
            numbers.append(number)
        except ValueError:
            print('Nie podałeś liczby naturalnej! Spróbuj jeszcze raz!')
            continue
        except OutOfRangeError:
            print('Podana liczba nie znajduje się w przedziale 1-49! Spróbuj jeszcze raz!')
            continue
        except RepeatedNumberError:
            print('Tę liczba podałeś już wcześniej! Spróbuj jeszcze raz!')
            continue

    numbers.sort()
    winning_numbers.sort()
    print('Oto liczby które wybrałeś: ', numbers)
    print('Oto wylosowane liczby: ', winning_numbers)

    matches = [_ for _ in numbers if _ in winning_numbers]

    if len(matches) < 3:
        print('Niestety nie trafiłeś nawet "trójki".')
    else:
        print('Trafiłeś co najmniej "trójkę"!')


lotto()
