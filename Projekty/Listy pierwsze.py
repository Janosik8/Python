lista = []
licznik = 0
n = int(input("Podaj liczbę elementów: "))

while licznik<n:
    lista.append(int(input("Podaj liczbę: ")))
    licznik += 1


while True:
    akcja = input("Co robić? (max = szukanie maksa, min - szukanie mina, "
                  "sort - sortowanie tablicy, zlicz - zlicza ilosc elementów,"
                  " index - podaje indeks elementu, reverse - odwrócenie listy): ")
    if akcja == 'max':
        print(max(lista))
    elif akcja == 'min':
        print(min(lista))
    elif akcja == 'sort':
        lista.sort()
        print(lista)
        break
    elif akcja == 'zlicz':
        print(len(lista))
    elif akcja == 'index':
       print(lista.index(int(input("Podaj liczbę: "))))
    elif akcja == 'reverse':
        lista.reverse()
        print(lista)
        break
    