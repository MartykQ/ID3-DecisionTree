"""

Reguła = fakt -> przesłanka

przykład faktu:
    przedmiot = nudny
    pogoda = ladna


    humor = swietny



przykład reguły:

    przedmiot = nudny THEN pogoda = ladna
    (przedmiot = nudny AND pogoda = ladna) THEN humor = kiepski



PPRZYKLAD DZIALANIA

    FAKT_IN: pogoda = kiepska
    //WNIOSKUJEMY HUMOR

    REGULY

        pogoda = kiepska THEN czas = duzo
        czas = duzo THEN rozrywka = duzo
        rorywka = duzo AND pogoda = kiepska THEN humor = sredni


"""

class Fact:
    def __init__(self, kategoria, wartosc):
        self.kategoria = kategoria
        self.wartosc = wartosc

    def __str__(self):
        return str(self.kategoria) + ' = '+str(self.wartosc)

def CompareFacts(faktA, faktB):
    if (faktA.kategoria == faktB.kategoria) & (faktA.wartosc == faktB.wartosc):
        return True
    return False

class Rule:
    """
    :parameter FAKT_IN => tablica faktow
    """
    def __init__(self, FAKT_IN, FAKT_OUT):
        if isinstance(FAKT_IN, (list,)):
            self.fakt_in = FAKT_IN
        else:
            self.fakt_in = [FAKT_IN,]

        self.fakt_out = FAKT_OUT

    def ActivateRule(self):
        return self.fakt_out

    def testRule(self, input):
        """Czy kazda przeslanka jest w zbiorze faktow"""

        for przeslanka in self.fakt_in:
            if przeslanka in input:
                pass
            else:
                return False

        return self.fakt_out



def WyznaczRegulySpelnione(FAKTY, REGULY):
    RegulySpelnione = []
    for regula in REGULY:
        if not regula.testRule(FAKTY):
            RegulySpelnione.append(regula.fakt_out)
    return RegulySpelnione


def SprawdzCel(cel, FAKTY):
    """
    Zwraca TRUE jesli w zbiorze faktow jest fakt, w kieunku ktorego wnioskujemy
    """
    for fakt in FAKTY:
        if fakt.kategoria == cel:
            return True
        return False


def WnioskowaniePrzod(ZBIOR_REGUL, ZBIOR_FAKTOW, cel):
    i = 0
    S = WyznaczRegulySpelnione(ZBIOR_FAKTOW, ZBIOR_REGUL)
    while len(S) != 0 & (not SprawdzCel(cel, ZBIOR_FAKTOW)):
        ZBIOR_FAKTOW.append(ZBIOR_REGUL[i].ActivateRule())
        ZBIOR_REGUL.remove(ZBIOR_REGUL[i])
        S = WyznaczRegulySpelnione(ZBIOR_FAKTOW, ZBIOR_REGUL)




fakt1 = Fact("dystans", "0-1km")
fakt2 = Fact("dystans", "1-2km")
fakt3 = Fact("dystans", "2-3km")
fakt4 = Fact("dystans", "3km+")
fakt5 = Fact("pogoda","slonecznie")
fakt6 = Fact("pogoda","zachmurzenie")
fakt7 = Fact("pogoda","opady")
fakt8 = Fact("zapas czasu", "<15min")
fakt9 = Fact("zapas czasu", "<30min")
fakt10 = Fact("zapas czasu", ">30min")
fakt11 = Fact("KKM?", "tak")
fakt12 = Fact("KKM?", "nie")
fakt13 = Fact("ruch", "godziny szczytu")
fakt14 = Fact("ruch", "umiarkowany")
fakt15 = Fact("ruch", "brak ruchu")
fakt16 = Fact("srodek transportu", "pieszo")
fakt17 = Fact("srodek transportu", "rower")
fakt18 = Fact("srodek transportu", "mpk")
fakt19 = Fact("srodek transportu", "taxi/uber")
fakt20 = Fact("srodek transportu", "auto")


regula1 = Rule(fakt1, fakt17)
regula2 = Rule([fakt1, fakt6], fakt17)

#TETUJEMY

ZBIOR_REGUL = [regula1, regula2, regula3]
ZBIOR_FAKTOW = [fakt1]

WnioskowaniePrzod(ZBIOR_REGUL, ZBIOR_FAKTOW, "humor")

for fakcior in ZBIOR_FAKTOW:
    print(fakcior)

