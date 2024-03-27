import json
import os
# Chemin du répertoire courant où se trouve donneesJSON.py
current_directory = os.path.dirname(os.path.abspath(__file__))
# Construction du chemin vers donneesLangages.json
json_path = os.path.join(current_directory, 'donneesLangages.json')

def getKnownLanguages(): 
    with open(json_path, 'r') as json_file:
        data = json.load(json_file)
        return data