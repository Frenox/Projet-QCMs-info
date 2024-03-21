from flask import Flask
from flask import request, render_template

from os import *
from generation_variable import *
from donneesJSON import *
from generation_question_mako import generate_question
from execution_avec_subproces import execution
from Execution_docker import execution_docker
from reponse import rep

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/process_qcm', methods=['POST'])
def process_qcm():
    if request.method == 'POST':
        filePath = request.files['source_file'].filename
        answerPath = request.files['answer_file'].filename
        outputType = request.form['output_type']
        codeLanguage = request.form.get('format_select')
    
        codeFile = formatage_fichier(filePath)
        fileReturn = execution_docker(codeFile, codeLanguage)
        answerLists = rep(fileReturn, answerPath)

        questionsString = []
        for answers in answerLists:
            questionsString.append(generate_question("fichier.py", "Que renvoie ce programme?", answers, outputType))
    
        return questionsString
    
    #return f"Qcm généré avec succès! Type de QCM : {outputType}. Format : {codeLanguage}. Fichier source : {filePath}. Fichier reponse : {answerPath}"