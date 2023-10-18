plik = open("dane.txt", 'r')
tekst = plik.read()
plik.close()

print(tekst)


print('-----------------------------')

lista = []

from random import randint
for i in range(20):
    lista.append(randint(0,100))

print(lista)

if any([a % 2 == 0 for a in lista]):
    print('Chociaz jedna parzysta')

if all([a % 2 == 0 for a in lista]):
    print("Wszystkie są parzyste")


for i in enumerate(lista):
    print(i[0]+1, "-",i[1])



def policz(txt, znak):
    licznik = 0
    for i in txt:
        if i == znak:
            licznik += 1
    return licznik

print(policz(tekst.lower(), 'a'))

for z in 'abcdefghijklmnopqrstuwxyz':
    ile = policz(tekst.lower(), z)
    procent = 100 * ile/len(tekst)
    print('{0} - {1} - {2}%'.format(z.upper(), ile, round(procent, 2)))

    






    


