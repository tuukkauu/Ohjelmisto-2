class Julkaisu():

    def __init__(self, teos):
        self.teos = teos

    def tulosta_tiedot(self):
        print(f"{self.teos}")


class Kirjailija(Julkaisu):
    def __init__(self, teos, kirjailija, etunimi, sukunimi):
        self.kirjailija = kirjailija
        self.etunimi = etunimi
        self.sukunimi = sukunimi
        super().__init__(teos)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"{self.kirjailija} {self.etunimi} {self.sukunimi}")

class Paatoimittaja(Julkaisu):
    def __init__(self, teos, paatoimittaja, etunimi, sukunimi):
        self.paatoimittaja = paatoimittaja
        self.etunimi = etunimi
        self.sukunimi = sukunimi
        super().__init__(teos)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"{self.paatoimittaja} {self.etunimi} {self.sukunimi}")


"""
class Julkaisija(Julkaisu):

    def __init__(self, teos, ammattinimike, etunimi, sukunimi):
        self.ammattinimike = ammattinimike
        self.etunimi = etunimi
        self.sukunimi = sukunimi
        super().__init__(teos)


    def tulosta_tiedot(self):
        super().tulosta.tiedot()
        print(f": {self.ammattinimike}, {self.etunimi} {self.sukunimi}")
"""


# Pääohjelma

Julkaisu.tulosta_tiedot()
