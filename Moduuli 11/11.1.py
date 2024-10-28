class Julkaisu():

    def __init__(self, teos):
        self.teos = teos

    def tulosta_tiedot(self):
        print(f"{self.teos}", end=" ")


class Kirja(Julkaisu):
    def __init__(self, teos, kirjailija, sivut):
        self.kirjailija = kirjailija
        self.sivut = sivut
        super().__init__(teos)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"(Kirjailija: {self.kirjailija}, {self.sivut} sivua)", end=" ")

class Lehti(Julkaisu):
    def __init__(self, teos, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(teos)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"(Päätoimittaja: {self.paatoimittaja})")


# Pääohjelma

lista = []

lista.append(Lehti("Aku Ankka", "Aki Hyyppä"))
lista.append(Kirja("Hytti n:o 6", "Rosa Liksom", "200"))


for i in lista:
    i.tulosta_tiedot()


