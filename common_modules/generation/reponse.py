from random import *

def rep(execution,path_reponse):
    """
    Renvoi une liste de liste, chaque sous-liste represente un question avec 4 reponses (la bonne reponse est en premiere position)
    Inputs:
       execution (list): liste contennant les executions du programme avec les differents appels
       answerPath (str) : chemin d'acces du fichier contenant les mauvaises reponses
    Outputs:
        reponses (liste) : liste de liste representant les differentes questions
    """
    reponses = []

    with open(path_reponse,"r") as fichier_reponses_prof:
        reponses_prof = fichier_reponses_prof.readlines()
        reponses_prof = [el.replace("\n", "") for el in reponses_prof]

    for e in execution:
        reponse = [e]
        exec_copy = execution.copy()
        exec_copy.remove(e)
        reponses_potentielles = exec_copy + reponses_prof

        while len(reponse) < 4 and len(reponses_potentielles) > 0:
            reponse_potentielle = reponses_potentielles.pop(randrange(len(reponses_potentielles)))

            if reponse_potentielle not in reponse:
                reponse.append(reponse_potentielle)

        while len(reponse) < 4:
            reponse.append("Error")

        reponses.append(reponse)
        
    return reponses
