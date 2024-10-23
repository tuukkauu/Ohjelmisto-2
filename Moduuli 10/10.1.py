class Hissi():
    def __init__(self, alin = 1, ylin = 5):
        self.alin = alin
        self.ylin = ylin
        self.nykyinen_kerros = alin

    def siirry_kerrokseen(self, kerros):
        if kerros != 1:
            self.kerros_alas()
        if self.kerros > self.nykyinen_kerros:
            while self.nykyinen_kerros < kerros:
                self.kerros_ylos()
                print(self.nykyinen_kerros)

        elif self.kerros < self.nykyinen_kerros:
            while self.nykyinen_kerros > kerros:
                self.kerros_alas()
                print(nykyinen_kerros)

    def kerros_ylos(self, ylos):
        for i in range(ylos):
            i = i + 1
            print(f"Kerros {i}")
        return

    def kerros_alas(self, alas):
        for i in range(alas):
            i = i - 1
            print(f"Kerros {i}")
        return

#if kerros != 1:
 #   self.kerros_alas()

# Pääohjelmassa kutusutaan hissi. (uusi)

h = Hissi()


h.siirry_kerrokseen(5)