# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
from typing import TextIO


def serializedATN():
    return [
        4, 1, 36, 162, 2, 0, 7, 0, 2, 1, 7, 1, 2, 2, 7, 2, 2, 3, 7, 3, 2, 4, 7, 4, 2, 5, 7, 5, 2, 6, 7,
        6, 2, 7, 7, 7, 2, 8, 7, 8, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 5, 0, 27, 8, 0, 10,
        0, 12, 0, 30, 9, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 2, 1, 2, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1,
        4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 5, 4, 51, 8, 4, 10, 4, 12, 4, 54, 9, 4, 1, 4, 1, 4, 1,
        4, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 5, 5, 67, 8, 5, 10, 5, 12, 5, 70, 9, 5, 1,
        5, 1, 5, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 5, 6, 84, 8, 6, 10, 6, 12,
        6, 87, 9, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 5, 6,
        102, 8, 6, 10, 6, 12, 6, 105, 9, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1,
        6, 1, 6, 1, 6, 1, 6, 5, 6, 120, 8, 6, 10, 6, 12, 6, 123, 9, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6,
        1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 5, 6, 141, 8, 6, 10, 6, 12,
        6, 144, 9, 6, 1, 6, 1, 6, 3, 6, 148, 8, 6, 1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 1, 8, 1, 8, 1,
        8, 1, 8, 1, 8, 1, 8, 1, 8, 0, 0, 9, 0, 2, 4, 6, 8, 10, 12, 14, 16, 0, 5, 1, 0, 6, 10, 1, 0, 13,
        17, 1, 0, 35, 36, 1, 0, 34, 36, 2, 0, 34, 34, 36, 36, 183, 0, 18, 1, 0, 0, 0, 2, 33, 1, 0,
        0, 0, 4, 35, 1, 0, 0, 0, 6, 37, 1, 0, 0, 0, 8, 43, 1, 0, 0, 0, 10, 58, 1, 0, 0, 0, 12, 147,
        1, 0, 0, 0, 14, 149, 1, 0, 0, 0, 16, 155, 1, 0, 0, 0, 18, 19, 5, 1, 0, 0, 19, 28, 5, 11, 0,
        0, 20, 27, 3, 6, 3, 0, 21, 27, 3, 8, 4, 0, 22, 27, 3, 10, 5, 0, 23, 27, 3, 14, 7, 0, 24, 27,
        3, 16, 8, 0, 25, 27, 3, 12, 6, 0, 26, 20, 1, 0, 0, 0, 26, 21, 1, 0, 0, 0, 26, 22, 1, 0, 0,
        0, 26, 23, 1, 0, 0, 0, 26, 24, 1, 0, 0, 0, 26, 25, 1, 0, 0, 0, 27, 30, 1, 0, 0, 0, 28, 26,
        1, 0, 0, 0, 28, 29, 1, 0, 0, 0, 29, 31, 1, 0, 0, 0, 30, 28, 1, 0, 0, 0, 31, 32, 5, 2, 0, 0,
        32, 1, 1, 0, 0, 0, 33, 34, 7, 0, 0, 0, 34, 3, 1, 0, 0, 0, 35, 36, 7, 1, 0, 0, 36, 5, 1, 0, 0,
        0, 37, 38, 5, 3, 0, 0, 38, 39, 5, 34, 0, 0, 39, 40, 5, 25, 0, 0, 40, 41, 7, 2, 0, 0, 41, 42,
        5, 11, 0, 0, 42, 7, 1, 0, 0, 0, 43, 44, 5, 4, 0, 0, 44, 45, 5, 34, 0, 0, 45, 46, 5, 25, 0,
        0, 46, 47, 5, 27, 0, 0, 47, 52, 7, 3, 0, 0, 48, 49, 5, 31, 0, 0, 49, 51, 7, 3, 0, 0, 50, 48,
        1, 0, 0, 0, 51, 54, 1, 0, 0, 0, 52, 50, 1, 0, 0, 0, 52, 53, 1, 0, 0, 0, 53, 55, 1, 0, 0, 0,
        54, 52, 1, 0, 0, 0, 55, 56, 5, 28, 0, 0, 56, 57, 5, 11, 0, 0, 57, 9, 1, 0, 0, 0, 58, 59, 5,
        34, 0, 0, 59, 60, 5, 12, 0, 0, 60, 61, 7, 4, 0, 0, 61, 62, 3, 2, 1, 0, 62, 68, 7, 4, 0, 0,
        63, 64, 3, 2, 1, 0, 64, 65, 7, 4, 0, 0, 65, 67, 1, 0, 0, 0, 66, 63, 1, 0, 0, 0, 67, 70, 1,
        0, 0, 0, 68, 66, 1, 0, 0, 0, 68, 69, 1, 0, 0, 0, 69, 71, 1, 0, 0, 0, 70, 68, 1, 0, 0, 0, 71,
        72, 5, 11, 0, 0, 72, 11, 1, 0, 0, 0, 73, 74, 5, 18, 0, 0, 74, 75, 7, 4, 0, 0, 75, 76, 3, 4,
        2, 0, 76, 77, 7, 4, 0, 0, 77, 85, 5, 32, 0, 0, 78, 84, 3, 6, 3, 0, 79, 84, 3, 8, 4, 0, 80,
        84, 3, 10, 5, 0, 81, 84, 3, 14, 7, 0, 82, 84, 3, 16, 8, 0, 83, 78, 1, 0, 0, 0, 83, 79, 1,
        0, 0, 0, 83, 80, 1, 0, 0, 0, 83, 81, 1, 0, 0, 0, 83, 82, 1, 0, 0, 0, 84, 87, 1, 0, 0, 0, 85,
        83, 1, 0, 0, 0, 85, 86, 1, 0, 0, 0, 86, 88, 1, 0, 0, 0, 87, 85, 1, 0, 0, 0, 88, 89, 5, 26,
        0, 0, 89, 90, 5, 11, 0, 0, 90, 148, 1, 0, 0, 0, 91, 92, 5, 22, 0, 0, 92, 93, 7, 4, 0, 0, 93,
        94, 3, 4, 2, 0, 94, 95, 7, 4, 0, 0, 95, 103, 5, 32, 0, 0, 96, 102, 3, 6, 3, 0, 97, 102, 3,
        8, 4, 0, 98, 102, 3, 10, 5, 0, 99, 102, 3, 14, 7, 0, 100, 102, 3, 16, 8, 0, 101, 96, 1,
        0, 0, 0, 101, 97, 1, 0, 0, 0, 101, 98, 1, 0, 0, 0, 101, 99, 1, 0, 0, 0, 101, 100, 1, 0, 0,
        0, 102, 105, 1, 0, 0, 0, 103, 101, 1, 0, 0, 0, 103, 104, 1, 0, 0, 0, 104, 106, 1, 0, 0,
        0, 105, 103, 1, 0, 0, 0, 106, 107, 5, 26, 0, 0, 107, 108, 5, 11, 0, 0, 108, 148, 1, 0,
        0, 0, 109, 110, 5, 19, 0, 0, 110, 111, 5, 34, 0, 0, 111, 112, 5, 33, 0, 0, 112, 113, 5,
        34, 0, 0, 113, 121, 5, 32, 0, 0, 114, 120, 3, 6, 3, 0, 115, 120, 3, 8, 4, 0, 116, 120,
        3, 10, 5, 0, 117, 120, 3, 14, 7, 0, 118, 120, 3, 16, 8, 0, 119, 114, 1, 0, 0, 0, 119, 115,
        1, 0, 0, 0, 119, 116, 1, 0, 0, 0, 119, 117, 1, 0, 0, 0, 119, 118, 1, 0, 0, 0, 120, 123,
        1, 0, 0, 0, 121, 119, 1, 0, 0, 0, 121, 122, 1, 0, 0, 0, 122, 124, 1, 0, 0, 0, 123, 121,
        1, 0, 0, 0, 124, 125, 5, 26, 0, 0, 125, 148, 5, 11, 0, 0, 126, 127, 5, 20, 0, 0, 127, 128,
        5, 34, 0, 0, 128, 129, 5, 21, 0, 0, 129, 130, 5, 29, 0, 0, 130, 131, 5, 36, 0, 0, 131,
        132, 5, 11, 0, 0, 132, 133, 5, 36, 0, 0, 133, 134, 5, 30, 0, 0, 134, 142, 5, 32, 0, 0,
        135, 141, 3, 6, 3, 0, 136, 141, 3, 8, 4, 0, 137, 141, 3, 10, 5, 0, 138, 141, 3, 14, 7,
        0, 139, 141, 3, 16, 8, 0, 140, 135, 1, 0, 0, 0, 140, 136, 1, 0, 0, 0, 140, 137, 1, 0, 0,
        0, 140, 138, 1, 0, 0, 0, 140, 139, 1, 0, 0, 0, 141, 144, 1, 0, 0, 0, 142, 140, 1, 0, 0,
        0, 142, 143, 1, 0, 0, 0, 143, 145, 1, 0, 0, 0, 144, 142, 1, 0, 0, 0, 145, 146, 5, 26, 0,
        0, 146, 148, 5, 11, 0, 0, 147, 73, 1, 0, 0, 0, 147, 91, 1, 0, 0, 0, 147, 109, 1, 0, 0, 0,
        147, 126, 1, 0, 0, 0, 148, 13, 1, 0, 0, 0, 149, 150, 5, 23, 0, 0, 150, 151, 5, 29, 0, 0,
        151, 152, 5, 34, 0, 0, 152, 153, 5, 30, 0, 0, 153, 154, 5, 11, 0, 0, 154, 15, 1, 0, 0,
        0, 155, 156, 5, 24, 0, 0, 156, 157, 5, 29, 0, 0, 157, 158, 5, 35, 0, 0, 158, 159, 5, 30,
        0, 0, 159, 160, 5, 11, 0, 0, 160, 17, 1, 0, 0, 0, 13, 26, 28, 52, 68, 83, 85, 101, 103,
        119, 121, 140, 142, 147
    ]


