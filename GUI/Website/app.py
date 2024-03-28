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
                temp_file = tempfile.NamedTemporaryFile(delete=False)
                file.save(temp_file.name)
                temp_files_paths.append(temp_file.name)
            
            languageData = getKnownLanguages()[codeLanguage]
            codeFile = formatage_fichier(temp_files_paths[0])

            with open(temp_files_paths[1], "r") as execFile:
                executionFile = execFile.read()
                globalFile = codeFile + "\n" + executionFile 

                fileReturn = execution_docker(globalFile, languageData[:3])
                answerLists = rep(fileReturn, temp_files_paths[2])

                questions = []
                for i in range(len(answerLists)):
                    question = generate_question("codeFile{languageData[0]}", "Que renvoie ce programme?", answerLists[i], outputType, 'multi')
                    questions.append(question)
                execFile.close()
                return jsonify({'result': render_template('qcm-result.html', qcmList=questions, fileList = files)})
        finally:
            #for path in temp_files_paths:
                #os.remove(path)
            pass

@app.route('/download/<filename>', methods=['GET'])
def download(filename):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), as_attachment=True)   

if __name__ == "__main__":
    app.run(debug=True)
