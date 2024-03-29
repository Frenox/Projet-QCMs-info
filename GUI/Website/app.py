from flask import Flask, request, render_template, jsonify

from modules.data import *
from modules.execution import *
from modules.generation import *
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
            
            languageData = getKnownLanguages()[codeLanguage]
            codeFile = formatage_fichier(temp_files_paths[0])

            with open(temp_files_paths[1], "r") as execFile:
                executionFile = execFile.read()
                categoryList, cleanExecFile = handleCategories(executionFile)
                globalFile = codeFile + "\n" + cleanExecFile 

                fileReturn = execution_docker(globalFile, languageData[:3])
                answerLists = rep(fileReturn, temp_files_paths[2])

                mintedDisplayType = languageData[-1] if len(languageData) == 4 else "text"

                questions = []
                for i in range(len(answerLists)):
                    question = generate_question(f"codeFile{languageData[0]}", "Que renvoie ce programme?", answerLists[i], outputType, mintedDisplayType, 'multi')
                    questions.append(question)

                questionsDict = handleQuestionGroups(questions,categoryList)
                for category, questions in questionsDict.items():
                    categoryString = generate_categorie(category,questions)
                    with open(f'Outputs/{category}.txt', 'w') as f:
                        f.write(categoryString) ## Cree le fichier contenant la question
                        f.close()

                with open(f'Outputs/codeFile{languageData[0]}', 'w') as f:
                        f.write(codeFile) ## Cree le fichier contenant le code (pour affichage en latex)
                        f.close()

                execFile.close()
                return jsonify({'result': render_template('qcm-result.html', qcmList=questions, fileList = files)})
        finally:
            for path in temp_files_paths:
                os.remove(path)
            pass

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

@app.route('/download/<filename>', methods=['GET'])
def download(filename):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), as_attachment=True)   

if __name__ == "__main__":
    app.run(debug=True)
