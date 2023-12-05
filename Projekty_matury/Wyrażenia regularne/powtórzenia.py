import re

wzorce = [['^[A-Z][a-z]*$', "Aleksandra"], # nr 0 : * - moze sie powtarzac, nie musi wystąpić ostatni znak
          ['^[A-z][a-z]+$', "Aleksandra"], # nr2: + - musi przynajmniej raz wystąpić znak przed
          ['^[A-z][a-z]?$', 'Ala'],#nr3: ? - dokladnie jedno wystąpienie znaku przed
          ['^[A-z][a-z]{,5}$', 'Janeczek']#nr4: {Maj2021, 2} min Maj2021 wystąpienie, max 2
          ]



i = 0
for wzorzec in wzorce:
    print('nr: ', i)
    if re.match(wzorzec[0], wzorzec[1]):
        print("Dopasowano\n")
    else:
        print("Nie dopasowano!\n")

    i += 1
