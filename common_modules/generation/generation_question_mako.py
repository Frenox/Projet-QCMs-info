from mako.template import Template
from random import * 
def generate_question(program,question,answers,typeOutput,typeMinted,category,typeQuestion = None):
  if typeOutput == "amc":
    enonce = r'''
    \element{${category}}{
      \begin{question}{question}
        ${question} 
        \inputminted[firstline=1, lastline=5]{${langage}}{${programme}}
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
      {${question}}
      \inputminted[firstline=1, lastline=5]{${langage}}{${programme}}
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
  return Template(enonce).render(programme = program,question = question,answers = answers_format,langage = typeMinted,category = category)


def generate_category(name,categories):
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



print(generate_question("test1.py","Que ?",["47"],"moodle","python","newCat","short"))
print(generate_category("Category3",{"Category2":2,"Category1":1}))


