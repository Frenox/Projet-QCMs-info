from random import *

mots = ["jgjvdsjsv","hdsv","ceradlassopas","gvsd","psojf","jv","ghgcgj"]

def gen_liste_int(taille = 6, valeur_max = 100, repetition = False, tri = False):

    if repetition:
        liste = [randint(0, valeur_max-1) for _ in range(taille)]

    else:
        assert taille <= valeur_max, "la taille est plus grande que la valeur max"
        possible = list(range(valeur_max))
        liste = [possible.pop(randint(0, len(possible)-1)) for _ in range(taille)]
     
    if tri:
        liste.sort()

    return liste


def gen_tuple_int(taille = 6, valeur_max = 100, repetition = False, tri = False):
    return tuple(gen_liste_int(taille, valeur_max, repetition, tri))


def gen_dict(taille = 6, valeur_max = 100, repetition = False):

    assert taille <= len(mots), "La taille est plus grande que le nombre de mots possibles"

    keys = mots.copy()
    liste = gen_liste_int(taille, valeur_max, repetition)
    dict = {}

    for i in range(taille):
        key = keys.pop(randint(0, len(keys)-1))
        dict[key] = liste[i]

    return dict


print(gen_liste_int())
