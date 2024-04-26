from random import *

mots = ["cerradlassopas","sopa","legume", "abeille", "agneau", "aile", "ane", "arbre", "bain", "barque", "bassin", "bebe", "bec", "bete", "boeuf", "botte de foin", "boue", "bouquet", "bourgeon", "branche", "caillou", "campagne", "car", "champ", "chariot", "chat", "cheminee", "cheval", "chevre", "chien", "cochon", "colline", "coq", "coquelicot", "crapaud", "cygne", "depart", "dindon", "escargot", "etang", "ferme", "fermier", "feuille", "flamme", "fleur", "fontaine", "fumee", "grain", "graine", "grenouille", "griffe", "guepe", "herbe", "herisson", "insecte", "jardin", "mare", "marguerite", "miel", "morceau de pain", "mouche", "mouton", "oie", "oiseau", "pierre", "pigeon", "plante", "plume", "poney", "poule", "poussin", "prairie", "rat", "riviere", "route", "tortue", "tracteur", "tulipe", "vache", "veterinaire", "Landry"]

memoire = None #garde en mémoire les résultats des fonctions entre balises


def formatage_fichier(nom_fichier):
    ''' permetde remplacer sur un document texte le code entre les balises $
        par ce que renvoie ce code

        :paramètres:

        nom_fichier : str : contient le nom du fichier texte que
        l'on souhaite modifié

        :variables:

        symbole : str : contient le sybole des balises.
        
        insymbole : bool : indique True si le curseur de lecture
        de la fonction est entre deux balises
        
        instruction : str : permet après lecture par la fonction
        de stocker le contenu des balises.
        
        :return:

        newcontenu : str : contient le texte modifié.    
    '''
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
        
    return newcontenu


def gen_bool():
    """
    Genere aleatoirement un booleen
    Inputs:
       None
    Outputs:
        memoire (bool) : booleen genere
    """
    global memoire
    memoire = choice((True,False))
    return memoire


def gen_int(min = 1, max = 10, pas = 1):
    """
    Genere aleatoirement un entier entre les valeurs min et max avec un certain pas
    Inputs:
       min (int): entier minimum pouvant etre genere
       max (int): entier maximum pouvant etre genere
       pas (int): pas pour la generation des entiers
    Outputs:
        memoire (int) : entier genere
    """
    assert isinstance(min,int) and isinstance(max,int) and isinstance(pas,int) , ""
    assert min < max , ""
    assert pas >= 0 , ""

    global memoire
    memoire = choice(range(min,max,pas))
    return memoire


def gen_str(liste_mots = mots):
    """
    Genere aleatoirement une chaine de caractere parmis une liste predefinie ou une liste donnee
    Inputs:
       liste_mots (liste): liste de str
    Outputs:
        memoire (str) : str genere
    """
    assert isinstance(liste_mots,list) and len(liste_mots) > 0 , ""
    assert all(isinstance(mot,str) for mot in liste_mots) , ""

    global memoire
    memoire = choice(liste_mots)
    return memoire


def gen_liste_int(taille = 5, valeur_max = 100, repetition = False, tri = False):
    """
    Genere aleatoirement une liste d'entier
    Inputs:
       taille (int): taille de la liste
       valeur_max (int): valeur maximale pour les entiers
       repetition (bool): indique si la repetition des entiers est possible
       tri (bool): indique si la liste doit etre triee
    Outputs:
        memoire (liste) : liste d'entier generee
    """
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
    """
    Genere aleatoirement une tuple d'entier
    Inputs:
       taille (int): taille du tuple
       valeur_max (int): valeur maximale pour les entiers
       repetition (bool): indique si la repetition des entiers est possible
       tri (bool): indique si le tuple doit etre trie
    Outputs:
        memoire (tupl) : tuple d'entier genere
    """
    global memoire
    memoire = tuple(gen_liste_int(taille, valeur_max, repetition, tri))
    return memoire


def gen_dict(taille = 6, valeur_max = 100, repetition = False, keys = mots):
    """
    Genere aleatoirement une dictionnaire avec pour cles des str et pour valeurs des entier
    Inputs:
       taille (int): taille ddictionnaire
       valeur_max (int): valeur maximale pour les entiers
       repetition (bool): indique si la repetition des entiers est possible
       keys (list): liste de str pour les cles du dictionnaire
    Outputs:
        memoire (dict) : dictionnaire genere
    """
    assert taille <= len(keys), "La taille est plus grande que le nombre de mots possibles"

    liste = gen_liste_int(taille, valeur_max, repetition)
    dict = {}

    for i in range(taille):
        key = keys.pop(randint(0, len(keys)-1))
        dict[key] = liste[i]

    global memoire
    memoire = dict
    return memoire
