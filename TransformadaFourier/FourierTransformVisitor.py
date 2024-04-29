from matplotlib import pyplot as plt
from TFourierVisitor import TFourierVisitor
from TFourierParser import TFourierParser
import math
import numpy as np
import sympy as sp

class FourierTransformVisitor(TFourierVisitor):
    def __init__(self):
        self.memory = {}  # Diccionario para almacenar variables asignadas

    def visitAssign(self, ctx):
        id_ = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[id_] = value
        return value

    def visitPrint(self, ctx):
        value = self.visit(ctx.expr())
        print("[{}]".format(", ".join("{:.2f}".format(x) for x in value)))
        return value

    def visitInt(self, ctx):
        return float(ctx.INT().getText())

    def visitAddSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == TFourierParser.ADD:
            return left + right
        return left - right

    def visitMulDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == TFourierParser.MUL:
            return left * right
        return left / right

    def visitParens(self, ctx):
        return self.visit(ctx.expr())

    def visitId(self, ctx):
        id_ = ctx.ID().getText()
        if id_ in self.memory:
            return self.memory[id_]
        return 0.0
    
    def visitSin(self, ctx):
        n = self.visit(ctx.expr())
        return math.sin(n)

    def visitCos(self, ctx):
        n = self.visit(ctx.expr())
        return math.cos(n)

    def visitTan(self, ctx):
        n = self.visit(ctx.expr())
        return math.tan(n)
    
    def VisitNeg(self, ctx):
        n = self.visit(ctx.expr())
        return -n
    
    def VisitPos(self, ctx):
        n = self.visit(ctx.expr())
        return n
    
    def visitIncremento(self, ctx):
        n = self.visit(ctx.expr())
        return n + 1

    def visitDecremento(self, ctx):
        n = self.visit(ctx.expr())
        return n - 1
        
    def visitBoolean(self, ctx):
        value = ctx.BOOLEAN().getText()
        return value.lower() == "true"
    
    def visitBoolNegacion(self, ctx):
        value = self.visit(ctx.expr())
        return not bool(value)

    def visitFourierTransform(self, ctx):
        print("Visitando la función F")
        arglist_ctx = ctx.arglist()
        arguments = [expr_ctx.getText() for expr_ctx in arglist_ctx.expr()]
        print("Argumentos de la función F:", arguments)

        def signal(t):
            t_sym = sp.symbols('t') 
            evaluated_args = []
            for t_val in t:
                for expr in arguments:
                    if 'Sin(' in expr:  
                        sin_expr = expr[expr.find('(')+1:expr.find(')')]  
                        expr = expr.replace('Sin(' + sin_expr + ')', str(sp.sin(t_sym)))  
                    elif 'Cos(' in expr:  
                        cos_expr = expr[expr.find('(')+1:expr.find(')')]  
                        expr = expr.replace('Cos(' + cos_expr + ')', str(sp.cos(t_sym))) 
                    elif 'Tan(' in expr:  
                        tan_expr = expr[expr.find('(')+1:expr.find(')')]  
                        expr = expr.replace('Tan(' + tan_expr + ')', str(sp.tan(t_sym)))  
                    evaluated_args.append(sp.sympify(expr).subs({'t': t_val}).evalf())
            return evaluated_args

        t = np.linspace(0, 100, 1000)
        dt = t[1] - t[0]  

        x = signal(t)

        transformada = np.fft.fft(x)
        frecuencias = np.fft.fftfreq(len(x), dt)

        plt.figure(figsize=(12, 6))

        plt.subplot(2, 1, 1)
        plt.plot(t, x)
        plt.title('Señal:' + ', '.join(arguments))
        plt.xlabel('Tiempo')
        plt.ylabel('Amplitud')

        plt.subplot(2, 1, 2)
        plt.plot(frecuencias, np.abs(transformada))
        plt.title('Transformada de Fourier')
        plt.xlabel('Frecuencia')
        plt.ylabel('Magnitud')

        plt.tight_layout()
        plt.show()

        return transformada


        