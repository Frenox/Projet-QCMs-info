# Production d'un exercice...
# Les données :
# - sequence : la séquence utilisée (assez longue avec ... au milieu)
# - les indices des éléments cherchés
# - organisation des questions : le second, le dernier, un du début (parmi
# plusieurs), un des deniers (parmi plusieurs)

enonce = r'''
<%
    classesIndices = {
	'Second': (1,),
	'Dernier': (-1,),
	'VersDebut': (2, 3),
	'VersFin': (-2, -3, -4),
    }
%>
% for numSeq, seqText in enumerate(sequences, 1):
<%
    seq = eval(seqText)
    nomPrincipal = "SequenceIndex"
    nomSerie = nomPrincipal + str(numSeq)
    assert len(set(seq)) == len(seq), "Erreur : les éléments doivent être uniques" + seqText
%>
    % for nom, indices in classesIndices.items():
    <%
	questionNom = nomSerie + nom
    %>
	% for indice in indices:
	\element{${questionNom}}{%
	    \begin{questionmultx}{${questionNom}}
	    Quel est l'indice de ${seq[indice]} dans \mintinline{python}|s| ?
	    \AMCnumericChoices{${indice}}{digits=1,decimals=0,sign=true,scoreexact=1,vertical=false,
			    borderwidth=0mm,bordercol=gray,hspace=1.2ex,vspace=0em,reverse=false}
	    \end{questionmultx}
	}

	% endfor

    \element{${nomSerie}Questions}{%
	\insertgroup[1]{${questionNom}}
    }
    % endfor

\element{${nomSerie}}{%
    \smallskip
    Soit %l'instruction
    \mintinline{python}|s = ${seqText}| où
    \og{} \mintinline{python}|...| \fg{} remplace plusieurs éléments.

    \medskip

    \insertgroup{${nomSerie}Questions}
}

\element{${nomPrincipal}}{
    \insertgroup{${nomSerie}}
}
% endfor
'''

from mako.template import Template
print(Template(enonce).render(sequences=(
    "[7, 13, -4, 18, 5, ..., 6, -1, 91, 77, 10]",
    "[13, -4, 18, 7, 15, ..., 11, 91, 6, 10, 77]",
    "[15, 4, 52,  2, 5, ..., 28, 3, 6, 9, 7]")))