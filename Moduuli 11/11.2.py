class Auto():
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0


    def kulje(self, tuntimaara):
        self.kuljettu_matka = self.kuljettu_matka + self.tamanhetkinen_nopeus * tuntimaara
        if self.kuljettu_matka >= 10000:
            self.kuljettu_matka = 10000

class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus):


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus):

