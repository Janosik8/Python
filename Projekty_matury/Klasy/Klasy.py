class zwierze:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def voice(self):
        print("Należę do zwierząt")

class kot(zwierze):
    def getvoice(self):
        print("Hejo, jestem kotem")
        super().voice()

class psy(kot):
    def getvoice(self, przywitanie = "Hej"):
        print(przywitanie + ' jestem psem i mam lat: ' + str(self.wiek))
        super().voice()

kot1 = kot("Borys", 9)
kot1.getvoice()
print('---------')
pes1 = psy("Burek", 9)
pes1.getvoice("Siema")