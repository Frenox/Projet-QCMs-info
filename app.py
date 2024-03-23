from flask import Flask, request, render_template, send_from_directory

from generation_variable import *
from donneesJSON import *
from Execution_docker import *
from generation_question_mako import generate_question
from execution_avec_subproces import execution
from reponse import rep


app = Flask(__name__)



@app.route("/")
def home():
    # Chemin vers le fichier JSON dans le répertoire data
    json_path = os.path.join(app.root_path, 'data', 'donneesLangages.json')
    with open(json_path, 'r') as json_file:
        langages_data = json.load(json_file)
    
    # Passer les noms des langages au template index.html
    return render_template('index.html', langages=langages_data.keys())



@app.route('/process_qcm', methods=['POST'])
def process_qcm():
    if request.method == 'POST':
        outputType = request.form['output_type']
        codeLanguage = request.form.get('format_select')
        filePath = request.files['source_file'].filename
        answerPath = request.files['answer_file'].filename
    
        codeFile = formatage_fichier(filePath)
        languageData = getLanguageData(codeLanguage)
        fileReturn = execution_docker(codeFile, codeLanguage)
        answerLists = rep(fileReturn, answerPath)

        for i in range(len(answerLists)):
            questions = ''
            questions += generate_question("fichier.py", "Que renvoie ce programme?", answerLists[i], outputType, 'multi')
            return(questions)
    
    #return f"Qcm généré avec succès! Type de QCM : {outputType}. Format : {codeLanguage}. Fichier source : {filePath}. Fichier reponse : {answerPath}"

def getLanguageData(language):
    return getKnownLanguages()[language]