# Generated from TFourier.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,24,88,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,10,8,0,11,0,12,
        0,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,23,8,1,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,3,2,63,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,
        2,75,8,2,10,2,12,2,78,9,2,1,3,1,3,1,3,5,3,83,8,3,10,3,12,3,86,9,
        3,1,3,0,1,4,4,0,2,4,6,0,2,2,0,10,10,12,12,2,0,11,11,13,13,104,0,
        9,1,0,0,0,2,22,1,0,0,0,4,62,1,0,0,0,6,79,1,0,0,0,8,10,3,2,1,0,9,
        8,1,0,0,0,10,11,1,0,0,0,11,9,1,0,0,0,11,12,1,0,0,0,12,1,1,0,0,0,
        13,14,3,4,2,0,14,15,5,23,0,0,15,23,1,0,0,0,16,17,5,20,0,0,17,18,
        5,1,0,0,18,19,3,4,2,0,19,20,5,23,0,0,20,23,1,0,0,0,21,23,5,23,0,
        0,22,13,1,0,0,0,22,16,1,0,0,0,22,21,1,0,0,0,23,3,1,0,0,0,24,25,6,
        2,-1,0,25,26,5,2,0,0,26,27,3,4,2,0,27,28,5,3,0,0,28,63,1,0,0,0,29,
        63,5,21,0,0,30,63,5,22,0,0,31,63,5,4,0,0,32,33,5,15,0,0,33,34,5,
        2,0,0,34,35,3,4,2,0,35,36,5,3,0,0,36,63,1,0,0,0,37,38,5,16,0,0,38,
        39,5,2,0,0,39,40,3,4,2,0,40,41,5,3,0,0,41,63,1,0,0,0,42,43,5,17,
        0,0,43,44,5,2,0,0,44,45,3,4,2,0,45,46,5,3,0,0,46,63,1,0,0,0,47,48,
        5,18,0,0,48,49,5,2,0,0,49,50,3,6,3,0,50,51,5,3,0,0,51,63,1,0,0,0,
        52,63,5,14,0,0,53,54,5,19,0,0,54,63,3,4,2,7,55,63,5,20,0,0,56,57,
        5,7,0,0,57,63,3,4,2,3,58,59,5,8,0,0,59,63,3,4,2,2,60,61,5,9,0,0,
        61,63,3,4,2,1,62,24,1,0,0,0,62,29,1,0,0,0,62,30,1,0,0,0,62,31,1,
        0,0,0,62,32,1,0,0,0,62,37,1,0,0,0,62,42,1,0,0,0,62,47,1,0,0,0,62,
        52,1,0,0,0,62,53,1,0,0,0,62,55,1,0,0,0,62,56,1,0,0,0,62,58,1,0,0,
        0,62,60,1,0,0,0,63,76,1,0,0,0,64,65,10,17,0,0,65,66,7,0,0,0,66,75,
        3,4,2,18,67,68,10,16,0,0,68,69,7,1,0,0,69,75,3,4,2,17,70,71,10,5,
        0,0,71,75,5,5,0,0,72,73,10,4,0,0,73,75,5,6,0,0,74,64,1,0,0,0,74,
        67,1,0,0,0,74,70,1,0,0,0,74,72,1,0,0,0,75,78,1,0,0,0,76,74,1,0,0,
        0,76,77,1,0,0,0,77,5,1,0,0,0,78,76,1,0,0,0,79,84,3,4,2,0,80,81,5,
        9,0,0,81,83,3,4,2,0,82,80,1,0,0,0,83,86,1,0,0,0,84,82,1,0,0,0,84,
        85,1,0,0,0,85,7,1,0,0,0,86,84,1,0,0,0,6,11,22,62,74,76,84
    ]

