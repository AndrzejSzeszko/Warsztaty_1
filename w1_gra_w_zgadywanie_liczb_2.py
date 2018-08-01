#!/usr/bin/python3.7


def guess_2():
    print('Pomyśl liczbę od 0 do 1000 a ja zgadnę w maksymalnie dziesięciu próbach.')
    try_counter, d_counter, m_counter = 0, 0, 0
    minimum, maximum = 0, 1001

    while try_counter < 10:
        guess = int((maximum - minimum) / 2) + minimum
        print(f'Zgaduję: {guess} (to jest {try_counter + 1}. próba)')
        hint = input('Zgadłem? Wybierz wskazówkę z poniższego zestawu: \n'
                     'd - za dużo \n'
                     'm - za mało \n'
                     'z - zgadłeś \n')
        if hint == 'd':
            maximum = guess
            try_counter += 1
            d_counter += 1
            continue
        elif hint == 'm':
            minimum = guess
            try_counter +=1
            m_counter += 1
            continue
        elif hint == 'z':
            print('Wygrałem!')
        else:
            print('Oszuście! Nie podałeś wskazówki z podanego wyżej zestawu (m/d/z). '
                  'Spróbuj ponownownie.')
            continue

    if d_counter == 10 or m_counter == 10:
        print('Oszukałeś!')


guess_2()
