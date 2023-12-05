def func(x):
    return x * x

zmienna = func

print(zmienna(4))

def func1(f1, x):
    return f1(x) * x

print(func1(func,2))

def silnia(x):
    if x <= 1:
        return 1
    else:
        return x * silnia(x - 1)

print(silnia(9))

