class Czlowiek:
    def __init__(self, imie, przywitanie):
        self.imie = imie
        self.przywitanie = przywitanie

    def przywitaj_sie(self):
        return 'Cześć, jestem człowiekiem'

    @classmethod
    def nowy_Czlowiek(cls,imie):
        return cls(imie, 'Witam mośći pana')


    @staticmethod
    def powitanie():
        return 'To jest powitanie statyczne'








cz1 = Czlowiek('Konrad', 'siema elo')

print(cz1.przywitaj_sie())

cz2 = Czlowiek.nowy_Czlowiek('Jan')

print(cz2.imie)
print(cz2.przywitanie)
print(cz1.przywitanie)


print('-----------------------------')

class Czlowiek2:
    def __init__(self, imie, pelnoletni):
        self.imie = imie
        self.pelnoletni = pelnoletni

    @classmethod
    def Nowyczlowiek(cls, imie, wiek):
        pozwolenie = False
        if wiek >= 18:
            pozwolenie = True
        return cls(imie, pozwolenie)



cz3 = Czlowiek2.Nowyczlowiek('Fabnian', 17)

cz4 = Czlowiek2('Maria', True)

cz5 = Czlowiek2.Nowyczlowiek('Kacper', 21)

print(cz3.pelnoletni)
print(cz4.pelnoletni)
print(cz5.pelnoletni)
