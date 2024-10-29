class Auto():
    def __init__(self, nopeus, aika, rekisteritunnus):
        self.rekisteritunnus = rekisteritunnus
        self.nopeus = nopeus
        self.aika = aika

    def tulosta_tiedot(self):
        matka = self.nopeus * self.aika
        print(f"{matka}, {self.rekisteritunnus}, {self.nopeus}, {self.aika}")


class Sahkoauto(Auto):
    def __init__(self, nopeus, aika, rekisteritunnus, huippunopeus = 180, akkukapasiteetti = 52.5):
        self.huippunopeus = huippunopeus
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(nopeus, aika, rekisteritunnus)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(self.rekisteritunnus, self.huippunopeus, self.akkukapasiteetti)


class Polttomoottoriauto(Auto):
    def __init__(self, nopeus, aika, rekisteritunnus, huippunopeus, tankki = 32.3):
        self.huippunopeus = huippunopeus
        self.tankki = tankki
        super().__init__(nopeus, aika, rekisteritunnus)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"{self.tankki}", end = " ")


# Pääohjelma

autot = []

autot.append(Sahkoauto(100, 3, "ABC-15"))
autot.append(Polttomoottoriauto(100, 3, 165, 32.5, "ACD-123"))

for a in autot:
    a.tulosta_tiedot()

