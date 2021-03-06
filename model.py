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
        return self.stevilo_napak() >= STEVILO_DOVOLJENIH_NAPAK
           

    def pravilni_del_gesla(self):
        sez = ''
        for crka in self.geslo:
            if crka in self.crke:
                sez += crka + '_ '
            else:
                sez += '_ '
        return sez

    def nepravilni_ugibi(self):
        
        return ' '.join(self.napacne_crke())

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
with open('besede.txt',encoding='UTF8') as dat:
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
    
    def nova_igra(self):
        id = self.prost_id_igre()
        igra = nova_igra()
        self.igre[id] = (igra, ZACETEK)
        return id

    def ugibaj(self, id, crka):
        igra, _ = self.igre[id]
        stanje = igra.ugibaj(crka)
        self.igre[id] = (igra, stanje)