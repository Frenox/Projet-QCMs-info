from flask import Flask, request, render_template, jsonify
import tempfile
import os, sys

sys.path.append(os.path.abspath('..'))

from ShellProgram.main import *

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

            questionType = "multi"       # change questionType to variable
            questionName = "NomQCMTemporaire" # change questionName to variable
            main(questionName, outputType, codeLanguage, temp_files_paths[0], temp_files_paths[1], temp_files_paths[2], questionType, GUImode="True")
            #return jsonify({'result': render_template('qcm-result.html', qcmList=questions, fileList = files)})
            return jsonify({'result': render_template('download.html', name = questionName)})
        finally:
            for path in temp_files_paths:
                os.remove(path)
            pass

if __name__ == "__main__":
    app.run(debug=True)
