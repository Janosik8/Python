x = 12
y = 2
lista = [1]
try:
    print(x/y)
    print(x + 1)
    print(lista[0])
except (ZeroDivisionError, TypeError):
    print("Wystąpił Błąd!")
except:
    print("Wystąpił nieznany błąd!")
finally:
    print("No siema!")
