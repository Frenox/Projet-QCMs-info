from os import *
from generation_variable import *
from donneesJSON import *

def execution():
    outputType = askOutputType()
    codeLanguage = askLanguage()
    filePath = askFilePath("a executer")
    filePath = askFilePath("contenant les appels de la fonction")
    codeFile = formatage_fichier(filePath)



def askOutputType():
    type = input("Selectionnez votre type de formattage (AMC ou Moodle): ")
    if type.lower() in ["moodle", "amc"]:
        return type
    else:
        print("Ce n'est pas une option valide")
        return askOutputType()
    
def askFilePath(fileType):
    filPath = input(f"Entrez la localisation du fichier {fileType}: ")
    if path.exists(filPath):
        return filPath
    else:
        print("Le fichier n'existe pas")
        return askFilePath(fileType)
    
def askLanguage():
    languageData = getKnownLanguages() ##Need to get the list of the JSON keys
    languageList = languageData.keys()
    language = input("Selectionnez le langage (et la version eventuelle) de l'algorithme fourni: ")
    if language in languageList:
        return language
    else:
        print("Ce n'est pas une option valide")
        return askLanguage()

execution()