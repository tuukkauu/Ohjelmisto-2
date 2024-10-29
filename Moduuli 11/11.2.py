class Auto():
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kulje(self, tuntimaara):
        self.kuljettu_matka = self.kuljettu_matka + self.tamanhetkinen_nopeus * tuntimaara

    def tulosta_tiedot(self):
        print(self.rekisteritunnus, self.huippunopeus, self.tamanhetkinen_nopeus, self.kuljettu_matka)


class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, kapasiteetti):
        self.kapasiteetti = kapasiteetti
        super().__init__(rekisteritunnus, huippunopeus)

    def tulosta_tiedot(self):
        print(f"{self.kapasiteetti}")
        super().tulosta_tiedot()


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, kulutus):
        self.kulutus = kulutus
        super().__init__(rekisteritunnus, huippunopeus)

    def tulosta_tiedot(self):
        print(f"{self.kulutus}")
        super().tulosta_tiedot()


# Pääohjelma

lista = []

lista.append(Sahkoauto("ABC-15", 180, 52.5))
lista.append(Polttomoottoriauto("ACD-123", 165, 32.3))


for i in lista:
    i.kulje(3)
    i.tulosta_tiedot()


