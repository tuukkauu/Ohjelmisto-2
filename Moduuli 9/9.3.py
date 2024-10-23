class Auto():
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
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

auto = Auto("ABC-123", 142)

# auton alkuperäiset tiedot:
print(f"Auton rekisteritunnus on {auto.rekisteritunnus}, huippunopeus on {auto.huippunopeus} km/h,"
      f"tämänhetkinen nopeus on {auto.tamanhetkinen_nopeus} km/h ja kuljettu matka on "
      f"{auto.kuljettu_matka} km.")

# kuljettu matka, kun nopeus muuttuu
auto.kiihdyta(30)
print(f"Nopeus kiihdytyksen jälkeen (+30 km/h): {auto.tamanhetkinen_nopeus} km/h.")
auto.kulje(1.5)
print(f"Kuljettu matka tällä nopeudella 1,5 h aikana on {auto.kuljettu_matka} km.")

auto.kiihdyta(60)
print(f"Nopeus kiihdytyksen jälkeen (+30 km/h): {auto.tamanhetkinen_nopeus} km/h.")
auto.kulje(1.5)
print(f"Kuljettu matka tällä nopeudella 1,5 h aikana on {auto.kuljettu_matka} km.")