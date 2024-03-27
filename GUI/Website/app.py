from flask import Flask, request, render_template, send_from_directory,jsonify

from modules.data import *
from modules.execution import *
from modules.generation import *
app = Flask(__name__)

from flask import Flask, request, render_template, send_from_directory, jsonify, abort




@app.route('/process_qcm', methods=['POST'])
def process_qcm():
    try:
        outputType = request.form['output_type']
        codeLanguage = request.form.get('format_select')
        source_file = request.files['source_file']
        answer_file = request.files['answer_file']
        
        if source_file.filename == '' or answer_file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Ajouter une validation pour codeLanguage si nécessaire

        filePath = source_file.filename
        answerPath = answer_file.filename
    
        codeFile = formatage_fichier(filePath)
        fileReturn = execution_docker(codeFile, codeLanguage, getKnownLanguages())
        answerLists = rep(fileReturn, answerPath)
        
        questions = []
        for i in range(len(answerLists)):
            questions.append(generate_question("fichier.py", "Que renvoie ce programme?", answerLists[i], outputType, 'multi'))
            
        return jsonify({'result': render_template('qcm-result.html', qcmList=questions)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route("/")
def home():
    # Passer les noms des langages au template index.html
    return render_template('index.html', langages=getKnownLanguages().keys())

    
def getLanguageData(language):
    return getKnownLanguages()[language]

if __name__ == "__main__":
    app.run(debug=True)
