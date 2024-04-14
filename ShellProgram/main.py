import os
import sys
import argparse

sys.path.append(os.path.abspath('..'))

from common_modules.data import *
from common_modules.generation import *
from common_modules.execution import *

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
        categoryList, callsList = handleCategories(questionName, executionFile)
        
        fileReturn = [] ## Liste des renvois
        files = [] ## Liste des fichiers
        for call in callsList:
            globalFile = codeFile.replace("_[CodeInsertion]_" ,call) ## Cree le fichier global contenant le code et la partie variable
            files.append(globalFile) ## Sauvegarde le fichier

            fileReturn += execution_docker(globalFile, languageData[:3]) ## Execute le fichier sur docker (supprime le 4eme element de la liste s'il existe (non necessaire pour cette partie))

        answerLists = rep(fileReturn, answerPath) ## Genere les listes des reponses pour chaque question

        mintedDisplayType = languageData[-1] if languageData[-1] != None else "text" ## Recupere le type de langage (pour le formatage Latex)

        formatedQuestionsList = []
        for i in range(len(answerLists)):
            formatedQuestionsList.append(generate_question(f"codeFile_{questionName}{languageData[0]}", "Que renvoie ce programme?", answerLists[i], outputType, mintedDisplayType, categoryList[i], questionType)) ## Genere le formattage de la question
            
        questionsDict = handleQuestionGroups(categoryList)
        categoryString = generate_category(questionName, questionsDict)

        with open(f"Outputs/questionFile_{questionName}.txt", "w") as f:
            for question in formatedQuestionsList:
                f.write(question + "\n") ## Ecrit chaque question dans le fichier Latex
            f.write(categoryString) ## Ecrit le groupe global des questions
        f.close()

        for i in range(len(files)):
            with open(f'Outputs/codeFile_{questionName}{i+1}{languageData[0]}', 'w') as f:
                    f.write(files[i]) ## Cree le fichier contenant chaque code (pour affichage en latex)
                    f.close()

    execFile.close()

def handleCategories(questionName, executionFile):
    lines = executionFile.split("\n")

    categoryList = []
    currentCategory = "Default"

    callsList = []

    for line in lines:
        if line.replace(" ","") != "\n" and len(line) > 0:
            if line[0] == "#":
                currentCategory = questionName + "_" + line[1:]
            else:
                callsList.append(line)
                categoryList.append(currentCategory)
    return categoryList, callsList


def handleQuestionGroups(categoryList):
    questionsDict = {}
    for category in categoryList:
        questionsDict[category] = questionsDict.get(category, 0) + 1
    return questionsDict



main(args.questionName, args.outputType, args.codeLanguage, args.filePath, args.executionPath, args.answerPath, args.questionType)