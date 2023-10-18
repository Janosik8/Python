plik = open('instrukcje.txt')
wiersze = plik.readlines()
plik.close()
wiersze = [i.strip().split(" ") for i in wiersze]
#print(wiersze)
slowo = []
alfabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K','L','M','N','O','P','Q','R','S','T','U','V', 'W','X','Y','Z']
#kreowanie słowa:
for wiersz in wiersze:
    if wiersz[0] == 'DOPISZ':
        slowo.append(wiersz[1])
        #print(slowo, '\n')
    elif wiersz[0] == 'USUN':
        slowo.pop(len(slowo)-1)
        #print(slowo, '\n')
    elif wiersz[0] == 'ZMIEN':
         slowo[len(slowo)-1] = wiersz[1]
         #print(slowo, '\n')
    elif wiersz[0] == 'PRZESUN':
        for i in range(0, len(slowo)):
            if slowo[i] == wiersz[1] and wiersz[1] != 'Z':
                for j in range(0, len(alfabet)):
                    if alfabet[j] == wiersz[1]:
                        slowo[i] = alfabet[j+1]
                        break
                break
            elif slowo[i] == wiersz[1] and wiersz[1] == 'Z':
                slowo[i] = 'A'
                break
        print(slowo, '\n')


#ODP 4.1

print("Odpowiedz do 4.1: ", len(slowo))

#4.2
rodzaje = [0,0,0,0]
#1 dodaj 2: usun, 3:zmien, 4:przesun
d = wiersze[0][0]
licznik = 0
for wiersz in wiersze:
    if wiersz[0] == d:
        licznik += 1
    else:
        if d == 'DOPISZ':
            if rodzaje[0] < licznik:
                rodzaje[0] = licznik
        elif d == 'USUN':
            if rodzaje[1] < licznik:
                rodzaje[1] = licznik
        elif d == 'ZMIEN':
            if rodzaje[2] < licznik:
                rodzaje[2] = licznik
        elif d == 'PRZESUN':
            if rodzaje[3] < licznik:
                rodzaje[3] = licznik
        d = wiersz[0]
        licznik = 1

max = max(rodzaje)

if rodzaje[0] == max:
    print("Odpowiedz do 4.2: DOPISZ: ", max)
elif rodzaje[1] == max:
    print("Odpowiedz do 4.2: USUN: ", max)
elif rodzaje[2] == max:
    print("Odpowiedz do 4.2: ZMIEN: ", max)
elif rodzaje[3] == max:
    print("Odpowiedz do 4.2: PRZESUN: ", max)

#4.3

leters = {}
li = 0
for wiersz in wiersze:
    if wiersz[0] == 'DOPISZ':
        for i in leters.keys():
            if i == wiersz[1]:
                li += 1
        if li < 1:
            leters[wiersz[1]] = 1
        else: leters[wiersz[1]] += 1
        li = 0
        
max = -1
for i in leters.values():
    if i > max:
        max = i

for j in leters:
    if leters[j] == max:
        print('Odpowiedź do 4.3: ', j, ': ', max)



#4.4

slowo = "".join(slowo)
print('Odpowiedz do 4.4: ', slowo)






