# Generated from ComplexCalc.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ComplexCalcParser import ComplexCalcParser
else:
    from ComplexCalcParser import ComplexCalcParser

# This class defines a complete generic visitor for a parse tree produced by ComplexCalcParser.

class ComplexCalcVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ComplexCalcParser#prog.
    def visitProg(self, ctx:ComplexCalcParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexCalcParser#print.
    def visitPrint(self, ctx:ComplexCalcParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexCalcParser#assign.
    def visitAssign(self, ctx:ComplexCalcParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexCalcParser#blank.
    def visitBlank(self, ctx:ComplexCalcParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexCalcParser#parens.
    def visitParens(self, ctx:ComplexCalcParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexCalcParser#MulDiv.
    def visitMulDiv(self, ctx:ComplexCalcParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexCalcParser#AddSub.
    def visitAddSub(self, ctx:ComplexCalcParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexCalcParser#complex.
    def visitComplex(self, ctx:ComplexCalcParser.ComplexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexCalcParser#id.
    def visitId(self, ctx:ComplexCalcParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexCalcParser#float.
    def visitFloat(self, ctx:ComplexCalcParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexCalcParser#int.
    def visitInt(self, ctx:ComplexCalcParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexCalcParser#Negativo.
    def visitNegativo(self, ctx:ComplexCalcParser.NegativoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexCalcParser#Positivo.
    def visitPositivo(self, ctx:ComplexCalcParser.PositivoContext):
        return self.visitChildren(ctx)



del ComplexCalcParser