import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from ComplexCalcLexer import ComplexCalcLexer
from ComplexCalcParser import ComplexCalcParser
from MyCalcVisitor import MyCalcVisitor

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())

    lexer = ComplexCalcLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ComplexCalcParser(token_stream)
    tree = parser.prog()

    #lisp_tree_str = tree.toStringTree(recog=parser)
    #print(lisp_tree_str)

    visitor = MyCalcVisitor()
    visitor.visit(tree)
