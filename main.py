from os import *
from generation_variable import *
from donneesJSON import *
from generation_question_mako import generate_question

def execution():
    splashScreen()
    outputType = askOutputType()
    codeLanguage = askLanguage()
    filePath = askFilePath("a executer")
    answerPath = askFilePath("contenant les appels de la fonction")
    codeFile = formatage_fichier(filePath)

    ##generate_question(1, "fichier.py", "Que renvoie ce programme?", reponses)

def splashScreen():
    print("----------------------------------------------------------------------")
    print("                    Bienvenue sur QCM Generator                       ")
    print("\n\n")
    print("                       -By Cerrad las sopas-                          ")
    print("----------------------------------------------------------------------")
    print()

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
    languageData = getKnownLanguages()
    languageList = languageData.keys()
    language = input("Selectionnez le langage (et la version eventuelle) de l'algorithme fourni (ou entrez 'l' pour avoir la liste des langages disponibles): ")
    
    if language == "l":
        for el in languageList:
            print(el)
        return askLanguage()
    elif language in languageList:
        return languageData[language]
    else:
        print("Ce n'est pas une option valide")
        return askLanguage()

execution()