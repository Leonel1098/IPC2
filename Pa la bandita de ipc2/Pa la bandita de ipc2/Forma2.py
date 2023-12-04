import webbrowser
import graphviz

dot = graphviz.Digraph('ejemploForma2')

dot.node('a','Hola mundo 2')
dot.node('b','Hola mundo 3')

dot.edges(['ab','ba'])

dot.render().replace('\\', '/')
'ejemploForma2.gv.pdf'
print(dot.source)
##webbrowser.open('ejemploForma2.gv.pdf')