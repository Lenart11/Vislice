STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = '0'
NAPACNA_CRKA = '-'
ZMAGA = 'W'
PORAZ = 'X'
class Igra:
    def __init__(self, geslo, crke):
        self.geslo = geslo
        self.crke = crke

    def napacne_crke(self):
        sez = []
        for crka in self.crke:
            if crka not in self.geslo:
                sez.append(crka)
        return sez
    def pravilne_crke(self):
        sez = []
        for crka in self.crke:
            if crka in self.geslo:
                sez.append(crka)
        return sez
    def stevilo_napak(self):
        return len(self.napacne_crke())
    def zmaga(self):
        for crka in self.geslo:
            if crka not in self.crke:
                return False
        return True
    def poraz(self):
        if self.stevilo_napak() == STEVILO_DOVOLJENIH_NAPAK:
            return True
        else:
            return False
    def pravilni_del_gesla(self):
        sez = []
        for crka in self.crke():
            if crka in self.pravilne_crke():
                sez.append(crka)
            else:
                sez.append('_')
        return sez


        
