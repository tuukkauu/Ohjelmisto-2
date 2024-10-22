class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

# auto-olio
auto1 = Auto("ABC-123", 142)


print(f"Auton rekisteritunnus on {auto1.rekisteritunnus:s}, huippunopeus on {auto1.huippunopeus:d} km/h, "
      f"tämänhetkinen nopeus on {auto1.tamanhetkinen_nopeus:d} km/h ja kuljettu matka on {auto1.kuljettu_matka:d} "
      f"km.")