class nlanParser(Parser):
    grammarFileName = "nlan.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "'start'", "'zakoncz'", "'stworzZmienna'",
                    "'stworzTablice'", "<INVALID>", "'dodac'", "'odjac'",
                    "'razy'", "'podzielicPrzez'", "'doPotegi'", "','",
                    "'rownaSie'", "'jestRowne'", "'jestMniejsze'", "'jestMniejszeLubRowne'",
                    "'jestWieksze'", "'jestWiekszeLubRowne'", "'jezeli'",
                    "'dlaKazdegoElementu'", "'dlaKazdejWartosci'", "'ZZakresu'",
                    "'dopoki'", "'wypiszZmienna'", "'wypiszTekst'", "'oWartosci'",
                    "'koniecPetli'", "'['", "']'", "'('", "')'", "'&'",
                    "':'", "'nalezacegoDo'"]

    symbolicNames = ["<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "SPACE", "PLUS", "MINUS", "MULTIPLICATION",
                     "DIVIDE", "POWER", "COMA", "EQ", "DOUBLEEQ", "LESS",
                     "LESSEQ", "GREATER", "GREATEREQ", "IF", "FOREACH",
                     "FORELEMENT", "FORRANGE", "WHILE", "PRINT_VAR", "PRINT_TEXT",
                     "VALUE", "END_LOOP", "LEFT_BR", "RIGHT_BR", "OPEN",
                     "CLOSE", "ARRAYAND", "STARTLOOP", "ARRAY", "ID", "STRING",
                     "NUMBER"]

    RULE_program = 0
    RULE_math_sym = 1
    RULE_compare_sym = 2
    RULE_var_decl = 3
    RULE_arr_decl = 4
    RULE_math = 5
    RULE_loop_exp = 6
    RULE_print_var_exp = 7
    RULE_print_text_exp = 8

    ruleNames = ["program", "math_sym", "compare_sym", "var_decl", "arr_decl",
                 "math", "loop_exp", "print_var_exp", "print_text_exp"]

    EOF = Token.EOF
    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    SPACE = 5
    PLUS = 6
    MINUS = 7
    MULTIPLICATION = 8
    DIVIDE = 9
    POWER = 10
    COMA = 11
    EQ = 12
    DOUBLEEQ = 13
    LESS = 14
    LESSEQ = 15
    GREATER = 16
    GREATEREQ = 17
    IF = 18
    FOREACH = 19
    FORELEMENT = 20
    FORRANGE = 21
    WHILE = 22
    PRINT_VAR = 23
    PRINT_TEXT = 24
    VALUE = 25
    END_LOOP = 26
    LEFT_BR = 27
    RIGHT_BR = 28
    OPEN = 29
    CLOSE = 30
    ARRAYAND = 31
    STARTLOOP = 32
    ARRAY = 33
    ID = 34
    STRING = 35
    NUMBER = 36

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None

    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(nlanParser.COMA, 0)

        def var_decl(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(nlanParser.Var_declContext)
            else:
                return self.getTypedRuleContext(nlanParser.Var_declContext, i)

        def arr_decl(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(nlanParser.Arr_declContext)
            else:
                return self.getTypedRuleContext(nlanParser.Arr_declContext, i)

        def math(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(nlanParser.MathContext)
            else:
                return self.getTypedRuleContext(nlanParser.MathContext, i)

        def print_var_exp(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(nlanParser.Print_var_expContext)
            else:
                return self.getTypedRuleContext(nlanParser.Print_var_expContext, i)

        def print_text_exp(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(nlanParser.Print_text_expContext)
            else:
                return self.getTypedRuleContext(nlanParser.Print_text_expContext, i)

        def loop_exp(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(nlanParser.Loop_expContext)
            else:
                return self.getTypedRuleContext(nlanParser.Loop_expContext, i)

        def getRuleIndex(self):
            return nlanParser.RULE_program

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterProgram"):
                listener.enterProgram(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitProgram"):
                listener.exitProgram(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitProgram"):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)

    def program(self):

        localctx = nlanParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(nlanParser.T__0)
            self.state = 19
            self.match(nlanParser.COMA)
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 17211064344) != 0:
                self.state = 26
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3]:
                    self.state = 20
                    self.var_decl()
                    pass
                elif token in [4]:
                    self.state = 21
                    self.arr_decl()
                    pass
                elif token in [34]:
                    self.state = 22
                    self.math()
                    pass
                elif token in [23]:
                    self.state = 23
                    self.print_var_exp()
                    pass
                elif token in [24]:
                    self.state = 24
                    self.print_text_exp()
                    pass
                elif token in [18, 19, 20, 22]:
                    self.state = 25
                    self.loop_exp()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 31
            self.match(nlanParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Math_symContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(nlanParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(nlanParser.MINUS, 0)

        def MULTIPLICATION(self):
            return self.getToken(nlanParser.MULTIPLICATION, 0)

        def DIVIDE(self):
            return self.getToken(nlanParser.DIVIDE, 0)

        def POWER(self):
            return self.getToken(nlanParser.POWER, 0)

        def getRuleIndex(self):
            return nlanParser.RULE_math_sym

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterMath_sym"):
                listener.enterMath_sym(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitMath_sym"):
                listener.exitMath_sym(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitMath_sym"):
                return visitor.visitMath_sym(self)
            else:
                return visitor.visitChildren(self)

    def math_sym(self):

        localctx = nlanParser.Math_symContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_math_sym)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            _la = self._input.LA(1)
            if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 1984) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Compare_symContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOUBLEEQ(self):
            return self.getToken(nlanParser.DOUBLEEQ, 0)

        def LESS(self):
            return self.getToken(nlanParser.LESS, 0)

        def LESSEQ(self):
            return self.getToken(nlanParser.LESSEQ, 0)

        def GREATER(self):
            return self.getToken(nlanParser.GREATER, 0)

        def GREATEREQ(self):
            return self.getToken(nlanParser.GREATEREQ, 0)

        def getRuleIndex(self):
            return nlanParser.RULE_compare_sym

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterCompare_sym"):
                listener.enterCompare_sym(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitCompare_sym"):
                listener.exitCompare_sym(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitCompare_sym"):
                return visitor.visitCompare_sym(self)
            else:
                return visitor.visitChildren(self)

    def compare_sym(self):

        localctx = nlanParser.Compare_symContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_compare_sym)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            _la = self._input.LA(1)
            if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 253952) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(nlanParser.ID, 0)

        def VALUE(self):
            return self.getToken(nlanParser.VALUE, 0)

        def COMA(self):
            return self.getToken(nlanParser.COMA, 0)

        def STRING(self):
            return self.getToken(nlanParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(nlanParser.NUMBER, 0)

        def getRuleIndex(self):
            return nlanParser.RULE_var_decl

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterVar_decl"):
                listener.enterVar_decl(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitVar_decl"):
                listener.exitVar_decl(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitVar_decl"):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)

    def var_decl(self):

        localctx = nlanParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var_decl)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(nlanParser.T__2)
            self.state = 38
            self.match(nlanParser.ID)
            self.state = 39
            self.match(nlanParser.VALUE)
            self.state = 40
            _la = self._input.LA(1)
            if not (_la == 35 or _la == 36):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 41
            self.match(nlanParser.COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Arr_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i: int = None):
            if i is None:
                return self.getTokens(nlanParser.ID)
            else:
                return self.getToken(nlanParser.ID, i)

        def VALUE(self):
            return self.getToken(nlanParser.VALUE, 0)

        def LEFT_BR(self):
            return self.getToken(nlanParser.LEFT_BR, 0)

        def RIGHT_BR(self):
            return self.getToken(nlanParser.RIGHT_BR, 0)

        def COMA(self):
            return self.getToken(nlanParser.COMA, 0)

        def STRING(self, i: int = None):
            if i is None:
                return self.getTokens(nlanParser.STRING)
            else:
                return self.getToken(nlanParser.STRING, i)

        def NUMBER(self, i: int = None):
            if i is None:
                return self.getTokens(nlanParser.NUMBER)
            else:
                return self.getToken(nlanParser.NUMBER, i)

        def ARRAYAND(self, i: int = None):
            if i is None:
                return self.getTokens(nlanParser.ARRAYAND)
            else:
                return self.getToken(nlanParser.ARRAYAND, i)

        def getRuleIndex(self):
            return nlanParser.RULE_arr_decl

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterArr_decl"):
                listener.enterArr_decl(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitArr_decl"):
                listener.exitArr_decl(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitArr_decl"):
                return visitor.visitArr_decl(self)
            else:
                return visitor.visitChildren(self)

    def arr_decl(self):

        localctx = nlanParser.Arr_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_arr_decl)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(nlanParser.T__3)
            self.state = 44
            self.match(nlanParser.ID)
            self.state = 45
            self.match(nlanParser.VALUE)
            self.state = 46
            self.match(nlanParser.LEFT_BR)
            self.state = 47
            _la = self._input.LA(1)
            if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 120259084288) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 31:
                self.state = 48
                self.match(nlanParser.ARRAYAND)
                self.state = 49
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 120259084288) != 0):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 55
            self.match(nlanParser.RIGHT_BR)
            self.state = 56
            self.match(nlanParser.COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i: int = None):
            if i is None:
                return self.getTokens(nlanParser.ID)
            else:
                return self.getToken(nlanParser.ID, i)

        def EQ(self):
            return self.getToken(nlanParser.EQ, 0)

        def math_sym(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(nlanParser.Math_symContext)
            else:
                return self.getTypedRuleContext(nlanParser.Math_symContext, i)

        def COMA(self):
            return self.getToken(nlanParser.COMA, 0)

        def NUMBER(self, i: int = None):
            if i is None:
                return self.getTokens(nlanParser.NUMBER)
            else:
                return self.getToken(nlanParser.NUMBER, i)

        def getRuleIndex(self):
            return nlanParser.RULE_math

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterMath"):
                listener.enterMath(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitMath"):
                listener.exitMath(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitMath"):
                return visitor.visitMath(self)
            else:
                return visitor.visitChildren(self)

    def math(self):

        localctx = nlanParser.MathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_math)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(nlanParser.ID)
            self.state = 59
            self.match(nlanParser.EQ)
            self.state = 60
            _la = self._input.LA(1)
            if not (_la == 34 or _la == 36):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 61
            self.math_sym()
            self.state = 62
            _la = self._input.LA(1)
            if not (_la == 34 or _la == 36):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 1984) != 0:
                self.state = 63
                self.math_sym()
                self.state = 64
                _la = self._input.LA(1)
                if not (_la == 34 or _la == 36):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 71
            self.match(nlanParser.COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Loop_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(nlanParser.IF, 0)

        def compare_sym(self):
            return self.getTypedRuleContext(nlanParser.Compare_symContext, 0)

        def STARTLOOP(self):
            return self.getToken(nlanParser.STARTLOOP, 0)

        def END_LOOP(self):
            return self.getToken(nlanParser.END_LOOP, 0)

        def COMA(self, i: int = None):
            if i is None:
                return self.getTokens(nlanParser.COMA)
            else:
                return self.getToken(nlanParser.COMA, i)

        def ID(self, i: int = None):
            if i is None:
                return self.getTokens(nlanParser.ID)
            else:
                return self.getToken(nlanParser.ID, i)

        def NUMBER(self, i: int = None):
            if i is None:
                return self.getTokens(nlanParser.NUMBER)
            else:
                return self.getToken(nlanParser.NUMBER, i)

        def var_decl(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(nlanParser.Var_declContext)
            else:
                return self.getTypedRuleContext(nlanParser.Var_declContext, i)

        def arr_decl(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(nlanParser.Arr_declContext)
            else:
                return self.getTypedRuleContext(nlanParser.Arr_declContext, i)

        def math(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(nlanParser.MathContext)
            else:
                return self.getTypedRuleContext(nlanParser.MathContext, i)

        def print_var_exp(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(nlanParser.Print_var_expContext)
            else:
                return self.getTypedRuleContext(nlanParser.Print_var_expContext, i)

        def print_text_exp(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(nlanParser.Print_text_expContext)
            else:
                return self.getTypedRuleContext(nlanParser.Print_text_expContext, i)

        def WHILE(self):
            return self.getToken(nlanParser.WHILE, 0)

        def FOREACH(self):
            return self.getToken(nlanParser.FOREACH, 0)

        def ARRAY(self):
            return self.getToken(nlanParser.ARRAY, 0)

        def FORELEMENT(self):
            return self.getToken(nlanParser.FORELEMENT, 0)

        def FORRANGE(self):
            return self.getToken(nlanParser.FORRANGE, 0)

        def OPEN(self):
            return self.getToken(nlanParser.OPEN, 0)

        def CLOSE(self):
            return self.getToken(nlanParser.CLOSE, 0)

        def getRuleIndex(self):
            return nlanParser.RULE_loop_exp

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterLoop_exp"):
                listener.enterLoop_exp(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitLoop_exp"):
                listener.exitLoop_exp(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitLoop_exp"):
                return visitor.visitLoop_exp(self)
            else:
                return visitor.visitChildren(self)

    def loop_exp(self):

        localctx = nlanParser.Loop_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_loop_exp)
        self._la = 0  # Token type
        try:
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.match(nlanParser.IF)
                self.state = 74
                _la = self._input.LA(1)
                if not (_la == 34 or _la == 36):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 75
                self.compare_sym()
                self.state = 76
                _la = self._input.LA(1)
                if not (_la == 34 or _la == 36):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 77
                self.match(nlanParser.STARTLOOP)
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while ((_la) & ~0x3f) == 0 and ((1 << _la) & 17205035032) != 0:
                    self.state = 83
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [3]:
                        self.state = 78
                        self.var_decl()
                        pass
                    elif token in [4]:
                        self.state = 79
                        self.arr_decl()
                        pass
                    elif token in [34]:
                        self.state = 80
                        self.math()
                        pass
                    elif token in [23]:
                        self.state = 81
                        self.print_var_exp()
                        pass
                    elif token in [24]:
                        self.state = 82
                        self.print_text_exp()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 87
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 88
                self.match(nlanParser.END_LOOP)
                self.state = 89
                self.match(nlanParser.COMA)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.match(nlanParser.WHILE)
                self.state = 92
                _la = self._input.LA(1)
                if not (_la == 34 or _la == 36):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 93
                self.compare_sym()
                self.state = 94
                _la = self._input.LA(1)
                if not (_la == 34 or _la == 36):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 95
                self.match(nlanParser.STARTLOOP)
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while ((_la) & ~0x3f) == 0 and ((1 << _la) & 17205035032) != 0:
                    self.state = 101
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [3]:
                        self.state = 96
                        self.var_decl()
                        pass
                    elif token in [4]:
                        self.state = 97
                        self.arr_decl()
                        pass
                    elif token in [34]:
                        self.state = 98
                        self.math()
                        pass
                    elif token in [23]:
                        self.state = 99
                        self.print_var_exp()
                        pass
                    elif token in [24]:
                        self.state = 100
                        self.print_text_exp()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 105
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 106
                self.match(nlanParser.END_LOOP)
                self.state = 107
                self.match(nlanParser.COMA)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 3)
                self.state = 109
                self.match(nlanParser.FOREACH)
                self.state = 110
                self.match(nlanParser.ID)
                self.state = 111
                self.match(nlanParser.ARRAY)
                self.state = 112
                self.match(nlanParser.ID)
                self.state = 113
                self.match(nlanParser.STARTLOOP)
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while ((_la) & ~0x3f) == 0 and ((1 << _la) & 17205035032) != 0:
                    self.state = 119
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [3]:
                        self.state = 114
                        self.var_decl()
                        pass
                    elif token in [4]:
                        self.state = 115
                        self.arr_decl()
                        pass
                    elif token in [34]:
                        self.state = 116
                        self.math()
                        pass
                    elif token in [23]:
                        self.state = 117
                        self.print_var_exp()
                        pass
                    elif token in [24]:
                        self.state = 118
                        self.print_text_exp()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 123
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 124
                self.match(nlanParser.END_LOOP)
                self.state = 125
                self.match(nlanParser.COMA)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 4)
                self.state = 126
                self.match(nlanParser.FORELEMENT)
                self.state = 127
                self.match(nlanParser.ID)
                self.state = 128
                self.match(nlanParser.FORRANGE)
                self.state = 129
                self.match(nlanParser.OPEN)
                self.state = 130
                self.match(nlanParser.NUMBER)
                self.state = 131
                self.match(nlanParser.COMA)
                self.state = 132
                self.match(nlanParser.NUMBER)
                self.state = 133
                self.match(nlanParser.CLOSE)
                self.state = 134
                self.match(nlanParser.STARTLOOP)
                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while ((_la) & ~0x3f) == 0 and ((1 << _la) & 17205035032) != 0:
                    self.state = 140
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [3]:
                        self.state = 135
                        self.var_decl()
                        pass
                    elif token in [4]:
                        self.state = 136
                        self.arr_decl()
                        pass
                    elif token in [34]:
                        self.state = 137
                        self.math()
                        pass
                    elif token in [23]:
                        self.state = 138
                        self.print_var_exp()
                        pass
                    elif token in [24]:
                        self.state = 139
                        self.print_text_exp()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 144
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 145
                self.match(nlanParser.END_LOOP)
                self.state = 146
                self.match(nlanParser.COMA)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Print_var_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT_VAR(self):
            return self.getToken(nlanParser.PRINT_VAR, 0)

        def OPEN(self):
            return self.getToken(nlanParser.OPEN, 0)

        def ID(self):
            return self.getToken(nlanParser.ID, 0)

        def CLOSE(self):
            return self.getToken(nlanParser.CLOSE, 0)

        def COMA(self):
            return self.getToken(nlanParser.COMA, 0)

        def getRuleIndex(self):
            return nlanParser.RULE_print_var_exp

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterPrint_var_exp"):
                listener.enterPrint_var_exp(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitPrint_var_exp"):
                listener.exitPrint_var_exp(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitPrint_var_exp"):
                return visitor.visitPrint_var_exp(self)
            else:
                return visitor.visitChildren(self)

    def print_var_exp(self):

        localctx = nlanParser.Print_var_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_print_var_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(nlanParser.PRINT_VAR)
            self.state = 150
            self.match(nlanParser.OPEN)
            self.state = 151
            self.match(nlanParser.ID)
            self.state = 152
            self.match(nlanParser.CLOSE)
            self.state = 153
            self.match(nlanParser.COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Print_text_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT_TEXT(self):
            return self.getToken(nlanParser.PRINT_TEXT, 0)

        def OPEN(self):
            return self.getToken(nlanParser.OPEN, 0)

        def STRING(self):
            return self.getToken(nlanParser.STRING, 0)

        def CLOSE(self):
            return self.getToken(nlanParser.CLOSE, 0)

        def COMA(self):
            return self.getToken(nlanParser.COMA, 0)

        def getRuleIndex(self):
            return nlanParser.RULE_print_text_exp

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterPrint_text_exp"):
                listener.enterPrint_text_exp(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitPrint_text_exp"):
                listener.exitPrint_text_exp(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitPrint_text_exp"):
                return visitor.visitPrint_text_exp(self)
            else:
                return visitor.visitChildren(self)

    def print_text_exp(self):

        localctx = nlanParser.Print_text_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_print_text_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(nlanParser.PRINT_TEXT)
            self.state = 156
            self.match(nlanParser.OPEN)
            self.state = 157
            self.match(nlanParser.STRING)
            self.state = 158
            self.match(nlanParser.CLOSE)
            self.state = 159
            self.match(nlanParser.COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
