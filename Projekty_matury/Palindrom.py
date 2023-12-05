lista = []
x = int(input("Podaj liczbę elemętów: "))

for n in range(0,x):
    lista.append(input("Podaj liczbę: "))


n = 0

while n < len(lista):
    z = lista[n]
    if z[::-1] == z:
        print('Słowo numer: ', n+1, " to Palindrom")
    n += 1

