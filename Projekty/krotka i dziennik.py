dic = {1: 'poniedzialek', 2: 'wtorek', 7: 'niedziela'}

print(dic)

print(dic[1])

dic[3] = 'środa'
dic[4] = 'czwartek'

print(dic)

for z in dic:
    print(dic[z])


print(dic[2][::-1])


krotka = (1, 2, 4, 8, 16, 32, 64, 128)

print(krotka)

print(krotka[0])

print(krotka.index(2))
print("\n")

print(krotka[::2])

s = 0
for d in dic.keys():
    if s % 2 == 0:
        print(d, ' : ', dic[d])
    s += 1



