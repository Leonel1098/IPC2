
import webbrowser
import os

strGraphviz = "digraph G { \n"
strGraphviz+='a[label="Hola"]\n'
strGraphviz+='b[label="mundo"]\n'
strGraphviz+='a->b \n}'
documentodot="matriz_graphvizforma1.txt"
with open(documentodot,'w') as grafica:
    grafica.write(strGraphviz)
pdf="matriz_graphvizforma1.pdf"
os.system("neato -Tpdf "+documentodot+" -o " + pdf)
webbrowser.open(pdf)




########################################Forma 2 

import webbrowser
import graphviz

dot = graphviz.Digraph('round-table')
dot.node('A', 'King Arthur')  

dot.node('B', 'Sir Bedevere the Wise')

dot.node('L', 'Sir Lancelot the Brave')

dot.edges(['AB', 'AL'])
dot.render().replace('\\', '/')
'round-table.gv.pdf'
webbrowser.open('round-table.gv.pdf')
