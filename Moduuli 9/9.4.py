import random

autot = []

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

for a in range(10):
    huippunopeus = random.randint(100, 200)
    rekisteritunnus = f"ABC-{a + 1}"
    uusi_auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(uusi_auto)


kilpailu_jatkuu = True

while kilpailu_jatkuu:
    for auto in autot:
        # nop. muutos
        nopeuden_muutos = random.randint(-10, 15)
        auto.kiihdyta(nopeuden_muutos)

        # 1 h
        auto.kulje(1)

        # 10k km
        if auto.kuljettu_matka == 10000:
            kilpailu_jatkuu = False
            break

# Tulostetaan kaikkien autojen tiedot
print(f"{'Rekisteritunnus':<10}, {'Huippunopeus':<15}, {'Nopeus':<10}, {'Kuljettu matka'}")
for auto in autot:
    print(f"{auto.rekisteritunnus:<10}           {auto.huippunopeus:<15}"
          f"{auto.tamanhetkinen_nopeus:<10}    {auto.kuljettu_matka:.2f}")