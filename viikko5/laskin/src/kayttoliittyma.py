from enum import Enum
from tkinter import ttk, constants, StringVar


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4

class Summa:
    def __init__(self, sovelluslogiikka, syote, aseta):
        self._sovelluslogiikka = sovelluslogiikka
        self._syote = syote
        self._aseta = aseta

    def suorita(self):
        self._aseta()
        self._sovelluslogiikka.plus(self._syote())

    def kumoa(self, edellinen):
        self._sovelluslogiikka.aseta_arvo(edellinen)

class Erotus:
    def __init__(self, sovelluslogiikka, syote, aseta):
        self._sovelluslogiikka = sovelluslogiikka
        self._syote = syote
        self._aseta = aseta

    def suorita(self):
        self._aseta()
        self._sovelluslogiikka.miinus(self._syote())

    def kumoa(self, edellinen):
        self._sovelluslogiikka.aseta_arvo(edellinen)

class Nollaus:
    def __init__(self, sovelluslogiikka, syote, aseta):
        self._sovelluslogiikka = sovelluslogiikka
        self._syote = syote
        self._aseta = aseta

    def suorita(self):
        self._aseta()
        self._sovelluslogiikka.nollaa()

    def kumoa(self, edellinen):
         self._sovelluslogiikka.aseta_arvo(edellinen)

class Kumoa:
    def __init__(self, sovelluslogiikka, edellinen, edellinen_tulos):
        self._sovelluslogiikka = sovelluslogiikka
        self._edellinen = edellinen
        self._edellinen_tulos = edellinen_tulos

    def suorita(self):
        edellinen_komento = self._edellinen()
        edellinen_tulos = self._edellinen_tulos()
        edellinen_komento.kumoa(edellinen_tulos)

class Kayttoliittyma:
    def __init__(self, sovelluslogiikka, root):
        self._sovelluslogiikka = sovelluslogiikka
        self._root = root

        self._komennot = {
                Komento.SUMMA: Summa(sovelluslogiikka, self._lue_syote, self._aseta_edellinen),
                Komento.EROTUS: Erotus(sovelluslogiikka, self._lue_syote, self._aseta_edellinen),
                Komento.NOLLAUS: Nollaus(sovelluslogiikka, self._lue_syote, self._aseta_edellinen),
                Komento.KUMOA: Kumoa(sovelluslogiikka, self._hae_edellinen_komento, self._hae_edellinen_tulos)
            }

        self._edellinen_tulos = 0
        self._edellinen_komento = None

    def kaynnista(self):
        self._tulos_var = StringVar()
        self._tulos_var.set(self._sovelluslogiikka.tulos)
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._tulos_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def _lue_syote(self):
        arvo = 0

        try:
            arvo = int(self._syote_kentta.get())
        except Exception:
            pass

        return arvo

    def _hae_edellinen_komento(self):
        return self._edellinen_komento

    def _hae_edellinen_tulos(self):
        return self._edellinen_tulos

    def _aseta_edellinen(self):
        self._edellinen_tulos = self._sovelluslogiikka.tulos

    def _suorita_komento(self, komento):
        komento_olio = self._komennot[komento]
        komento_olio.suorita()
        self._edellinen_komento = komento_olio
        self._kumoa_painike["state"] = constants.NORMAL

        if self._sovelluslogiikka.tulos == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._tulos_var.set(self._sovelluslogiikka.tulos)

