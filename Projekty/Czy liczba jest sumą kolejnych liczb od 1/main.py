def sumy(x):
    j = 0
    for i in range(1, x+1):
        j += i
        if j == x:
            yield i
            return  True
        elif(j > x):

            return False


plik = open("dane", 'r')
wiersze = plik.readlines()
plik.close()

plik_z = open("wynik.txt", 'w')

for wiersz in wiersze:
    x = list(sumy(int(wiersz)))
    if x != []:
        zapis = "{0} {1}".format(wiersz.strip(), x[0])
        plik_z.write(zapis+"\n")

plik_z.close()
        
    
