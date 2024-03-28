import os
import sys
from modules.data import *
from modules.execution import *
from modules.generation import *
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('outputType', type=str)
parser.add_argument('codeLanguage', type=str)
parser.add_argument('filePath', type=str)
parser.add_argument('executionPath', type=str)
parser.add_argument('answerPath', type=str)

args = parser.parse_args()

def main(outputType, codeLanguage, filePath, executionPath, answerPath, questionType):
    languageData = getKnownLanguages()[codeLanguage] ## Recupere les donnees associees au langage demande
    codeFile = formatage_fichier(filePath) ## Remplace les balises par du code dans le fichier donne

    with open(executionPath, "r") as execFile:
        executionFile = execFile.read()
        globalFile = codeFile + "\n" + executionFile ## Cree le fichier global contenant le code et les appels a executer

        fileReturn = execution_docker(globalFile, languageData[:3]) ## Execute le fichier sur docker (supprime le 4eme element de la liste s'il existe (non necessaire pour cette partie))
        answerLists = rep(fileReturn, answerPath) ## Genere les listes des reponses pour chaque question

        mintedDisplayType = languageData[-1] if len(languageData) == 4 else "text" ## Recupere le type de langage (pour le formatage Latex)

        for i in range(len(answerLists)):
            question = generate_question("codeFile{languageData[0]}", "Que renvoie ce programme?", answerLists[i], outputType, mintedDisplayType, questionType) ## Genere le formattage de la question
            with open(f'Outputs/test{i}.txt', 'w') as f:
                f.write(question) ## Cree le fichier contenant la question
                f.close()

        with open(f'Outputs/codeFile{languageData[0]}', 'w') as f:
                f.write(codeFile) ## Cree le fichier contenant le code (pour affichage en latex)
                f.close()

    execFile.close()


main(args.outputType, args.codeLanguage, args.filePath, args.answerPath, 'multi')