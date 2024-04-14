from mako.template import Template
from random import * 
def generate_question(programme,question,reponses,typeOutput,typeMinted,category,typeQuestion = None):
  if typeOutput == "amc":
    enonce = r'''
    \element{${category}}{
      \begin{question}{question}
        ${question} 
        \inputminted[firstline=1, lastline=5]{${langage}}{${programme}}
      \begin{reponseshoriz}
        % for elt in reponses:
          ${elt}
          % endfor
        \end{reponseshoriz} 
      \end{question}
      }
    '''
    reponses_format= [r"\bonne{" + reponses[0] + "}"] + [r"\mauvaise{" + elt+ "}" for elt in reponses[1:4]]
  elif typeOutput == "moodle":
    enonce = r'''\setsubcategory{''' + category + '}'
    main = r'''
      {${question}}
      \inputminted[firstline=1, lastline=5]{${langage}}{${programme}}
      % for elt in reponses:
            ${elt}
            % endfor
    '''
    if typeQuestion == "multi":
      enonce += r'\begin{multi}' + main+ r'\end{multi}'
      reponses_format = [r"\item*"+ reponses[0]] + [r"\item" + elt for elt in reponses[1:4]]
    elif typeQuestion == "short":
      enonce += r'\begin{shortanswer}[usecase]' + main+ r'\end{shortanswer}'
      reponses_format = [r"\item" + elt for elt in reponses]
  return Template(enonce).render(programme = programme,question = question,reponses = reponses_format,langage = typeMinted,category = category)


def generate_category(nom,categories):
  code = r'''
  % for elt in categories.keys():
  \setgroupmode{${elt}}{cyclic}
  \shufflegroup{${elt}}
  % for _ in range(categories[elt]):
  \element{${nom}}{
  \restituegroupe[1]{${elt}}
  }
  % endfor
  % endfor
    '''
  return Template(code).render(nom = nom,categories = categories )



"""
print(generate_question("test1.py","Que ?","47","moodle","python","newCat","short"))
print(generate_category("Category3",{"Category2":2,"Category1":1}))
"""
