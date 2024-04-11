import os
import sys
from modules.data import *
from modules.execution import *
from modules.generation import *
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('questionName', type=str)
parser.add_argument('outputType', type=str)
parser.add_argument('codeLanguage', type=str)
parser.add_argument('filePath', type=str)
parser.add_argument('executionPath', type=str)
parser.add_argument('answerPath', type=str)
parser.add_argument("questionType", nargs='?', default="multi")

args = parser.parse_args()

def main(questionName, outputType, codeLanguage, filePath, executionPath, answerPath, questionType):
    languageData = list(getKnownLanguages()[codeLanguage].values()) ## Recupere les donnees associees au langage demande
    codeFile = formatage_fichier(filePath) ## Remplace les balises par du code dans le fichier donne

    with open(executionPath, "r") as execFile:
        executionFile = execFile.read()
        categoryList, cleanExecFile = handleCategories(questionName, executionFile)
        globalFile = codeFile + "\n" + cleanExecFile ## Cree le fichier global contenant le code et les appels a executer

        fileReturn = execution_docker(globalFile, languageData[:3]) ## Execute le fichier sur docker (supprime le 4eme element de la liste s'il existe (non necessaire pour cette partie))
        answerLists = rep(fileReturn, answerPath) ## Genere les listes des reponses pour chaque question

        mintedDisplayType = languageData[-1] if languageData[-1] != None else "text" ## Recupere le type de langage (pour le formatage Latex)

        formatedQuestionsList = []
        for i in range(len(answerLists)):
            formatedQuestionsList.append(generate_question(f"codeFile_{questionName}{languageData[0]}", "Que renvoie ce programme?", answerLists[i], outputType, mintedDisplayType, questionType)) ## Genere le formattage de la question
            
        questionsDict = handleQuestionGroups(formatedQuestionsList,categoryList)

        with open(f"Outputs/questionFile_{questionName}.txt", "w") as f:
            for category, questions in questionsDict.items():
                categoryString = generate_categorie(category,questions)
                f.write(categoryString) ## Cree le fichier contenant la question
        f.close()

        with open(f'Outputs/codeFile_{questionName}{languageData[0]}', 'w') as f:
                f.write(codeFile) ## Cree le fichier contenant le code (pour affichage en latex)
                f.close()

    execFile.close()

def handleCategories(questionName, executionFile):
    lines = executionFile.split("\n")

    categoryList = []
    currentCategory = "Default"

    callsString = ""

    for line in lines:
        if line.replace(" ","") != "\n" and len(line) > 0:
            if line[0] == "#":
                currentCategory = questionName + "_" + line[1:]
            else:
                callsString += line + "\n"
                categoryList.append(currentCategory)
    return categoryList, callsString


def handleQuestionGroups(questionsList, categoryList):
    questionsDict = {}
    for i in range(len(categoryList)):
        questionsDict[categoryList[i]] = questionsDict.get(categoryList[i], []) + [questionsList[i]]
    return questionsDict



main(args.questionName, args.outputType, args.codeLanguage, args.filePath, args.executionPath, args.answerPath, args.questionType)