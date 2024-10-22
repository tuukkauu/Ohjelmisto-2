class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tamanhetkinen_nopeus = 0, kuljettu_matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = tamanhetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka


auto1 = Auto("ABC-123", 142)


print(f"Auton rekisteritunnus on {auto1.rekisteritunnus:s}, huippunopeus on {auto1.huippunopeus:d}, "
      f"tämänhetkinen nopeus on {auto1.tamanhetkinen_nopeus:d} km/h ja kuljettu matka on {auto1.kuljettu_matka:d} "
      f"kilometriä.")
