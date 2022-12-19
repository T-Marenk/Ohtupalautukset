from kivi_paperi_sakset import KiviPaperiSakset

def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        vaihtoehdot = ["a", "b", "c"]
        if vastaus in vaihtoehdot:
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )
            peli = KiviPaperiSakset(vastaus)
            peli.pelaa()
        else:
            break

if __name__ == "__main__":
    main()
