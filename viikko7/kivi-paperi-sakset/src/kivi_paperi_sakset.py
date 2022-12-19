from tuomari import Tuomari
from luo_peli import LuoPeli

class KiviPaperiSakset:
    def __init__(self, tyyppi: str = "a") -> None:
        self._toinen_pelaaja = LuoPeli().luo_peli(tyyppi)

    def pelaa(self):
        tuomari = Tuomari()

        ekan_siirto = self._ekan_siirto()
        tokan_siirto = self._tokan_siirto(ekan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

            ekan_siirto = self._ekan_siirto()
            tokan_siirto = self._tokan_siirto(ekan_siirto)

        print("Kiitos!")
        print(tuomari)
    
    def _ekan_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def _tokan_siirto(self, ensimmaisen_siirto):
        return self._toinen_pelaaja._toisen_pelaajan_siirto(ensimmaisen_siirto)

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
            

