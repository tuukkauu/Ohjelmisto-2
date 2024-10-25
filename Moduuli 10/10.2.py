
class Hissi():
    def __init__(self, alin = 1, ylin = 10):
        self.alin = alin
        self.ylin = ylin
        self.nykyinen_kerros = alin

    def siirry_kerrokseen(self, kerros):
        if kerros < self.alin:
            print("Alin mahdollinen kerros on ensimmäinen kerros.")
            kerros = self.alin
        elif kerros > self.ylin:
            print("Ylin mahdollinen kerros on viides kerros.")
            kerros = self.ylin

        if self.nykyinen_kerros == kerros:
            print(f"Hissi on nyt kerroksessa: {self.nykyinen_kerros}")
            return

        while self.nykyinen_kerros < kerros:
            self.kerros_ylos()
        while self.nykyinen_kerros > kerros:
            self.kerros_alas()
        else:
            print(f"Olet nyt kerroksessa {self.nykyinen_kerros}")

    def kerros_ylos(self):
        if self.nykyinen_kerros < self.ylin:
            self.nykyinen_kerros = self.nykyinen_kerros + 1
            print(f"Hissi on nyt kerroksessa: {self.nykyinen_kerros}")
        else:
            print("Hissi on jo ylimmässä kerroksessa.")

    def kerros_alas(self):
        if self.nykyinen_kerros < self.alin:
            self.nykyinen_kerros = self.nykyinen_kerros - 1
            print(f"Hissi on nyt kerroksessa: {self.nykyinen_kerros}")
        else:
            print("Hissi on jo alimmassa kerroksessa.")


# Talo class

class Talo():
    def __init__(self, alin = 1, ylin = 10, lukumaara = 3):
        self.alin = alin
        self.ylin = ylin
        self.lukumaara = lukumaara
        self.hissit = [Hissi(alin, ylin) for _ in range(lukumaara)]

    def hissien_maara(self):
        for h in range(self.lukumaara):
            hissi = Hissi(self.ylin, self.alin)
            self.hissit.append(hissi)
            self.hissi = self.hissi + 1

    def aja_hissia(self, hissin_numero, kohdekerros):
        if 0 < hissin_numero < self.lukumaara:
            print(f"Ajetaan {hissin_numero}. hissiä")
            self.hissit[hissin_numero].siirry_kerrokseen(kohdekerros)
        else:
            print("Hissejä on vain kolme kappaletta.")


# Pääohjelma

talo = Talo(1, 10, 3)

talo.aja_hissia(1, 2)
talo.aja_hissia(2, 5)
