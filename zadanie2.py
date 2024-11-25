#ZADANIE 2

liczby = input('Podaj pięć liczb całkowitych dodatnich rozdzielonych spacjami:')
lista_liczb = [int(s) for s in liczby.split()]
print(lista_liczb)
print(f'Najmniejsza liczba na liście to: {min(lista_liczb)}')