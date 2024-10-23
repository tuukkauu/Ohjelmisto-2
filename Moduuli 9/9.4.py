import random

class Auto():
    def __init__(self, rekisteritunnus, huippunopeus, tamanhetkinen_nopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = tamanhetkinen_nopeus
        self.kuljettu_matka = 0

    #kiihdytysmetodi
    def kiihdyta(self, muutos):
        uusi_nopeus = self.tamanhetkinen_nopeus + muutos

        if uusi_nopeus > self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus

        elif uusi_nopeus < 0:
            self.tamanhetkinen_nopeus = 0

        else:
            self.tamanhetkinen_nopeus = uusi_nopeus

    def kulje(self, tuntimaara):
        self.kuljettu_matka = self.kuljettu_matka + self.tamanhetkinen_nopeus * tuntimaara


autot = []

for a in range(10):
    autot.append(f"auto {1 + a}")

print(autot)

for a in range(10):
    random.randint()

# auto1 = Auto("ABC-123", 142,)

