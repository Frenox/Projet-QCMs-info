from os import *
import sys
from generation_variable import *
from donneesJSON import *
from generation_question_mako import generate_question
from execution_avec_subproces import execution
from reponse import rep

def main(outputType, codeLanguage, filePath, answerPath):
    codeFile = formatage_fichier(filePath)
    languageData = getLanguageData(codeLanguage)
    fileReturn = execution(codeFile, languageData)
    answerLists = rep(fileReturn, answerPath)

    questionsString = []
    for answers in answerLists:
        questionsString.append(generate_question("fichier.py", "Que renvoie ce programme?", answers, outputType))
    
    return questionsString


def getLanguageData(language):
    return getKnownLanguages()[language]

if __name__ == "__main__":
    if len(sys.argv) > 1:
        outputType = sys.argv[1] 
        codeLanguage = sys.argv[2]
        filePath = sys.argv[3]
        answerPath = sys.argv[4]
        print(main(outputType, codeLanguage, filePath, answerPath))
    else:
        print(main("moodle", "pythonA", r"C:\Users\maxim\Desktop\INP\2A\Projet\Projet-QCMs-info\codeFile.txt", r"C:\Users\maxim\Desktop\INP\2A\Projet\Projet-QCMs-info\answersFile.txt"))