class TFourierParser ( Parser ):

    grammarFileName = "TFourier.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'('", "')'", "'pi'", "'++'", "'--'", 
                     "'-'", "'+'", "','", "' * '", "' + '", "' / '", "' - '", 
                     "<INVALID>", "'Sin'", "'Cos'", "'Tan'", "'F'", "'!'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "MUL", "ADD", "DIV", "SUB", 
                      "BOOLEAN", "SIN", "COS", "TAN", "F", "BOOL_NEG", "ID", 
                      "INT", "FLOAT", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2
    RULE_arglist = 3

    ruleNames =  [ "prog", "stat", "expr", "arglist" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    MUL=10
    ADD=11
    DIV=12
    SUB=13
    BOOLEAN=14
    SIN=15
    COS=16
    TAN=17
    F=18
    BOOL_NEG=19
    ID=20
    INT=21
    FLOAT=22
    NEWLINE=23
    WS=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TFourierParser.StatContext)
            else:
                return self.getTypedRuleContext(TFourierParser.StatContext,i)


        def getRuleIndex(self):
            return TFourierParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = TFourierParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.stat()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 16761748) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TFourierParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrintContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TFourierParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(TFourierParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(TFourierParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)


    class BlankContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TFourierParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(TFourierParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlank" ):
                listener.enterBlank(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlank" ):
                listener.exitBlank(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlank" ):
                return visitor.visitBlank(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TFourierParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(TFourierParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(TFourierParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(TFourierParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = TFourierParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 22
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = TFourierParser.PrintContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.expr(0)
                self.state = 14
                self.match(TFourierParser.NEWLINE)
                pass

            elif la_ == 2:
                localctx = TFourierParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.match(TFourierParser.ID)
                self.state = 17
                self.match(TFourierParser.T__0)
                self.state = 18
                self.expr(0)
                self.state = 19
                self.match(TFourierParser.NEWLINE)
                pass

            elif la_ == 3:
                localctx = TFourierParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 21
                self.match(TFourierParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TFourierParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class TanContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TFourierParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TAN(self):
            return self.getToken(TFourierParser.TAN, 0)
        def expr(self):
            return self.getTypedRuleContext(TFourierParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTan" ):
                listener.enterTan(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTan" ):
                listener.exitTan(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTan" ):
                return visitor.visitTan(self)
            else:
                return visitor.visitChildren(self)


    class ListaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TFourierParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(TFourierParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista" ):
                listener.enterLista(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista" ):
                listener.exitLista(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLista" ):
                return visitor.visitLista(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TFourierParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(TFourierParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class FourierTransformContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TFourierParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def F(self):
            return self.getToken(TFourierParser.F, 0)
        def arglist(self):
            return self.getTypedRuleContext(TFourierParser.ArglistContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFourierTransform" ):
                listener.enterFourierTransform(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFourierTransform" ):
                listener.exitFourierTransform(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFourierTransform" ):
                return visitor.visitFourierTransform(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TFourierParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TFourierParser.ExprContext)
            else:
                return self.getTypedRuleContext(TFourierParser.ExprContext,i)

        def MUL(self):
            return self.getToken(TFourierParser.MUL, 0)
        def DIV(self):
            return self.getToken(TFourierParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TFourierParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TFourierParser.ExprContext)
            else:
                return self.getTypedRuleContext(TFourierParser.ExprContext,i)

        def ADD(self):
            return self.getToken(TFourierParser.ADD, 0)
        def SUB(self):
            return self.getToken(TFourierParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class CosContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TFourierParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def COS(self):
            return self.getToken(TFourierParser.COS, 0)
        def expr(self):
            return self.getTypedRuleContext(TFourierParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCos" ):
                listener.enterCos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCos" ):
                listener.exitCos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCos" ):
                return visitor.visitCos(self)
            else:
                return visitor.visitChildren(self)


    class BoolNegacionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TFourierParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL_NEG(self):
            return self.getToken(TFourierParser.BOOL_NEG, 0)
        def expr(self):
            return self.getTypedRuleContext(TFourierParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolNegacion" ):
                listener.enterBoolNegacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolNegacion" ):
                listener.exitBoolNegacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolNegacion" ):
                return visitor.visitBoolNegacion(self)
            else:
                return visitor.visitChildren(self)


    class FloatContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TFourierParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(TFourierParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat" ):
                return visitor.visitFloat(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TFourierParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(TFourierParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)


    class PositivoContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TFourierParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(TFourierParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPositivo" ):
                listener.enterPositivo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPositivo" ):
                listener.exitPositivo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPositivo" ):
                return visitor.visitPositivo(self)
            else:
                return visitor.visitChildren(self)


    class PiContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TFourierParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPi" ):
                listener.enterPi(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPi" ):
                listener.exitPi(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPi" ):
                return visitor.visitPi(self)
            else:
                return visitor.visitChildren(self)


    class SinContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TFourierParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SIN(self):
            return self.getToken(TFourierParser.SIN, 0)
        def expr(self):
            return self.getTypedRuleContext(TFourierParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSin" ):
                listener.enterSin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSin" ):
                listener.exitSin(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSin" ):
                return visitor.visitSin(self)
            else:
                return visitor.visitChildren(self)


    class DecrementoContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TFourierParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(TFourierParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecremento" ):
                listener.enterDecremento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecremento" ):
                listener.exitDecremento(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecremento" ):
                return visitor.visitDecremento(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TFourierParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(TFourierParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class BooleanContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TFourierParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOLEAN(self):
            return self.getToken(TFourierParser.BOOLEAN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean" ):
                listener.enterBoolean(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean" ):
                listener.exitBoolean(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean" ):
                return visitor.visitBoolean(self)
            else:
                return visitor.visitChildren(self)


    class IncrementoContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TFourierParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(TFourierParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncremento" ):
                listener.enterIncremento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncremento" ):
                listener.exitIncremento(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIncremento" ):
                return visitor.visitIncremento(self)
            else:
                return visitor.visitChildren(self)


    class NegativoContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TFourierParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(TFourierParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegativo" ):
                listener.enterNegativo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegativo" ):
                listener.exitNegativo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegativo" ):
                return visitor.visitNegativo(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TFourierParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = TFourierParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 25
                self.match(TFourierParser.T__1)
                self.state = 26
                self.expr(0)
                self.state = 27
                self.match(TFourierParser.T__2)
                pass
            elif token in [21]:
                localctx = TFourierParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 29
                self.match(TFourierParser.INT)
                pass
            elif token in [22]:
                localctx = TFourierParser.FloatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 30
                self.match(TFourierParser.FLOAT)
                pass
            elif token in [4]:
                localctx = TFourierParser.PiContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 31
                self.match(TFourierParser.T__3)
                pass
            elif token in [15]:
                localctx = TFourierParser.SinContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 32
                self.match(TFourierParser.SIN)
                self.state = 33
                self.match(TFourierParser.T__1)
                self.state = 34
                self.expr(0)
                self.state = 35
                self.match(TFourierParser.T__2)
                pass
            elif token in [16]:
                localctx = TFourierParser.CosContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 37
                self.match(TFourierParser.COS)
                self.state = 38
                self.match(TFourierParser.T__1)
                self.state = 39
                self.expr(0)
                self.state = 40
                self.match(TFourierParser.T__2)
                pass
            elif token in [17]:
                localctx = TFourierParser.TanContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 42
                self.match(TFourierParser.TAN)
                self.state = 43
                self.match(TFourierParser.T__1)
                self.state = 44
                self.expr(0)
                self.state = 45
                self.match(TFourierParser.T__2)
                pass
            elif token in [18]:
                localctx = TFourierParser.FourierTransformContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 47
                self.match(TFourierParser.F)
                self.state = 48
                self.match(TFourierParser.T__1)
                self.state = 49
                self.arglist()
                self.state = 50
                self.match(TFourierParser.T__2)
                pass
            elif token in [14]:
                localctx = TFourierParser.BooleanContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 52
                self.match(TFourierParser.BOOLEAN)
                pass
            elif token in [19]:
                localctx = TFourierParser.BoolNegacionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 53
                self.match(TFourierParser.BOOL_NEG)
                self.state = 54
                self.expr(7)
                pass
            elif token in [20]:
                localctx = TFourierParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 55
                self.match(TFourierParser.ID)
                pass
            elif token in [7]:
                localctx = TFourierParser.NegativoContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 56
                self.match(TFourierParser.T__6)
                self.state = 57
                self.expr(3)
                pass
            elif token in [8]:
                localctx = TFourierParser.PositivoContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 58
                self.match(TFourierParser.T__7)
                self.state = 59
                self.expr(2)
                pass
            elif token in [9]:
                localctx = TFourierParser.ListaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 60
                self.match(TFourierParser.T__8)
                self.state = 61
                self.expr(1)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 76
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 74
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = TFourierParser.MulDivContext(self, TFourierParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 64
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 65
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==10 or _la==12):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 66
                        self.expr(18)
                        pass

                    elif la_ == 2:
                        localctx = TFourierParser.AddSubContext(self, TFourierParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 67
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 68
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==11 or _la==13):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 69
                        self.expr(17)
                        pass

                    elif la_ == 3:
                        localctx = TFourierParser.IncrementoContext(self, TFourierParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 70
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 71
                        self.match(TFourierParser.T__4)
                        pass

                    elif la_ == 4:
                        localctx = TFourierParser.DecrementoContext(self, TFourierParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 72
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 73
                        self.match(TFourierParser.T__5)
                        pass

             
                self.state = 78
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ArglistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TFourierParser.ExprContext)
            else:
                return self.getTypedRuleContext(TFourierParser.ExprContext,i)


        def getRuleIndex(self):
            return TFourierParser.RULE_arglist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArglist" ):
                listener.enterArglist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArglist" ):
                listener.exitArglist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArglist" ):
                return visitor.visitArglist(self)
            else:
                return visitor.visitChildren(self)




    def arglist(self):

        localctx = TFourierParser.ArglistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_arglist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.expr(0)
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 80
                self.match(TFourierParser.T__8)
                self.state = 81
                self.expr(0)
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         




