import subprocess

def execution(script, langue):
    filename = 'MonFichier' + langue[1]
    
    with open(filename, 'w') as f:
        f.write(script)
        
    commande = [langue[0], filename]
    
    result = subprocess.run(commande, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    
    return result.stdout.splitlines()
