class Auto():
    def __init__(self, nopeus, aika):
        self.nopeus = nopeus
        self.aika = aika

    def tulosta_tiedot(self):
        matka = self.nopeus * self.aika
        print(f"Auton kulkema matka {self.aika} tunnin aikana ja {self.nopeus} kilometrin"
              f" tuntinopeudella on {matka} kilometriä.")


class Sahkoauto(Auto):
    def __init__(self, nopeus, aika, rekisteritunnus, huippunopeus = 180, akkukapasiteetti = 52.5):
        self.huippunopeus = huippunopeus
        self.akkukapasiteetti = akkukapasiteetti
        self.rekisteritunnus = rekisteritunnus
        super().__init__(nopeus, aika)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kyseinen auto on sähköauto: {self.rekisteritunnus}, huippunopeus on {self.huippunopeus} km/h ja"
              f" akun kapasiteetti {self.akkukapasiteetti} kWh.")


class Polttomoottoriauto(Auto):
    def __init__(self, nopeus, aika, rekisteritunnus, huippunopeus, tankki = 32.3):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tankki = tankki
        super().__init__(nopeus, aika)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kyseinen auto on polttomoottoriauto: {self.rekisteritunnus}, huippunopeus on {self.huippunopeus} km/h ja"
              f" tankin koko {self.tankki} l.")


# Pääohjelma

autot = []

autot.append(Sahkoauto(170, 3, "ABC-15", 180, 52.5))
autot.append(Polttomoottoriauto(100, 3, "ACD-123", 165, 32.5))

for a in autot:
    a.tulosta_tiedot()

