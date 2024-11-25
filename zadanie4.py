#zadanie 4


plik = open('tekst.txt', 'r', encoding='utf-8')

zawartosc = plik.read()
slowa = zawartosc.split()
liczba_slow = len(slowa)

znaki_do_usuniecia =['.', ',', '!', '?', ':', ';', '-', '\\', ' ']

for znak in znaki_do_usuniecia:
    zawartosc = zawartosc.replace(znak, "")

liczba_liter = len(zawartosc)

print(f'Śrerdnia liczba liter na słowo: {round(liczba_liter / liczba_slow)}')