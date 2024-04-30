from ComplexCalcVisitor import ComplexCalcVisitor
from ComplexCalcParser import ComplexCalcParser
import math

class MyCalcVisitor(ComplexCalcVisitor):

    def __init__(self):
        self.memory = {}

    def visitAssign(self, ctx):
        id_ = ctx.ID().getText()
        value = int(self.visit(ctx.expr()))
        self.memory[id_] = value
        return float(value)

    def visitProg(self, ctx):
        return super().visitProg(ctx)

    def visitPrint(self, ctx):
        value = self.visit(ctx.expr())
        if isinstance(value, bool):
            print(value)
        else:
            print("{:.1f}".format(value))  # Imprime con 2 decimales si el valor no es booleano
        return value

    def visitBlank(self, ctx):
        return super().visitBlank(ctx)

    def visitId(self, ctx):
        id_ = ctx.ID().getText()
        if id_ in self.memory:
            return float(self.memory[id_])
        return 0.0

    def visitInt(self, ctx):
        return float(ctx.INT().getText())

    def visitFloat(self, ctx):
        return float(ctx.FLOAT().getText())

    def visitAddSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == ComplexCalcParser.ADD:
            return left + right
        return left - right

    def visitMulDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == ComplexCalcParser.MUL:
            return left * right
        return left / right

    def visitParens(self, ctx):
        return self.visit(ctx.expr())

    
    def VisitNeg(self, ctx):
        n = self.visit(ctx.expr())
        return -n
    
    def VisitPos(self, ctx):
        n = self.visit(ctx.expr())
        return n
        
    def visitComplex(self, ctx):
        # Obtener el texto de la expresión compleja
        complex_text = ctx.getText()
        
        # Verificar si hay una parte real explícita
        if '+' in complex_text:
            # Dividir la expresión en la parte real y la parte imaginaria
            real_part_text, imag_part_text = complex_text.split(' + ', 1)
        else:
            real_part_text = '0'
            imag_part_text = complex_text.rstrip('i')

        # Convertir las partes a números
        real_part = float(real_part_text)
        imag_part = float(imag_part_text) if imag_part_text else 0

        # Crear el número complejo
        complex_number = complex(real_part, imag_part)
        return complex_number
