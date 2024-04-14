from flask import Flask, request, render_template, jsonify
import tempfile
import os, sys

sys.path.append(os.path.abspath('..'))

from common_modules.data import *
from common_modules.generation import *
from common_modules.execution import *

app = Flask(__name__)

@app.route("/")
def home():
    # Passer les noms des langages au template index.html
    return render_template('index.html', langages=getKnownLanguages().keys())

@app.route('/process_qcm', methods=['POST'])
def process_qcm():
    if request.method == 'POST':
        outputType = request.form['output_type']
        codeLanguage = request.form.get('format_select')
        files = []
        temp_files_paths = []
        source_file = request.files['source_file']
        execution_file = request.files['calls_file']
        answer_file = request.files['answer_file']
        files.extend([source_file, execution_file, answer_file])
        
        try:
            for file in files:
                with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                    file.save(temp_file.name)
                    temp_files_paths.append(temp_file.name)
            
            languageData = list(getKnownLanguages()[codeLanguage].values()) ## Recupere les donnees associees au langage demande
            codeFile = formatage_fichier(temp_files_paths[0]) ## Remplace les balises par du code dans le fichier donne

            questionName = "NomQCMTemporaire" # change questionName to variable
            questionType = "multi"       # change questionType to variable

            with open(temp_files_paths[1], "r") as execFile:
                executionFile = execFile.read()
                categoryList, cleanExecFile = handleCategories(questionName, executionFile)
                globalFile = codeFile + "\n" + cleanExecFile ## Cree le fichier global contenant le code et les appels a executer

                fileReturn = execution_docker(globalFile, languageData[:3]) ## Execute le fichier sur docker (supprime le 4eme element de la liste s'il existe (non necessaire pour cette partie))
                answerLists = rep(fileReturn, temp_files_paths[2]) ## Genere les listes des reponses pour chaque question

                mintedDisplayType = languageData[-1] if languageData[-1] != None else "text" ## Recupere le type de langage (pour le formatage Latex)

                formatedQuestionsList = []
                for i in range(len(answerLists)):
                    question = generate_question(f"codeFile_{questionName}{languageData[0]}", "Que renvoie ce programme?", answerLists[i], outputType, mintedDisplayType, categoryList[i], questionType) ## Genere le formattage de la question
                    formatedQuestionsList.append(question)

                questionsDict = handleQuestionGroups(categoryList)
                categoryString = generate_category(questionName, questionsDict)

                print("App root path:", app.root_path, flush=True)
                print("Current Working Directory:", os.getcwd(), flush=True)

                with open(f"Website/static/download/questionFile_{questionName}.txt", "w") as f:
                    for question in formatedQuestionsList:
                        f.write(question + "\n")
                    f.write(categoryString)
                f.close()
        
                with open(f'Website/static/download/codeFile_{questionName}{languageData[0]}', 'w') as f:
                    f.write(codeFile) ## Cree le fichier contenant le code (pour affichage en latex)
                    f.close()

            execFile.close()
            #return jsonify({'result': render_template('qcm-result.html', qcmList=questions, fileList = files)})
            return jsonify({'result': render_template('download.html', name = questionName)})
        finally:
            for path in temp_files_paths:
                os.remove(path)
            pass

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

def handleQuestionGroups(categoryList):
    questionsDict = {}
    for category in categoryList:
        questionsDict[category] = questionsDict.get(category, 0) + 1
    return questionsDict

if __name__ == "__main__":
    app.run(debug=True)
