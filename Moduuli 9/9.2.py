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



# pääohjelma:
auto = Auto("ABC-123", 142)

# auton alkuperäiset tiedot:
print(f"Auton rekisteritunnus on {auto.rekisteritunnus}, huippunopeus on {auto.huippunopeus} km/h,"
      f"tämänhetkinen nopeus on {auto.tamanhetkinen_nopeus} km/h ja kuljettu matka on"
      f"{auto.kuljettu_matka} km.")

# +30 km/h
auto.kiihdyta(30)
print(f"Nopeus kiihdytyksen jälkeen (+30 km/h): {auto.tamanhetkinen_nopeus} km/h.")

# +70 km/h
auto.kiihdyta(70)
print(f"Nopeus kiihdytyksen jälkeen (+70 km/h): {auto.tamanhetkinen_nopeus} km/h.")

# +50 km/h
auto.kiihdyta(50)
print(f"Nopeus nyt maksiminopeus (+50 km/h): {auto.tamanhetkinen_nopeus} km/h.")

# hätäjarrutus -200 km/h
auto.kiihdyta(-200)
print(f"Nopeus hätäjarrutuksen jälkeen (-200 km/h): {auto.tamanhetkinen_nopeus} km/h.")
