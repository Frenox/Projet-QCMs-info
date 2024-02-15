from random import *

mots = ["jgjvdsjsv","hdsv","ceradlassopas","gvsd","psojf","jv","ghgcgj"]
memoire = None


def gen_bool():
    global memoire
    memoire = choice((True,False))


def gen_int(min = 1, max = 10, pas = 1):

    assert isinstance(min,int) and isinstance(max,int) and isinstance(pas,int) , ""
    assert min < max , ""
    assert pas >= 0 , ""

    global memoire
    memoire = choice(range(min,max,pas))


def gen_str(liste_mots = mots):

    assert isinstance(liste_mots,list) and len(liste_mots) > 0 , ""
    assert all(isinstance(mot,str) for mot in liste_mots) , ""

    global memoire
    memoire = choice(liste_mots)


def gen_liste_int(taille = 5, valeur_max = 100, repetition = False, tri = False):

    assert isinstance(taille,int) and isinstance(valeur_max,int)
    assert isinstance(repetition,int) and isinstance(tri,int)

    if repetition:
        liste = [randint(0, valeur_max-1) for _ in range(taille)]

    else:
        assert taille <= valeur_max, "la taille est plus grande que la valeur max"
        possible = list(range(valeur_max))
        liste = [possible.pop(randint(0, len(possible)-1)) for _ in range(taille)]
     
    if tri:
        liste.sort()
    
    global memoire
    memoire = liste


def gen_tuple_int(taille = 6, valeur_max = 100, repetition = False, tri = False):
    global memoire
    memoire = tuple(gen_liste_int(taille, valeur_max, repetition, tri))


def gen_dict(taille = 6, valeur_max = 100, repetition = False, keys = mots):

    assert taille <= len(keys), "La taille est plus grande que le nombre de mots possibles"

    liste = gen_liste_int(taille, valeur_max, repetition)
    dict = {}

    for i in range(taille):
        key = keys.pop(randint(0, len(keys)-1))
        dict[key] = liste[i]

    global memoire
    memoire = dict


