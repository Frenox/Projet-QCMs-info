from mako.template import Template
from random import * 
def generate_question(program,question,answers,typeOutput,typeMinted,category,typeQuestion = None):
  """
    Genere une question d'un QCM en latex au format moodle.sty ou AMC
    Inputs:
       *program(str): Nom du fichier contenant le programme utilise pour la question (ex: "program.py")
       *question (str) : Enonce de la question
       *answers(list): Liste des reponses, le premier element est la bonne reponse et les autres les mauvaises reponses(
       dans le cas d'une question à choix multiples)
       *typeOutput(str): Specifie le format qu'on souhaite (pour l'instant AMC ou moodle)
       *typeMinted(str): Precise le langage a rentre pour que minted mette en forme le code (ex: cpp pour un fichier en c++)
       *category (str) : Nom du groupe de la question, permet de regrouper des questions en AMC et moodle
       *typeQuestion(str): Precise le type de question pour moodle, pour l'instant seul les categories shortanswer(argument: short)
       et multi sont implementes
    Outputs:
        Template(enonce).render(...): str contenant le code latex correspondant a la question
    """
  if typeOutput == "amc":
    enonce = r'''
    \element{${category}}{
      \begin{question}{question}
        ${question} 
        \inputminted{${langage}}{${programme}}
      \begin{reponseshoriz}
        % for elt in answers:
          ${elt}
          % endfor
        \end{reponseshoriz} 
      \end{question}
      }
    '''
    answers_format= [r"\bonne{" + answers[0] + "}"] + [r"\mauvaise{" + elt+ "}" for elt in answers[1:4]]
  elif typeOutput == "moodle":
    enonce = r'''\setsubcategory{''' + category + '}'
    main = r'''
      {${programme}}
      ${question}
      \inputminted{${langage}}{${programme}}
      % for elt in answers:
            ${elt}
            % endfor
    '''
    if typeQuestion == "multi":
      enonce += r'\begin{multi}' + main+ r'\end{multi}'
      answers_format = [r"\item*"+ answers[0]] + [r"\item" + elt for elt in answers[1:4]]
    elif typeQuestion == "short":
      enonce += r'\begin{shortanswer}[usecase]' + main+ r'\end{shortanswer}'
      answers_format = [r"\item" + elt for elt in answers]
    else:
      return "format non pris en compte"
  else:
    return "format non pris en compte"
  return Template(enonce).render(programme = program,question = question,answers = answers_format,langage = typeMinted,category = category)


def generate_category(name,categories):
  """
    Pour AMC, genere une categorie regroupant un nombre choisi de question d'autres categories 
    Inputs:
       *name(str): Nom de la categorie cree
       *categories (str) : dictionnaire de cette forme: {nameCategory: numberQuestions} ab=vec nameCategory(str) le nom
       d'une categorie et numberQuestions(int) le nmbre de question de cette categorie a inclure
    Outputs:
        Template(code).render(...): str contenant le code latex correspondant a la categorie cree en AMC
    """
  code = r'''
  % for elt in categories.keys():
  \setgroupmode{${elt}}{cyclic}
  \shufflegroup{${elt}}
  % for _ in range(categories[elt]):
  \element{${name}}{
  \restituegroupe[1]{${elt}}
  }
  % endfor
  % endfor
    '''
  return Template(code).render(name = name,categories = categories )


