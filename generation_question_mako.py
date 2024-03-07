from mako.template import Template
from random import * 
def generate_question(indice,programme,question,solution,faux):
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
  reponses = [r"\bonne{" + reponse + "}"] + [r"\mauvaise{" + elt+ "}" for elt in faux][:3]
  shuffle(reponses)
  return Template(enonce).render(indice = indice,programme = programme,question = question,reponses = reponses)
indice = 1
programme = "test1.py"
question = "Que renvoie ce programme ?"
solution = "3"
faux = ["1","2","4"]
print(generate_question(indice,programme,question,solution,faux))
