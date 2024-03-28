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
    languageData = getKnownLanguages()[codeLanguage]
    codeFile = formatage_fichier(filePath)

    with open(executionPath, "r") as execFile:
        executionFile = execFile.read()
        globalFile = codeFile + "\n" + executionFile 

        fileReturn = execution_docker(globalFile, languageData[:3])
        answerLists = rep(fileReturn, answerPath)

        mintedDisplayType = languageData[-1] if len(languageData) == 4 else "text"

        for i in range(len(answerLists)):
            question = generate_question("codeFile{languageData[0]}", "Que renvoie ce programme?", answerLists[i], outputType, mintedDisplayType, questionType)
            with open(f'Outputs/test{i}.txt', 'w') as f:
                f.write(question)
                f.close()

        with open(f'Outputs/codeFile{languageData[0]}', 'w') as f:
                f.write(codeFile)
                f.close()

    execFile.close()


main(args.outputType, args.codeLanguage, args.filePath, args.answerPath, 'multi')