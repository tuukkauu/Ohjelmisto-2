class Julkaisu():

    def __init__(self, julkaisun_nimi, etunimi, sukunimi):
        self.julkaisun_nimi = julkaisun_nimi
        self.etunimi = etunimi
        self.sukunimi = sukunimi

    def tulosta_tiedot(self):
        print(f"{self.julkaisun_nimi}, {self.etunimi} {self.sukunimi}")


# Pääohjelma

