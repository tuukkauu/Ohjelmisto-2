import random


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

autot = []
for a in range(10):
    huippunopeus = random.randint(100, 200)
    rekisteritunnus = f"ABC-{a + 1}"
    uusi_auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(uusi_auto)


# Kilpailu-luokka
class Kilpailu():
    def __init__(self, kilpailun_nimi, pituus_km, autot_mukana):
        self.kilpailun_nimi = kilpailun_nimi
        self.pituus_km = pituus_km
        self.autot_mukana = autot_mukana

    def tunti_kuluu(self):
        for auto in self.autot_mukana:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdyta(nopeuden_muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"{'Rekisteritunnus':<10}  {'Huippunopeus':<15}  {'Nopeus':<10}  {'Kuljettu matka'}")
        for auto in self.autot_mukana:
            print(f"{auto.rekisteritunnus:<10}           {auto.huippunopeus:<15}"
                  f"{auto.tamanhetkinen_nopeus:<10}    {auto.kuljettu_matka:.2f}")

    def kilpailu_ohi(self):
        for auto in self.autot_mukana:
            if auto.kuljettu_matka >= self.pituus_km:
                return True
        return False


# Pääohjelma:

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)
tunnit = 0

while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunnit = tunnit + 1
    if tunnit % 10 == 0:
        kilpailu.tulosta_tilanne()

# Lopputilanne:

print("Kilpailu päättyi. Lopputilanne on:")
kilpailu.tulosta_tilanne()
