from tuomari import Tuomari
from tekoaly import Tekoaly


class KPSTekoaly:
    def __init__(self):
        self._tekoaly = Tekoaly()

    def _toisen_pelaajan_siirto(self, *siirrot):
        tokan_siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        return tokan_siirto


