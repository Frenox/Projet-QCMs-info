import json

def getKnownLanguages(): 
    with open('donneesLangages.json', 'r') as json_file:
        data = json.load(json_file)
        return data