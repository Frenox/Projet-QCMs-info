from os import *
from generation_variable import *

def execution():
    outputType = askOutputType()
    filePath = askFilePath()
    codeFile = formatage_fichier(filePath)



def askOutputType():
    out = input("Selectionnez votre type de formattage (AMC ou Moodle): ")
    if out.lower() in ["moodle", "amc"]:
        return out
    else:
        print("Ce n'est pas une option valide")
        return askOutputType()
    
def askFilePath():
    filPath = input("Entrez la localisation du fichier a executer: ")
    if path.exists(filPath):
        return filPath
    else:
        print("Le fichier n'existe pas")
        return askFilePath()
    
execution()