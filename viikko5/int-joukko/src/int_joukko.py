KAPASITEETTI = 5
OLETUSKASVATUS = 5

class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D
        else:
            self.kapasiteetti = kapasiteetti

        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("kapasiteetti2")  # heitin vaan jotain :D
        else:
            self.kasvatuskoko = kasvatuskoko

        self.ljono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, luku):
        return luku in self.ljono

    def lisaa(self, uusi_luku):
        if not self.kuuluu(uusi_luku):
            self.ljono[self.alkioiden_lkm] = uusi_luku
            self.alkioiden_lkm += 1
            if self.alkioiden_lkm % len(self.ljono) == 0:
                self.ljono.extend([0] * (self.kasvatuskoko))

    def poista(self, luku):
        if self.kuuluu(luku):
            i = self.ljono.index(luku)
            del self.ljono[i]
            self.alkioiden_lkm = self.alkioiden_lkm - 1

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        tuotos = "{"
        for i in range(0, self.alkioiden_lkm - 1):
            tuotos += str(self.ljono[i])
            tuotos += ", "
        tuotos += str(self.ljono[self.alkioiden_lkm - 1]) if self.alkioiden_lkm else ""
        tuotos += "}"
        return tuotos
