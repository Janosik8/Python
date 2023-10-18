from math import sqrt

class Punkt2d:
    def __init__(self,x, y):
        self.x = x
        self.y = y
        self.odleglosc = int(sqrt(x**2 + y**2))

    def __add__(self, other):
        return self.odleglosc + other.odleglosc

    def __bool__(self):
        if self.odleglosc > 0:
            return True
        else:
            return False

    def __pow__(self, power):
        return self.odleglosc**power



punkt1 = Punkt2d(5, 3)
punkt2 = Punkt2d(0, 0)

print(punkt2.odleglosc)
print(punkt1.odleglosc)

print(punkt1 + punkt2)


if punkt2:
    print("tak")
else:
    print("nie")

print(pow(punkt1, 3))