class Julkaisu():

    def __init__(self, teos):
        self.teos = teos

    def tulosta_tiedot(self):
        print(f"{self.teos}")

class Julkaisija(Julkaisu):

    def __init__(self, teos, ammattinimike, etunimi, sukunimi):
        self.ammattinimike = ammattinimike
        self.etunimi = etunimi
        self.sukunimi = sukunimi
        super().__init__(teos)


    def tulosta_tiedot(self):
        super().tulosta.tiedot()
        print(f": {self.ammattinimike}, {self.etunimi} {self.sukunimi}")



# Pääohjelma

Julkaisija.tulosta_tiedot("Päätoimittaja", "Aki", "Hyyppä")

