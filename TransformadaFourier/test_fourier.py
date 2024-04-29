#**Ejemplo de programa de prueba:**
import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from FourierTransformVisitor import FourierTransformVisitor
from TFourierLexer import TFourierLexer
from TFourierParser import TFourierParser

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())

    lexer = TFourierLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = TFourierParser(token_stream)
    tree = parser.prog()


    visitor = FourierTransformVisitor()
    result = visitor.visit(tree)

