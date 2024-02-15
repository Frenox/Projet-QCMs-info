def entier(x):
    global a
    a = x
    #print(a)

a = None


#print(newcontenu)

def formatage_fichier(nom_fichier):
    
    global a
    with open(nom_fichier, "r") as fichier:
        contenu = fichier.read()
        #print(contenu)
    
    symbole = '$'
    insymbole = False
    instruction = ''
    newcontenu = ''
    for i in contenu:
        if i == symbole:
            insymbole = not(insymbole)
            if insymbole:
                instruction = ''
            if insymbole == False:
                #print(instruction)
                try:
                    exec(instruction)
                except NameError:
                    print("   ʌ \n  / \\ \n / | \\ \n/__•__\\")
                    print("Une instruction entre '$' n'est pas correcte!\n")
                #print(a)
                newcontenu += str(a) 
                a = None
        else:
            if insymbole:
                instruction += i
            else:
                newcontenu += i
        
    with open("test_texte_fin.txt", "w") as fichier:
        fichier.write(newcontenu)
        print(newcontenu)
  

formatage_fichier("test_texte.txt")
