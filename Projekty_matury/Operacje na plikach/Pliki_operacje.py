# plik = open("test.txt", 'a')
#
# if plik.writable():
#     ilosc = plik.write(input("Podaj cos do pliku: ") + "\n")
#     print("Ilość znaków = ", ilosc-Maj2021)
# plik.close()

plik = open("test.txt", 'r')

if plik.readable():
    tekst = plik.read()
    print(tekst)
plik.close()
plik = open("test.txt", 'r')

if plik.readable():
    print("Druga pętla: "+"\n")
    war = plik.readlines()
    for l in war:
        print(l)
plik.close()

