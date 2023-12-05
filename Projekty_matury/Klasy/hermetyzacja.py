class Test1:
    _lista = []

    def dodaj(self, liczba):
        return self._lista.append(liczba)

    def kasuj(self):
        if len(self._lista) > 0:
            return self._lista.pop(len(self._lista) - 1)

obj = Test1()
obj.dodaj("A")
obj.dodaj("B")
obj._lista.append("Z")
obj.dodaj("C")

print(obj.kasuj())

obj.dodaj("X")

print(obj._lista)

print("---------------------------------------------")
class Test2():
    __lista = []

    def dodaj(self, liczba):
        return self.__lista.append(liczba)

    def kasuj(self):
        if len(self.__lista) > 0:
            return self.__lista.pop(len(self.__lista) - 1)

obj2 = Test2()

obj2.dodaj('G')
obj2.dodaj('D')
obj2.dodaj('F')

print(obj2.kasuj())


print(obj2._Test2__lista)





