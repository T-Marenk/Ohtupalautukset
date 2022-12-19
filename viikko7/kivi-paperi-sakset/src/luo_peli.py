from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

class LuoPeli:
    def luo_peli(self, valinta):
        valinnat = {"a": KPSPelaajaVsPelaaja,
                    "b": KPSTekoaly,
                    "c": KPSParempiTekoaly
                    }
        return valinnat[valinta]()
