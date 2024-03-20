from mako.template import Template
from random import * 
def generate_question(programme,question,reponses,extension):
  if extension == "amc":
    enonce = r'''
      \begin{question}{question}
        ${question} 
        ##la question

    ${programme}

        \begin{reponseshoriz}
        % for elt in reponses:
          ${elt}
          % endfor
        \end{reponseshoriz} 
      \end{question}
    '''
  elif extension == "moodle":
    enonce = r'''
    \begin{multi}{${question}}
    ${programme}
    % for elt in reponses:
          ${elt}
          % endfor
  \end{multi} 
    '''
  if extension == "amc":
    reponses_format= [r"\bonne{" + reponses[0] + "}"] + [r"\mauvaise{" + elt+ "}" for elt in reponses[1:4]]
  elif extension == "moodle":
    reponses_format = [r"\item*"+ reponses[0]] + [r"\item" + elt for elt in reponses[1:4]]
  shuffle(reponses_format)
  return Template(enonce).render(programme = programme,question = question,reponses = reponses_format)
indice = 1
programme = "test1.py"
question = "Que renvoie ce programme ?"
"""
solution = "3"
faux = ["1","2","4"]
"""
reponses = ["3","1","2","4"] #la bonne réponse est la première dans la liste
print(generate_question(programme,question,reponses,"AMC"))
