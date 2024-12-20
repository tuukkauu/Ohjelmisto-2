class Hissi():
    def __init__(self, alin = 1, ylin = 5):
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

# Pääohjelmassa, kutsutaan hissi
h = Hissi(1, 10)
h.siirry_kerrokseen(-1)
h.siirry_kerrokseen(5)
