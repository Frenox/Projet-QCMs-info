from random import *

mots = ["cerradlassopas","sopa","legume", "abeille", "agneau", "aile", "ane", "arbre", "bain", "barque", "bassin", "bebe", "bec", "bete", "boeuf", "botte de foin", "boue", "bouquet", "bourgeon", "branche", "caillou", "campagne", "car", "champ", "chariot", "chat", "cheminee", "cheval", "chevre", "chien", "cochon", "colline", "coq", "coquelicot", "crapaud", "cygne", "depart", "dindon", "escargot", "etang", "ferme", "fermier", "feuille", "flamme", "fleur", "fontaine", "fumee", "grain", "graine", "grenouille", "griffe", "guepe", "herbe", "herisson", "insecte", "jardin", "mare", "marguerite", "miel", "morceau de pain", "mouche", "mouton", "oie", "oiseau", "pierre", "pigeon", "plante", "plume", "poney", "poule", "poussin", "prairie", "rat", "riviere", "route", "tortue", "tracteur", "tulipe", "vache", "veterinaire", "Landry"]
memoire = None


def formatage_fichier(nom_fichier):
    
    global memoire
    with open(nom_fichier, "r") as fichier:
        contenu = fichier.read()
        #print(contenu)
    
    symbole = '$'
    insymbole = False
    instruction = ''
    newcontenu = ''
    for i in contenu:
        if i == symbole:
            insymbole = not(insymbole)
            if insymbole:
                instruction = ''
            if insymbole == False:
                #print(instruction)
                try:
                    exec(instruction)
                except NameError:
                    print("   ʌ \n  / \\ \n / | \\ \n/__•__\\")
                    print("Une instruction entre '$' n'est pas correcte!\n")
                #print(a)
                newcontenu += str(memoire) 
                memoire = None
        else:
            if insymbole:
                instruction += i
            else:
                newcontenu += i
        
    with open("test_texte_fin.txt", "w") as fichier:
        fichier.write(newcontenu)
        return newcontenu


def gen_bool():
    global memoire
    memoire = choice((True,False))
    return memoire


def gen_int(min = 1, max = 10, pas = 1):
    assert isinstance(min,int) and isinstance(max,int) and isinstance(pas,int) , ""
    assert min < max , ""
    assert pas >= 0 , ""

    global memoire
    memoire = choice(range(min,max,pas))
    return memoire


def gen_str(liste_mots = mots):

    assert isinstance(liste_mots,list) and len(liste_mots) > 0 , ""
    assert all(isinstance(mot,str) for mot in liste_mots) , ""

    global memoire
    memoire = choice(liste_mots)
    return memoire


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
    return memoire


def gen_tuple_int(taille = 6, valeur_max = 100, repetition = False, tri = False):
    global memoire
    memoire = tuple(gen_liste_int(taille, valeur_max, repetition, tri))
    return memoire


def gen_dict(taille = 6, valeur_max = 100, repetition = False, keys = mots):

    assert taille <= len(keys), "La taille est plus grande que le nombre de mots possibles"

    liste = gen_liste_int(taille, valeur_max, repetition)
    dict = {}

    for i in range(taille):
        key = keys.pop(randint(0, len(keys)-1))
        dict[key] = liste[i]

    global memoire
    memoire = dict
    return memoire