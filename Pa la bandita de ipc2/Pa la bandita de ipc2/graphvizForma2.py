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