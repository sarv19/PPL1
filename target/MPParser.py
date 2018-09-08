# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\33")
        buf.write("(\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\5\2\23\n\2\3\2\3\2\3\2\3\3\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\5\6$\n\6\3\6\3\6\3\6\2")
        buf.write("\2\7\2\4\6\b\n\2\2\2$\2\f\3\2\2\2\4\27\3\2\2\2\6\32\3")
        buf.write("\2\2\2\b\35\3\2\2\2\n \3\2\2\2\f\r\5\4\3\2\r\16\7\3\2")
        buf.write("\2\16\17\7\n\2\2\17\20\7\13\2\2\20\22\7\f\2\2\21\23\5")
        buf.write("\6\4\2\22\21\3\2\2\2\22\23\3\2\2\2\23\24\3\2\2\2\24\25")
        buf.write("\7\r\2\2\25\26\7\2\2\3\26\3\3\2\2\2\27\30\7\4\2\2\30\31")
        buf.write("\7\5\2\2\31\5\3\2\2\2\32\33\5\n\6\2\33\34\7\16\2\2\34")
        buf.write("\7\3\2\2\2\35\36\5\n\6\2\36\37\7\26\2\2\37\t\3\2\2\2 ")
        buf.write("!\7\25\2\2!#\7\n\2\2\"$\5\b\5\2#\"\3\2\2\2#$\3\2\2\2$")
        buf.write("%\3\2\2\2%&\7\13\2\2&\13\3\2\2\2\4\22#")
        return buf.getvalue()


class MPParser ( Parser ):

    grammarFileName = "MP.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "'int'", "'void'", "'real'", 
                     "'boolean'", "'string'", "'array'", "'('", "')'", "'{'", 
                     "'}'", "';'", "','", "'='", "':'", "'..'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "INTTYPE", "VOIDTYPE", "REALTYPE", 
                      "BOOLEANTYPE", "STRINGTYPE", "ARRAYTYPE", "LB", "RB", 
                      "LP", "RP", "SEMI", "CM", "EQ", "COL", "DD", "WS", 
                      "AND", "ID", "INTLIT", "REALLIT", "BOOLLIT", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_mptype = 1
    RULE_body = 2
    RULE_exp = 3
    RULE_funcall = 4

    ruleNames =  [ "program", "mptype", "body", "exp", "funcall" ]

    EOF = Token.EOF
    T__0=1
    INTTYPE=2
    VOIDTYPE=3
    REALTYPE=4
    BOOLEANTYPE=5
    STRINGTYPE=6
    ARRAYTYPE=7
    LB=8
    RB=9
    LP=10
    RP=11
    SEMI=12
    CM=13
    EQ=14
    COL=15
    DD=16
    WS=17
    AND=18
    ID=19
    INTLIT=20
    REALLIT=21
    BOOLLIT=22
    ERROR_CHAR=23
    UNCLOSE_STRING=24
    ILLEGAL_ESCAPE=25

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mptype(self):
            return self.getTypedRuleContext(MPParser.MptypeContext,0)


        def LB(self):
            return self.getToken(MPParser.LB, 0)

        def RB(self):
            return self.getToken(MPParser.RB, 0)

        def LP(self):
            return self.getToken(MPParser.LP, 0)

        def RP(self):
            return self.getToken(MPParser.RP, 0)

        def EOF(self):
            return self.getToken(MPParser.EOF, 0)

        def body(self):
            return self.getTypedRuleContext(MPParser.BodyContext,0)


        def getRuleIndex(self):
            return MPParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MPParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.mptype()
            self.state = 11
            self.match(MPParser.T__0)
            self.state = 12
            self.match(MPParser.LB)
            self.state = 13
            self.match(MPParser.RB)
            self.state = 14
            self.match(MPParser.LP)
            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MPParser.ID:
                self.state = 15
                self.body()


            self.state = 18
            self.match(MPParser.RP)
            self.state = 19
            self.match(MPParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MptypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(MPParser.INTTYPE, 0)

        def VOIDTYPE(self):
            return self.getToken(MPParser.VOIDTYPE, 0)

        def getRuleIndex(self):
            return MPParser.RULE_mptype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMptype" ):
                return visitor.visitMptype(self)
            else:
                return visitor.visitChildren(self)




    def mptype(self):

        localctx = MPParser.MptypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mptype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.match(MPParser.INTTYPE)
            self.state = 22
            self.match(MPParser.VOIDTYPE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall(self):
            return self.getTypedRuleContext(MPParser.FuncallContext,0)


        def SEMI(self):
            return self.getToken(MPParser.SEMI, 0)

        def getRuleIndex(self):
            return MPParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = MPParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.funcall()
            self.state = 25
            self.match(MPParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall(self):
            return self.getTypedRuleContext(MPParser.FuncallContext,0)


        def INTLIT(self):
            return self.getToken(MPParser.INTLIT, 0)

        def getRuleIndex(self):
            return MPParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = MPParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.funcall()
            self.state = 28
            self.match(MPParser.INTLIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MPParser.ID, 0)

        def LB(self):
            return self.getToken(MPParser.LB, 0)

        def RB(self):
            return self.getToken(MPParser.RB, 0)

        def exp(self):
            return self.getTypedRuleContext(MPParser.ExpContext,0)


        def getRuleIndex(self):
            return MPParser.RULE_funcall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncall" ):
                return visitor.visitFuncall(self)
            else:
                return visitor.visitChildren(self)




    def funcall(self):

        localctx = MPParser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_funcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(MPParser.ID)
            self.state = 31
            self.match(MPParser.LB)
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MPParser.ID:
                self.state = 32
                self.exp()


            self.state = 35
            self.match(MPParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





