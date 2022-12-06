KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko

        self.ljono = [0] * self.kapasiteetti

        self.alkioiden_lkm = 0

    def kuuluu(self, alkio):
        return alkio in self.ljono

    def lisaa(self, alkio): 
        if not self.kuuluu(alkio):
            self.ljono[self.alkioiden_lkm] = alkio
            self.alkioiden_lkm += 1

            if self.alkioiden_lkm % len(self.ljono) == 0:
                self.ljono = [self.ljono[i] if i < len(self.ljono) else 0 for i in range(len(self.ljono)+self.kasvatuskoko)]
            return True
        return False

    def poista(self, alkio):
        if self.kuuluu(alkio):
            self.ljono.remove(alkio)
            self.alkioiden_lkm -= 1
            return True
        return False

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        uusi_taulu = IntJoukko()
        [uusi_taulu.lisaa(alkio) for alkio in a.ljono.copy() + b.ljono.copy()]
        return uusi_taulu

    @staticmethod
    def leikkaus(a, b):
        uusi_taulu = IntJoukko()
        [uusi_taulu.lisaa(alkio) for alkio in a.ljono if b.kuuluu(alkio)]
        return uusi_taulu

    @staticmethod
    def erotus(a, b):
        uusi_taulu = IntJoukko()
        [uusi_taulu.lisaa(alkio) for alkio in a.ljono if not b.kuuluu(alkio)]
        return uusi_taulu

    def __str__(self):
        alkiot = ', '.join([str(alkio) for alkio in self.ljono if alkio != 0])
        return '{' + alkiot + '}' 
