#ZADANIE 1
a = int(input('Podaj liczbę całkowitą: '))

if a % 2 != 0 and a % 3 == 0:
    print('Liczba jest nieparzysta i podzielna przez 3.')
else:
    print('Liczba nie spełnia kryteriów.')