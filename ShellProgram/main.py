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
parser.add_argument('answerPath', type=str)
parser.add_argument('--GUIMode', type=str, help='argument optionnel pour la version GUI')

args = parser.parse_args()
lang_config = getKnownLanguages()

def main(outputType, codeLanguage, filePath, answerPath, questionType):
    codeFile = formatage_fichier(filePath)
    fileReturn = execution_docker(codeFile, codeLanguage, lang_config)
    answerLists = rep(fileReturn, answerPath)

    for i in range(len(answerLists)):
        question = generate_question("fichier.py", "Que renvoie ce programme?", answerLists[i], outputType, questionType)
        if args.GUIMode:
            return(question)
        else:
            with open(f'Outputs/test{i}.txt', 'w') as f:
                f.write(question)
                f.close()



main(args.outputType, args.codeLanguage, args.filePath, args.answerPath, 'multi')