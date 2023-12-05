plik = open("liczby.txt")
wiersze = plik.readlines()
plik.close()

licznik = 0
pierwsza = -1

print('zadanie 4.Maj2021: ')
for wiersz in wiersze:
    wiersz = wiersz.strip()
    if wiersz[0] == wiersz[-1]:
        licznik += 1
        if pierwsza == -1:
            pierwsza  = wiersz
print("\n", licznik, pierwsza)

#zadanie 4.2:
print("\nzadanie 4.2: ")

#420 = 2 * 2 * 3 * 5 * 7
#      210 + 105 + 35 + 7

wiersze = [int(i) for i in wiersze]

def rozklad(x):
    t_c = []
    czynnik = 2
    while(x > 1):
        while(x % czynnik == 0):
            t_c.append(czynnik)
            x /= czynnik
        czynnik += 1

    if x != 1:
        t_c.append(x)
    return t_c

max_czyn = -1
max = -1

max_r_czyn = -1
max_r = -1

for wiersz in wiersze:
    czynniki_i = rozklad(wiersz)
    if(max_czyn < len(czynniki_i)):
        max = wiersz
        max_czyn = len(czynniki_i)

    r_czyn = set(czynniki_i)
    if(len(r_czyn) > max_r_czyn):
        max_r_czyn = len(r_czyn)
        max_r = wiersz

print("\n", max, max_czyn, max_r, max_r_czyn)

#zadanie 4.3
print("\nzadanie 4.3: ")
plik_trk = open("trójki.txt", 'w')
licznik_dobrych_trujek = 0

for wiersz in wiersze:
    for wiersz1 in wiersze:

        if wiersz1 == wiersz or wiersz1 % wiersz != 0:
            continue

        for wiersz2 in wiersze:
            if wiersz2 == wiersz1 or wiersz2 == wiersz or wiersz2 % wiersz1 != 0:
                continue
            else:
                licznik_dobrych_trujek += 1
                zapis = "{0} {1} {2}".format(wiersz, wiersz1, wiersz2)
                plik_trk.write(zapis+"\n")

# dobre piątki:
licznik_dobrych_piatek = 0

for wiersz in wiersze:
    for wiersz1 in wiersze:

        if wiersz1 == wiersz or wiersz1 % wiersz != 0:
            continue

        for wiersz2 in wiersze:
            if wiersz2 == wiersz1 or wiersz2 == wiersz or wiersz2 % wiersz1 != 0:
                continue
            for wiersz3 in wiersze:
                if wiersz2 == wiersz1 or wiersz2 == wiersz or wiersz3 % wiersz2 != 0 or wiersz3 == wiersz2:
                    continue
                for wiersz4 in wiersze:
                    if wiersz2 == wiersz1 or wiersz2 == wiersz or wiersz4 % wiersz3 != 0 or wiersz4 == wiersz3:
                        continue
                    else:
                        licznik_dobrych_piatek += 1



print("\n", licznik_dobrych_trujek, licznik_dobrych_piatek)