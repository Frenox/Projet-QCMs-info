import json

def getKnownLanguages(): 
    with open('data/donneesLangages.json', 'r') as json_file:
        data = json.load(json_file)
        return data