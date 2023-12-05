plik = open("pary.txt", 'r')
wiersze = plik.readlines()
plik.close()
wiersze = [i.strip().split(" ") for i in wiersze]
for i in wiersze:
    i[0] = int(i[0])


def czy_pierwsza(x):
    n = 2
    if x == 2:
        return True
    if x % 2 != 0:
        while n <= x / 2:
            if x % n == 0:
                return False
            n += 1
        return True

    else:
        return False


print(wiersze)


def zad_1(wiersze):
    odp = []
    for wiersz in wiersze:
        x = wiersz[0]
        if x % 2 == 0:
            for i in range(2, x):
                if czy_pierwsza(i) and czy_pierwsza(x - i):
                    odp.append([x, i, x - i])
                    break
    return odp


for o in zad_1(wiersze):
    print(o[0], o[1], o[2])


# zad2:
def zad_2(wiersze):
    tab = []
    for wiersz in wiersze:
        txt = wiersz[1]
        poprzedni = txt[len(txt) - 1]
        max1 = 0
        max_max = 0
        max_litera = ''
        for i in range(0, len(txt)):
            if txt[i] == poprzedni:
                max1 += 1
                continue
            else:
                if max1 > max_max:
                    max_max = max1
                    max_litera = txt[i - 1]
            poprzedni = txt[i]
            max1 = 1

        wyn = []
        for i in range(0, max_max):
            wyn.append(max_litera)
        wyn = ''.join(wyn)

        tab.append([wyn, max_max])
    return tab


for i in zad_2(wiersze):
    print(i[0], i[1])

# 4.3
def zad_3(wiersze):
    min_slowo = wiersze[0][1]
    min_liczba = wiersze[0][0]
    for wiersz in wiersze:
        slowo = wiersz[1]
        liczba = wiersz[0]
        if liczba == len(slowo):
            if liczba < min_liczba or (liczba == min_liczba and slowo < min_slowo):
                min_slowo = slowo
                min_liczba = liczba
    return min_slowo, min_liczba

print(zad_3(wiersze))


