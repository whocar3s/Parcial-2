# Generated from TFourier.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .TFourierParser import TFourierParser
else:
    from TFourierParser import TFourierParser

# This class defines a complete generic visitor for a parse tree produced by TFourierParser.

class TFourierVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TFourierParser#prog.
    def visitProg(self, ctx:TFourierParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TFourierParser#print.
    def visitPrint(self, ctx:TFourierParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TFourierParser#assign.
    def visitAssign(self, ctx:TFourierParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TFourierParser#blank.
    def visitBlank(self, ctx:TFourierParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TFourierParser#Tan.
    def visitTan(self, ctx:TFourierParser.TanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TFourierParser#lista.
    def visitLista(self, ctx:TFourierParser.ListaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TFourierParser#parens.
    def visitParens(self, ctx:TFourierParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TFourierParser#FourierTransform.
    def visitFourierTransform(self, ctx:TFourierParser.FourierTransformContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TFourierParser#MulDiv.
    def visitMulDiv(self, ctx:TFourierParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TFourierParser#AddSub.
    def visitAddSub(self, ctx:TFourierParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TFourierParser#Cos.
    def visitCos(self, ctx:TFourierParser.CosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TFourierParser#BoolNegacion.
    def visitBoolNegacion(self, ctx:TFourierParser.BoolNegacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TFourierParser#float.
    def visitFloat(self, ctx:TFourierParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TFourierParser#int.
    def visitInt(self, ctx:TFourierParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TFourierParser#Positivo.
    def visitPositivo(self, ctx:TFourierParser.PositivoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TFourierParser#pi.
    def visitPi(self, ctx:TFourierParser.PiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TFourierParser#Sin.
    def visitSin(self, ctx:TFourierParser.SinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TFourierParser#Decremento.
    def visitDecremento(self, ctx:TFourierParser.DecrementoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TFourierParser#id.
    def visitId(self, ctx:TFourierParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TFourierParser#Potencia.
    def visitPotencia(self, ctx:TFourierParser.PotenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TFourierParser#Exp.
    def visitExp(self, ctx:TFourierParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TFourierParser#Boolean.
    def visitBoolean(self, ctx:TFourierParser.BooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TFourierParser#Incremento.
    def visitIncremento(self, ctx:TFourierParser.IncrementoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TFourierParser#Negativo.
    def visitNegativo(self, ctx:TFourierParser.NegativoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TFourierParser#arglist.
    def visitArglist(self, ctx:TFourierParser.ArglistContext):
        return self.visitChildren(ctx)



del TFourierParser