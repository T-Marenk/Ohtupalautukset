from tekoaly_parannettu import TekoalyParannettu


class KPSParempiTekoaly:
    def __init__(self):
        self._tekoaly = TekoalyParannettu(10)

    def _toisen_pelaajan_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        self._tekoaly.aseta_siirto(ensimmaisen_siirto)
        return tokan_siirto
