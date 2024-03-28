from mako.template import Template
from random import * 
def generate_question(programme,question,reponses,typeOutput,typeMinted,typeQuestion = None):
  if typeOutput == "amc":
    enonce = r'''
      \begin{question}{question}
        ${question} 
        \inputminted[firstline=1, lastline=5]{${langage}}{${programme}}
      \begin{reponseshoriz}
        % for elt in reponses:
          ${elt}
          % endfor
        \end{reponseshoriz} 
      \end{question}
    '''
  elif typeOutput == "moodle":
    main = r'''
      {${question}}
      ${programme}
      % for elt in reponses:
            ${elt}
            % endfor
    '''
    if typeQuestion == "multi":
      enonce = r'\begin{multi}' + main+ r'\end{multi}'
    elif typeQuestion == "short":
      enonce = r'\begin{shortanswer}[usecase]' + main+ r'\end{shortanswer}'

  if typeOutput == "amc":
    reponses_format= [r"\bonne{" + reponses[0] + "}"] + [r"\mauvaise{" + elt+ "}" for elt in reponses[1:4]]
  elif typeOutput == "moodle":
    if typeQuestion == "multi":
      reponses_format = [r"\item*"+ reponses[0]] + [r"\item" + elt for elt in reponses[1:4]]
    elif typeQuestion == "short":
      reponses_format = [r"\item" + elt for elt in reponses]
  #shuffle(reponses_format)
  return Template(enonce).render(programme = programme,question = question,reponses = reponses_format,langage = typeMinted )

def generate_categorie(nom,liste_questions):
  code = r'''\element{${nom}}{
  % for elt in questions:
  ${elt}
  % endfor
  }
    '''
  return Template(code).render(nom = nom,questions = liste_questions )


"""
indice = 1
programme = "test1.py"
question = "Que renvoie ce programme ?"
reponses = ["3","1","2","4"] #la bonne réponse est la première dans la liste
reponse2= ["3"]
question1 = generate_question(programme,question,reponse2,"amc","python")
question2 = generate_question(programme,question,reponse2,"amc","python")
print(generate_categorie("cat",[question1,question2]))
"""
