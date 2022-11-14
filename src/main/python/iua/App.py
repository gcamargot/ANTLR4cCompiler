import sys
from antlr4 import *
from compiladoresLexer  import compiladoresLexer
from compiladoresParser import compiladoresParser
from MiListener import MiListener

def main(argv):
    # archivo = "/home/gaston/Desktop/2022/2do cuatrimestre/DHS/DHS2022/input/entrada.txt"
    # archivo = "/home/gaston/Desktop/2022/2do cuatrimestre/DHS/DHS2022/input/parentesis.txt"
    archivo = "/home/gaston/Desktop/2022/2do cuatrimestre/DHS/DHS2022/input/programa.c"
    if len(argv) > 1 :
        archivo = argv[1]
    input = FileStream(archivo)
    lexer = compiladoresLexer(input)
    stream = CommonTokenStream(lexer)
    parser = compiladoresParser(stream)
    miListener = MiListener()
    parser.addParseListener(miListener)
    tree = parser.program()
    #print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)