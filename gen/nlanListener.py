from antlr4 import *

if __name__ is not None and "." in __name__:
    from .nlanParser import nlanParser
else:
    from nlanParser import nlanParser


# This class defines a complete listener for a parse tree produced by nlanParser.
class nlanListener(ParseTreeListener):

    # Enter a parse tree produced by nlanParser#program.
    def enterProgram(self, ctx: nlanParser.ProgramContext):
        pass

    # Exit a parse tree produced by nlanParser#program.
    def exitProgram(self, ctx: nlanParser.ProgramContext):
        pass

    # Enter a parse tree produced by nlanParser#math_sym.
    def enterMath_sym(self, ctx: nlanParser.Math_symContext):
        pass

    # Exit a parse tree produced by nlanParser#math_sym.
    def exitMath_sym(self, ctx: nlanParser.Math_symContext):
        pass

    # Enter a parse tree produced by nlanParser#compare_sym.
    def enterCompare_sym(self, ctx: nlanParser.Compare_symContext):
        pass

    # Exit a parse tree produced by nlanParser#compare_sym.
    def exitCompare_sym(self, ctx: nlanParser.Compare_symContext):
        pass

    # Enter a parse tree produced by nlanParser#var_decl.
    def enterVar_decl(self, ctx: nlanParser.Var_declContext):
        pass

    # Exit a parse tree produced by nlanParser#var_decl.
    def exitVar_decl(self, ctx: nlanParser.Var_declContext):
        pass

    # Enter a parse tree produced by nlanParser#arr_decl.
    def enterArr_decl(self, ctx: nlanParser.Arr_declContext):
        pass

    # Exit a parse tree produced by nlanParser#arr_decl.
    def exitArr_decl(self, ctx: nlanParser.Arr_declContext):
        pass

    # Enter a parse tree produced by nlanParser#math.
    def enterMath(self, ctx: nlanParser.MathContext):
        pass

    # Exit a parse tree produced by nlanParser#math.
    def exitMath(self, ctx: nlanParser.MathContext):
        pass

    # Enter a parse tree produced by nlanParser#loop_exp.
    def enterLoop_exp(self, ctx: nlanParser.Loop_expContext):
        pass

    # Exit a parse tree produced by nlanParser#loop_exp.
    def exitLoop_exp(self, ctx: nlanParser.Loop_expContext):
        pass

    # Enter a parse tree produced by nlanParser#print_var_exp.
    def enterPrint_var_exp(self, ctx: nlanParser.Print_var_expContext):
        pass

    # Exit a parse tree produced by nlanParser#print_var_exp.
    def exitPrint_var_exp(self, ctx: nlanParser.Print_var_expContext):
        pass

    # Enter a parse tree produced by nlanParser#print_text_exp.
    def enterPrint_text_exp(self, ctx: nlanParser.Print_text_expContext):
        pass

    # Exit a parse tree produced by nlanParser#print_text_exp.
    def exitPrint_text_exp(self, ctx: nlanParser.Print_text_expContext):
        pass


del nlanParser
