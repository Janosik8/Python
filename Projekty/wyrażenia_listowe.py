
lista = list(range(10))
print(lista)

ex = [i + 1 for i in lista]
print(ex)

ex2 = [i + 2 for i in lista]
print(ex2)

ex3 = [i for i in lista if i % 2 == 0]
print(ex3)

szablon = ["Janek", 19]

tekst = "Cześć, mam na imię: {0}, i mam {1} lat! :)".format(szablon[0],szablon[1])

print(tekst)

print(len(tekst))