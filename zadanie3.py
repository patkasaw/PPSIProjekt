#ZADANIE 3
print('Podaj dwie liczby:')

try:
    a, b = float(input('a')), float(input('b'))
    wynik = a / b
    print(f'Wynik dzielenia {a} przez {b} wynosi {wynik}')
    
except ZeroDivisionError:
    print('Nie można dzielić przez zero.')
    
except ValueError:
    print('Niepoprawne dane wejściowe, podaj liczby')

finally:
    print('Operacja zakończona')
