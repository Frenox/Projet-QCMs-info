import subprocess

def execution(script, langue):
    filename = 'MonFichier' + langue[1]
    
    with open(filename, 'w') as f:
        f.write(script)
        
    commande = [langue[0], filename]
    
    result = subprocess.run(commande, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    
    return result.stdout

# Exemple d'utilisation avec un script Python simple
stdout = execution("print('hello world')\nprint('2')", ["python", ".py"])

print(stdout)
