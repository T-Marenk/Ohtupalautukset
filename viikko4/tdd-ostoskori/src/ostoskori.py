from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._kori = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        maara = 0
        for ostos in self._kori:
            maara += ostos.lukumaara()
        return maara
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        hinta = 0
        for ostos in self._kori:
            hinta += ostos.hinta()
        return hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        for ostos in self._kori:
            if lisattava.nimi() == ostos.tuotteen_nimi():
                ostos.muuta_lukumaaraa(1)
                return
        ostos = Ostos(lisattava)
        self._kori.append(ostos)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        for ostos in self._kori:
            if ostos.tuotteen_nimi() == poistettava.nimi():
                ostos.muuta_lukumaaraa(-1)
                lkm = ostos.lukumaara()
                if lkm == 0:
                    self._kori.remove(ostos)
                return

    def tyhjenna(self):
        self._kori = []
        # tyhjentää ostoskorin

    def ostokset(self):
        return self._kori
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
