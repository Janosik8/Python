dane = [1, 2, 3, 5, 25, 45, 70, 56, 17, 49, 41, 101]

ex = map(lambda x: x/2, dane)

def multiply(x):
    return x*2

ex2 = map(multiply, dane)

print("\nex1: ")
print(list(ex))
print("\nex2: ")
print(list(ex2))

ex3 = list(filter(lambda x: x % 2 == 0, dane))

print("\nex3: ")
print(ex3)
from math import sqrt
from math import floor

def is_prime(x):
    if x < 2:
        return  False
    for i in range(2,floor(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

ex4 = filter(is_prime, dane)

print("\n ex4: ", list(ex4))


