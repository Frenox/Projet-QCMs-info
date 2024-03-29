import os
import sys
from modules.data import *
from modules.execution import *
from modules.generation import *
import argparse


"""parser = argparse.ArgumentParser()
parser.add_argument('outputType', type=str)
parser.add_argument('codeLanguage', type=str)
parser.add_argument('filePath', type=str)
parser.add_argument('executionPath', type=str)
parser.add_argument('answerPath', type=str)

args = parser.parse_args()"""

def main(outputType, codeLanguage, filePath, executionPath, answerPath, questionType):
    languageData = getKnownLanguages()[codeLanguage] ## Recupere les donnees associees au langage demande
    codeFile = formatage_fichier(filePath) ## Remplace les balises par du code dans le fichier donne

    with open(executionPath, "r") as execFile:
        executionFile = execFile.read()
        categoryList, cleanExecFile = handleCategories(executionFile)
        globalFile = codeFile + "\n" + cleanExecFile ## Cree le fichier global contenant le code et les appels a executer

        fileReturn = execution_docker(globalFile, languageData[:3]) ## Execute le fichier sur docker (supprime le 4eme element de la liste s'il existe (non necessaire pour cette partie))
        answerLists = rep(fileReturn, answerPath) ## Genere les listes des reponses pour chaque question

        mintedDisplayType = languageData[-1] if len(languageData) == 4 else "text" ## Recupere le type de langage (pour le formatage Latex)

        formatedQuestionsList = []
        for i in range(len(answerLists)):
            formatedQuestionsList.append(generate_question(f"codeFile{languageData[0]}", "Que renvoie ce programme?", answerLists[i], outputType, mintedDisplayType, questionType)) ## Genere le formattage de la question
            
        questionsDict = handleQuestionGroups(formatedQuestionsList,categoryList)
        for category, questions in questionsDict.items():
            categoryString = generate_categorie(category,questions)
            with open(f'Outputs/{category}.txt', 'w') as f:
                f.write(categoryString) ## Cree le fichier contenant la question
                f.close()

        with open(f'Outputs/codeFile{languageData[0]}', 'w') as f:
                f.write(codeFile) ## Cree le fichier contenant le code (pour affichage en latex)
                f.close()

    execFile.close()

def handleCategories(executionFile):
    lines = executionFile.split("\n")

    categoryList = []
    currentCategory = "Default"

    callsString = ""

    for line in lines:
        if line.replace(" ","") != "\n" and len(line) > 0:
            if line[0] == "#":
                currentCategory = line[1:]
            else:
                callsString += line + "\n"
                categoryList.append(currentCategory)
    return categoryList, callsString


def handleQuestionGroups(questionsList, categoryList):
    questionsDict = {}
    for i in range(len(categoryList)):
        questionsDict[categoryList[i]] = questionsDict.get(categoryList[i], []) + [questionsList[i]]
    return questionsDict



main("amc", "python3", r"C:\Users\maxim\Desktop\INP\2A\Projet\Projet-QCMs-info\ShellProgram\tests_files\Codefiles\codeFile.txt", r"C:\Users\maxim\Desktop\INP\2A\Projet\Projet-QCMs-info\ShellProgram\tests_files\executionFiles\executionFile.txt", r"C:\Users\maxim\Desktop\INP\2A\Projet\Projet-QCMs-info\ShellProgram\tests_files\answerFile\answersFile.txt", "multi")
##main(args.outputType, args.codeLanguage, args.filePath, args.answerPath, 'multi')