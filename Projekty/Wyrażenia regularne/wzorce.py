import re

wzorce = [["kot", 'kot'], # 0
          ['ko.', 'kot'], #Maj2021 . - dowolny znak
          ['^gulas.', 'gulasv'],#2 ^ - musi sie zaczynac od tego znaku
          ['^rok$', 'kot'],#3 $ - musi sie konczyc tym znakiem
          ['^[KkRr]ok$', 'Rok'],#4 [] - klasa znaków, musi być jedno dopasowanie
          ['^[A-za-z]o.$', 'sol'],#5 [A-za-z] - przedziały liter w alfabecie, tak samo z liczbami
          ]


i = 0
for wzor in wzorce:
    print("nr: ", i)
    if re.match(wzor[0], wzor[1]):
        print("Dopasowano\n")
        i += 1
    else:
        print("Nie dopasowano\n")
        i += 1


if re.match("^[A-Z][a-z][-_>][0-9][0-9][0-9][0-9].$", "Ja-2003["):
    print("Poprawny wzorzec")
else:
    print("Niepoprawny wzorzec")