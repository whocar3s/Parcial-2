# Generated from TFourier.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .TFourierParser import TFourierParser
else:
    from TFourierParser import TFourierParser

# This class defines a complete listener for a parse tree produced by TFourierParser.
class TFourierListener(ParseTreeListener):

    # Enter a parse tree produced by TFourierParser#prog.
    def enterProg(self, ctx:TFourierParser.ProgContext):
        pass

    # Exit a parse tree produced by TFourierParser#prog.
    def exitProg(self, ctx:TFourierParser.ProgContext):
        pass


    # Enter a parse tree produced by TFourierParser#print.
    def enterPrint(self, ctx:TFourierParser.PrintContext):
        pass

    # Exit a parse tree produced by TFourierParser#print.
    def exitPrint(self, ctx:TFourierParser.PrintContext):
        pass


    # Enter a parse tree produced by TFourierParser#assign.
    def enterAssign(self, ctx:TFourierParser.AssignContext):
        pass

    # Exit a parse tree produced by TFourierParser#assign.
    def exitAssign(self, ctx:TFourierParser.AssignContext):
        pass


    # Enter a parse tree produced by TFourierParser#blank.
    def enterBlank(self, ctx:TFourierParser.BlankContext):
        pass

    # Exit a parse tree produced by TFourierParser#blank.
    def exitBlank(self, ctx:TFourierParser.BlankContext):
        pass


    # Enter a parse tree produced by TFourierParser#Tan.
    def enterTan(self, ctx:TFourierParser.TanContext):
        pass

    # Exit a parse tree produced by TFourierParser#Tan.
    def exitTan(self, ctx:TFourierParser.TanContext):
        pass


    # Enter a parse tree produced by TFourierParser#lista.
    def enterLista(self, ctx:TFourierParser.ListaContext):
        pass

    # Exit a parse tree produced by TFourierParser#lista.
    def exitLista(self, ctx:TFourierParser.ListaContext):
        pass


    # Enter a parse tree produced by TFourierParser#parens.
    def enterParens(self, ctx:TFourierParser.ParensContext):
        pass

    # Exit a parse tree produced by TFourierParser#parens.
    def exitParens(self, ctx:TFourierParser.ParensContext):
        pass


    # Enter a parse tree produced by TFourierParser#FourierTransform.
    def enterFourierTransform(self, ctx:TFourierParser.FourierTransformContext):
        pass

    # Exit a parse tree produced by TFourierParser#FourierTransform.
    def exitFourierTransform(self, ctx:TFourierParser.FourierTransformContext):
        pass


    # Enter a parse tree produced by TFourierParser#MulDiv.
    def enterMulDiv(self, ctx:TFourierParser.MulDivContext):
        pass

    # Exit a parse tree produced by TFourierParser#MulDiv.
    def exitMulDiv(self, ctx:TFourierParser.MulDivContext):
        pass


    # Enter a parse tree produced by TFourierParser#AddSub.
    def enterAddSub(self, ctx:TFourierParser.AddSubContext):
        pass

    # Exit a parse tree produced by TFourierParser#AddSub.
    def exitAddSub(self, ctx:TFourierParser.AddSubContext):
        pass


    # Enter a parse tree produced by TFourierParser#Cos.
    def enterCos(self, ctx:TFourierParser.CosContext):
        pass

    # Exit a parse tree produced by TFourierParser#Cos.
    def exitCos(self, ctx:TFourierParser.CosContext):
        pass


    # Enter a parse tree produced by TFourierParser#BoolNegacion.
    def enterBoolNegacion(self, ctx:TFourierParser.BoolNegacionContext):
        pass

    # Exit a parse tree produced by TFourierParser#BoolNegacion.
    def exitBoolNegacion(self, ctx:TFourierParser.BoolNegacionContext):
        pass


    # Enter a parse tree produced by TFourierParser#float.
    def enterFloat(self, ctx:TFourierParser.FloatContext):
        pass

    # Exit a parse tree produced by TFourierParser#float.
    def exitFloat(self, ctx:TFourierParser.FloatContext):
        pass


    # Enter a parse tree produced by TFourierParser#int.
    def enterInt(self, ctx:TFourierParser.IntContext):
        pass

    # Exit a parse tree produced by TFourierParser#int.
    def exitInt(self, ctx:TFourierParser.IntContext):
        pass


    # Enter a parse tree produced by TFourierParser#Positivo.
    def enterPositivo(self, ctx:TFourierParser.PositivoContext):
        pass

    # Exit a parse tree produced by TFourierParser#Positivo.
    def exitPositivo(self, ctx:TFourierParser.PositivoContext):
        pass


    # Enter a parse tree produced by TFourierParser#pi.
    def enterPi(self, ctx:TFourierParser.PiContext):
        pass

    # Exit a parse tree produced by TFourierParser#pi.
    def exitPi(self, ctx:TFourierParser.PiContext):
        pass


    # Enter a parse tree produced by TFourierParser#Sin.
    def enterSin(self, ctx:TFourierParser.SinContext):
        pass

    # Exit a parse tree produced by TFourierParser#Sin.
    def exitSin(self, ctx:TFourierParser.SinContext):
        pass


    # Enter a parse tree produced by TFourierParser#Decremento.
    def enterDecremento(self, ctx:TFourierParser.DecrementoContext):
        pass

    # Exit a parse tree produced by TFourierParser#Decremento.
    def exitDecremento(self, ctx:TFourierParser.DecrementoContext):
        pass


    # Enter a parse tree produced by TFourierParser#id.
    def enterId(self, ctx:TFourierParser.IdContext):
        pass

    # Exit a parse tree produced by TFourierParser#id.
    def exitId(self, ctx:TFourierParser.IdContext):
        pass


    # Enter a parse tree produced by TFourierParser#Boolean.
    def enterBoolean(self, ctx:TFourierParser.BooleanContext):
        pass

    # Exit a parse tree produced by TFourierParser#Boolean.
    def exitBoolean(self, ctx:TFourierParser.BooleanContext):
        pass


    # Enter a parse tree produced by TFourierParser#Incremento.
    def enterIncremento(self, ctx:TFourierParser.IncrementoContext):
        pass

    # Exit a parse tree produced by TFourierParser#Incremento.
    def exitIncremento(self, ctx:TFourierParser.IncrementoContext):
        pass


    # Enter a parse tree produced by TFourierParser#Negativo.
    def enterNegativo(self, ctx:TFourierParser.NegativoContext):
        pass

    # Exit a parse tree produced by TFourierParser#Negativo.
    def exitNegativo(self, ctx:TFourierParser.NegativoContext):
        pass


    # Enter a parse tree produced by TFourierParser#arglist.
    def enterArglist(self, ctx:TFourierParser.ArglistContext):
        pass

    # Exit a parse tree produced by TFourierParser#arglist.
    def exitArglist(self, ctx:TFourierParser.ArglistContext):
        pass



del TFourierParser