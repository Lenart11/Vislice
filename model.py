import random

STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = '0'
NAPACNA_CRKA = '-'
ZMAGA = 'W'
PORAZ = 'X'
ZACETEK = 'Z'
class Igra:
    def __init__(self, geslo, crke=[]):
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
    def nepravilni_ugibi(self):
        brez_presledkov = ''.join(self.napacne_crke())
        return brez_presledkov.split(' ')
    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        else:
            self.crke.append(crka)
            if crka in self.pravilne_crke():
                if self.zmaga() == True:
                    return ZMAGA
                else:
                    return PRAVILNA_CRKA
            elif crka in self.napacne_crke():
                if self.poraz() == True:
                    return PORAZ
                else:
                    return NAPACNA_CRKA

bazen_besed = []
with open('besede.txt') as dat:
    for vrstica in dat:
        bazen_besed.append(vrstica.strip().upper())
def nova_igra():
    return Igra(random.choice(bazen_besed))



class Vislice:
    def __init__(self):
        self.igre = {}
    def prost_id_igre(self):
        if len(self.igre) == 0:
            return 0
        else:
            return max(self.igre.keys()) + 1
