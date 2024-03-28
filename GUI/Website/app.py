from flask import Flask, request, render_template, send_from_directory,jsonify

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
        filePath = request.files['source_file'].filename
        answerPath = request.files['answer_file'].filename
    
        codeFile = formatage_fichier(filePath)
        fileReturn = execution_docker(codeFile, codeLanguage, getKnownLanguages())
        answerLists = rep(fileReturn, answerPath)
        questions = []
        for i in range(len(answerLists)):
            questions.append(generate_question("fichier.py", "Que renvoie ce programme?", answerLists[i], outputType, 'multi'))
        return jsonify({'result': render_template('qcm-result.html', qcmList=questions)}) 
    
def getLanguageData(language):
    return getKnownLanguages()[language]

if __name__ == "__main__":
    app.run(debug=True)
