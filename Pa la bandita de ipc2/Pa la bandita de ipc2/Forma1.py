import webbrowser
import os 

escrituradot=""
escrituradot+=" digraph G { \n"
escrituradot+=' a[label="Hola"];\n'
escrituradot+=' b[label="mundo"];\n'
escrituradot+=' a -> b; \n'
escrituradot+=' b -> a; \n}'

dot = "ejemploForma1.txt"

with open(dot,'w') as variable: 
    variable.write(escrituradot)

pdf="ejemploForma1.pdf"
os.system("neato -Tpdf "+dot+" -o "+pdf)
webbrowser.open(pdf)

