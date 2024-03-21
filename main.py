import os
import sys
from generation_variable import *
from donneesJSON import *
from Execution_docker import *
from generation_question_mako import generate_question
from execution_avec_subproces import execution
from reponse import rep

def main(outputType, codeLanguage, filePath, answerPath):
    codeFile = formatage_fichier(filePath)
    languageData = getLanguageData(codeLanguage)
    fileReturn = execution(codeFile, languageData)
    answerLists = rep(fileReturn, answerPath)

    for i in range(len(answerLists)):
        question = generate_question("fichier.py", "Que renvoie ce programme?", answerLists[i], outputType)

        with open(f'test{i}.txt', 'w') as f:
            f.write(question)
            f.close()


def getLanguageData(language):
    return getKnownLanguages()[language]

if __name__ == "__main__":
    if len(sys.argv) > 1:
        outputType = sys.argv[1] 
        codeLanguage = sys.argv[2]
        filePath = sys.argv[3]
        answerPath = sys.argv[4]
        main(outputType, codeLanguage, filePath, answerPath)
    else:
        main("moodle", "pythonA", r"C:\Users\maxim\Desktop\INP\2A\Projet\Projet-QCMs-info\codeFile.txt", r"C:\Users\maxim\Desktop\INP\2A\Projet\Projet-QCMs-info\answersFile.txt")