class Hissi():
    def __init__(self, alin = 1, ylin = 5):
        self.alin = alin
        self.ylin = ylin
        self.nykyinen_kerros = alin

    def siirry_kerrokseen(self, kerros):
        if self.kerros > self.nykyinen_kerros:
            while self.nykyinen_kerros < kerros:
                self.kerros_ylos()
                print(self.nykyinen_kerros)

        elif self.kerros < self.nykyinen_kerros:
            while self.nykyinen_kerros > kerros:
                self.kerros_alas()
                print(self.nykyinen_kerros)

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

h = Hissi()

h.siirry_kerrokseen(5)
h.siirry_kerrokseen(1)

#if kerros != 1:
    #   self.kerros_alas()