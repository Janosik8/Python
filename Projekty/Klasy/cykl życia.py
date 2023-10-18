class Test:
    def __del__(self):
        print("Hello, its mi")

obj = Test()
obj2 = obj
del obj
lista = [obj2]
del obj2
print("Koniec wykonywania")