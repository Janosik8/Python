def funckaj(f, liczba):
    return f(liczba)

print(funckaj(lambda x: x*x, 2))

wyn = (lambda x: x*x)(5)

print(wyn)

lam = lambda x: x*x

print(lam)
print(lam(5))

lam2 = lambda x,y: x*y

print(lam2(5,5))


