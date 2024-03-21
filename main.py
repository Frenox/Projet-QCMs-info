import os
import sys
from generation_variable import *
from donneesJSON import *
from Execution_docker import *
from generation_question_mako import generate_question
from execution_avec_subproces import execution
from reponse import rep
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('outputType', type=str)
parser.add_argument('codeLanguage', type=str)
parser.add_argument('filePath', type=str)
parser.add_argument('answerPath', type=str)
parser.add_argument('--GUIMode', type=str)

args = parser.parse_args()

def main(outputType, codeLanguage, filePath, answerPath, questionType):
    codeFile = formatage_fichier(filePath)
    languageData = getLanguageData(codeLanguage)
    fileReturn = execution_docker(codeFile, languageData)
    answerLists = rep(fileReturn, answerPath)

    for i in range(len(answerLists)):
        question = generate_question("fichier.py", "Que renvoie ce programme?", answerLists[i], outputType, questionType)
        if args.GUIMode:
            return(question)
        else:
            with open(f'test{i}.txt', 'w') as f:
                f.write(question)
                f.close()


def getLanguageData(language):
    return getKnownLanguages()[language]

main(args.outputType, args.codeLanguage, args.filePath, args.answerPath, 'multi')