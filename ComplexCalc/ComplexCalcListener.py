# Generated from ComplexCalc.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ComplexCalcParser import ComplexCalcParser
else:
    from ComplexCalcParser import ComplexCalcParser

# This class defines a complete listener for a parse tree produced by ComplexCalcParser.
class ComplexCalcListener(ParseTreeListener):

    # Enter a parse tree produced by ComplexCalcParser#prog.
    def enterProg(self, ctx:ComplexCalcParser.ProgContext):
        pass

    # Exit a parse tree produced by ComplexCalcParser#prog.
    def exitProg(self, ctx:ComplexCalcParser.ProgContext):
        pass


    # Enter a parse tree produced by ComplexCalcParser#print.
    def enterPrint(self, ctx:ComplexCalcParser.PrintContext):
        pass

    # Exit a parse tree produced by ComplexCalcParser#print.
    def exitPrint(self, ctx:ComplexCalcParser.PrintContext):
        pass


    # Enter a parse tree produced by ComplexCalcParser#assign.
    def enterAssign(self, ctx:ComplexCalcParser.AssignContext):
        pass

    # Exit a parse tree produced by ComplexCalcParser#assign.
    def exitAssign(self, ctx:ComplexCalcParser.AssignContext):
        pass


    # Enter a parse tree produced by ComplexCalcParser#blank.
    def enterBlank(self, ctx:ComplexCalcParser.BlankContext):
        pass

    # Exit a parse tree produced by ComplexCalcParser#blank.
    def exitBlank(self, ctx:ComplexCalcParser.BlankContext):
        pass


    # Enter a parse tree produced by ComplexCalcParser#parens.
    def enterParens(self, ctx:ComplexCalcParser.ParensContext):
        pass

    # Exit a parse tree produced by ComplexCalcParser#parens.
    def exitParens(self, ctx:ComplexCalcParser.ParensContext):
        pass


    # Enter a parse tree produced by ComplexCalcParser#MulDiv.
    def enterMulDiv(self, ctx:ComplexCalcParser.MulDivContext):
        pass

    # Exit a parse tree produced by ComplexCalcParser#MulDiv.
    def exitMulDiv(self, ctx:ComplexCalcParser.MulDivContext):
        pass


    # Enter a parse tree produced by ComplexCalcParser#AddSub.
    def enterAddSub(self, ctx:ComplexCalcParser.AddSubContext):
        pass

    # Exit a parse tree produced by ComplexCalcParser#AddSub.
    def exitAddSub(self, ctx:ComplexCalcParser.AddSubContext):
        pass


    # Enter a parse tree produced by ComplexCalcParser#complex.
    def enterComplex(self, ctx:ComplexCalcParser.ComplexContext):
        pass

    # Exit a parse tree produced by ComplexCalcParser#complex.
    def exitComplex(self, ctx:ComplexCalcParser.ComplexContext):
        pass


    # Enter a parse tree produced by ComplexCalcParser#id.
    def enterId(self, ctx:ComplexCalcParser.IdContext):
        pass

    # Exit a parse tree produced by ComplexCalcParser#id.
    def exitId(self, ctx:ComplexCalcParser.IdContext):
        pass


    # Enter a parse tree produced by ComplexCalcParser#float.
    def enterFloat(self, ctx:ComplexCalcParser.FloatContext):
        pass

    # Exit a parse tree produced by ComplexCalcParser#float.
    def exitFloat(self, ctx:ComplexCalcParser.FloatContext):
        pass


    # Enter a parse tree produced by ComplexCalcParser#int.
    def enterInt(self, ctx:ComplexCalcParser.IntContext):
        pass

    # Exit a parse tree produced by ComplexCalcParser#int.
    def exitInt(self, ctx:ComplexCalcParser.IntContext):
        pass


    # Enter a parse tree produced by ComplexCalcParser#Negativo.
    def enterNegativo(self, ctx:ComplexCalcParser.NegativoContext):
        pass

    # Exit a parse tree produced by ComplexCalcParser#Negativo.
    def exitNegativo(self, ctx:ComplexCalcParser.NegativoContext):
        pass


    # Enter a parse tree produced by ComplexCalcParser#Positivo.
    def enterPositivo(self, ctx:ComplexCalcParser.PositivoContext):
        pass

    # Exit a parse tree produced by ComplexCalcParser#Positivo.
    def exitPositivo(self, ctx:ComplexCalcParser.PositivoContext):
        pass



del ComplexCalcParser