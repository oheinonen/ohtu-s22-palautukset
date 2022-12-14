from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self._hinta = 0
        self._tavaroita_korissa = 0
        self._ostokset = []

    def tavaroita_korissa(self):
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 
        return self._tavaroita_korissa

    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        return self._hinta

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        self._hinta += lisattava.hinta()
        self._tavaroita_korissa += 1
        on_korissa = False
        for i in range(len(self._ostokset)):
            if lisattava == self._ostokset[i].tuote:
                on_korissa = True
                self._ostokset[i].muuta_lukumaaraa(1)
        if not on_korissa:
            self._ostokset.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        for i in range(len(self._ostokset)):
            if poistettava == self._ostokset[i].tuote:
                self._ostokset[i].muuta_lukumaaraa(-1)
                self._tavaroita_korissa -= 1
                self._hinta -= poistettava.hinta()


    def tyhjenna(self):
        # tyhjentää ostoskorin
        self._hinta = 0
        self._tavaroita_korissa = 0
        self._ostokset = []

    def ostokset(self):
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
        return self._ostokset
