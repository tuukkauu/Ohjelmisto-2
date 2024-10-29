class Auto():
    def __init__(self, nopeus, aika):
        self.nopeus = nopeus
        self.aika = aika

    def tulosta_tiedot(self):
        matka = self.nopeus * self.aika
        print(matka)


class Sahkoauto(Auto):
    def __init__(self, nopeus, aika, rekisteritunnus, huippunopeus = 180, akkukapasiteetti = 52.5):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(nopeus, aika)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"{self.akkukapasiteetti}")


class Polttomoottoriauto(Auto):
    def __init__(self, nopeus, aika, rekisteritunnus, huippunopeus = 165, tankki = 32.3):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tankki = tankki
        super().__init__(nopeus, aika)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"{self.tankki}", end = " ")


# Pääohjelma

autot = []

autot.append(Sahkoauto(100, 3, "ABC-15"))
autot.append(Polttomoottoriauto(100, 3, "ACD.123"))

for a in autot:
    a.tulosta_tiedot()

