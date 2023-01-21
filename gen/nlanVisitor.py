from antlr4 import *
import numpy as np

if __name__ is not None and "." in __name__:
    from .nlanParser import nlanParser
else:
    from nlanParser import nlanParser


# This class defines a complete generic visitor for a parse tree produced by nlanParser.

class nlanVisitor(ParseTreeVisitor):

    def __init__(self):
        self.decs = 0

    # Visit a parse tree produced by nlanParser#program.
    def visitProgram(self, ctx: nlanParser.ProgramContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by nlanParser#math_sym.
    def visitMath_sym(self, ctx: nlanParser.Math_symContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by nlanParser#compare_sym.
    def visitCompare_sym(self, ctx: nlanParser.Compare_symContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by nlanParser#var_decl.
    def visitVar_decl(self, ctx: nlanParser.Var_declContext):
        text = ctx.getText()
        temp = text.split('oWartosci')

        val = temp[1][:-1]

        if self.decs > 0:
            print("   ", end='')
            self.decs -= 1

        print(temp[0][13:] + ' = ' + val)

        return self.visitChildren(ctx)

    # Visit a parse tree produced by nlanParser#arr_decl.
    def visitArr_decl(self, ctx: nlanParser.Arr_declContext):
        text = ctx.getText()
        temp = text.split('oWartosci')
        array_val = temp[1][1:-2].split("&")

        if self.decs > 0:
            print("   ", end='')
            self.decs -= 1

        print(temp[0][13:] + ' = ' + '[', end='')
        for i in array_val[0:-1]:
            print(i + ', ', end='')

        print(array_val[-1] + ']')

        return self.visitChildren(ctx)

    # Visit a parse tree produced by nlanParser#math.
    def visitMath(self, ctx: nlanParser.MathContext):
        text = ctx.getText()[:-1]
        text = text.split("rownaSie")
        value = text[0]
        eq = text[1]
        eq = eq.replace("razy", " * ")
        eq = eq.replace("dodac", " + ")
        eq = eq.replace("odjac", " - ")
        eq = eq.replace("podzielicPrzez", " / ")
        eq = eq.replace("doPotegi", " ** ")

        if self.decs > 0:
            print("   ", end='')
            self.decs -= 1
        print(value + ' = ' + eq)

        return self.visitChildren(ctx)

    # Visit a parse tree produced by nlanParser#loop_exp.
    def visitLoop_exp(self, ctx: nlanParser.Loop_expContext):
        text = ctx.getText()
        self.decs = text.count(",") - 1
        loop_decl = text.split(':')[0]
        if 'dlaKazdejWartosci' in loop_decl:
            self.decs -= 1
            loop_decl = loop_decl.replace('dlaKazdejWartosci', '')
            loop_decl = loop_decl.split('ZZakresu')

            print("for " + loop_decl[0] + " in range" + loop_decl[1] + ':')
        elif 'dlaKazdegoElementu' in loop_decl:
            loop_decl = loop_decl.replace('dlaKazdegoElementu', '')
            loop_decl = loop_decl.split('nalezacegoDo')
            print('for ' + loop_decl[0] + ' in ' + loop_decl[1] + ':')
        else:
            loop_decl = loop_decl.replace('jezeli', 'if ')
            loop_decl = loop_decl.replace('dopoki', 'while ')
            loop_decl = loop_decl.replace('jestRowne', ' == ')
            loop_decl = loop_decl.replace('jestMniejszeLubRowne', ' <= ')
            loop_decl = loop_decl.replace('jestWiekszeLubRowne', ' >= ')
            loop_decl = loop_decl.replace('jestWieksze', ' > ')
            loop_decl = loop_decl.replace('jestMniejsze', ' < ')
            loop_decl += ':'
            print(loop_decl)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by nlanParser#print_var_exp.
    def visitPrint_var_exp(self, ctx: nlanParser.Print_var_expContext):
        text = ctx.getText()[14:-2]
        if self.decs > 0:
            print("   ", end='')
            self.decs -= 1
        print("print(" + text + ")")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by nlanParser#print_text_exp.
    def visitPrint_text_exp(self, ctx: nlanParser.Print_text_expContext):
        text = ctx.getText()[13:-3]
        if self.decs > 0:
            print("   ", end='')
            self.decs -= 1
        print("print('" + text + "')")
        return self.visitChildren(ctx)


del nlanParser
