from random import *

def rep(execution,path_reponse):
    reponses = []

    with open(path_reponse,"r") as fichier_reponses_prof:
        reponses_prof = fichier_reponses_prof.readlines()

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
