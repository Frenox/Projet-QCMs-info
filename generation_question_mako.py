from mako.template import Template
from random import * 
def generate_question(indice,programme,question,reponses):
  enonce = r'''
  \element{categorie${indice}}{
    \begin{question}{cat${indice}-quest${indice}}\bareme{formula=NBC-0.5*NMC} 
      ${question} 
      ##la question

  \inputminted[firstline=1, lastline=5]{python}{${programme}}

      \begin{reponseshoriz}
      % for elt in reponses:
        ${elt}
        % endfor
      \end{reponseshoriz} 
    \end{question}
  }
  '''
  reponses = [r"\bonne{" + reponses[0] + "}"] + [r"\mauvaise{" + elt+ "}" for elt in reponses[1:4]]
  shuffle(reponses)
  return Template(enonce).render(indice = indice,programme = programme,question = question,reponses = reponses)
indice = 1
programme = "test1.py"
question = "Que renvoie ce programme ?"
"""
solution = "3"
faux = ["1","2","4"]
"""
reponses = ["3","1","2","4"] #la bonne réponse est la première dans la liste
print(generate_question(indice,programme,question,reponses))
