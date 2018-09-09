# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3D")
        buf.write("]\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\5\5\31\n\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5#\n\5\f\5\16\5&\13\5\3\5")
        buf.write("\3\5\6\5*\n\5\r\5\16\5+\3\5\3\5\3\6\3\6\6\6\62\n\6\r\6")
        buf.write("\16\6\63\3\6\3\6\7\68\n\6\f\6\16\6;\13\6\3\6\3\6\7\6?")
        buf.write("\n\6\f\6\16\6B\13\6\3\6\3\6\7\6F\n\6\f\6\16\6I\13\6\3")
        buf.write("\6\3\6\6\6M\n\6\r\6\16\6N\3\7\3\7\5\7S\n\7\3\b\3\b\3\b")
        buf.write("\7\bX\n\b\f\b\16\b[\13\b\3\b\2\2\t\2\4\6\b\n\f\16\2\3")
        buf.write("\3\2,/\2_\2\20\3\2\2\2\4\22\3\2\2\2\6\24\3\2\2\2\b\26")
        buf.write("\3\2\2\2\n/\3\2\2\2\fR\3\2\2\2\16T\3\2\2\2\20\21\5\4\3")
        buf.write("\2\21\3\3\2\2\2\22\23\5\n\6\2\23\5\3\2\2\2\24\25\t\2\2")
        buf.write("\2\25\7\3\2\2\2\26\30\7*\2\2\27\31\7\27\2\2\30\27\3\2")
        buf.write("\2\2\30\31\3\2\2\2\31\32\3\2\2\2\32\33\7\7\2\2\33\34\7")
        buf.write("\65\2\2\34\35\7\27\2\2\35\36\7\r\2\2\36\37\7\27\2\2\37")
        buf.write(" \7\65\2\2 $\7\b\2\2!#\7\27\2\2\"!\3\2\2\2#&\3\2\2\2$")
        buf.write("\"\3\2\2\2$%\3\2\2\2%\'\3\2\2\2&$\3\2\2\2\')\7+\2\2(*")
        buf.write("\7\27\2\2)(\3\2\2\2*+\3\2\2\2+)\3\2\2\2+,\3\2\2\2,-\3")
        buf.write("\2\2\2-.\5\6\4\2.\t\3\2\2\2/\61\7\'\2\2\60\62\7\27\2\2")
        buf.write("\61\60\3\2\2\2\62\63\3\2\2\2\63\61\3\2\2\2\63\64\3\2\2")
        buf.write("\2\64L\3\2\2\2\659\5\16\b\2\668\7\27\2\2\67\66\3\2\2\2")
        buf.write("8;\3\2\2\29\67\3\2\2\29:\3\2\2\2:<\3\2\2\2;9\3\2\2\2<")
        buf.write("@\7\f\2\2=?\7\27\2\2>=\3\2\2\2?B\3\2\2\2@>\3\2\2\2@A\3")
        buf.write("\2\2\2AC\3\2\2\2B@\3\2\2\2CG\5\f\7\2DF\7\27\2\2ED\3\2")
        buf.write("\2\2FI\3\2\2\2GE\3\2\2\2GH\3\2\2\2HJ\3\2\2\2IG\3\2\2\2")
        buf.write("JK\7\t\2\2KM\3\2\2\2L\65\3\2\2\2MN\3\2\2\2NL\3\2\2\2N")
        buf.write("O\3\2\2\2O\13\3\2\2\2PS\5\6\4\2QS\5\b\5\2RP\3\2\2\2RQ")
        buf.write("\3\2\2\2S\r\3\2\2\2TY\7\66\2\2UV\7\n\2\2VX\7\66\2\2WU")
        buf.write("\3\2\2\2X[\3\2\2\2YW\3\2\2\2YZ\3\2\2\2Z\17\3\2\2\2[Y\3")
        buf.write("\2\2\2\f\30$+\639@GNRY")
        return buf.getvalue()


class MPParser ( Parser ):

    grammarFileName = "MP.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "';'", "','", "'='", "':'", "'..'", "'+'", "'*'", "'<>'", 
                     "'<'", "'<='", "'-'", "'/'", "'>'", "'>='", "' '" ]

    symbolicNames = [ "<INVALID>", "LB", "RB", "LP", "RP", "LQ", "RQ", "SEMI", 
                      "CM", "EQ", "COL", "DD", "ADD", "MUL", "NOTEQ", "LESSTN", 
                      "LESSEQ", "SUBNE", "DIVSI", "GRETN", "GREEQ", "SP", 
                      "BREAK", "CONTINUE", "FOR", "TO", "DOWNTO", "DO", 
                      "IF", "THEN", "ELSE", "RETURN", "WHILE", "BEGIN", 
                      "END", "FUNCTION", "PROCEDURE", "VAR", "TRUE", "FALSE", 
                      "ARRAY", "OF", "REAL", "BOOLEAN", "INTEGER", "STRING", 
                      "NOT", "AND", "OR", "DIV", "MOD", "ManyNum", "ID", 
                      "INTLIT", "REALLIT", "BOOLLIT", "STRINGLIT", "TYPE", 
                      "CMT", "BLKCMT", "TRACMT", "BLCMT", "LINECMT", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "WS" ]

    RULE_program = 0
    RULE_manydeclares = 1
    RULE_primtype = 2
    RULE_arrtype = 3
    RULE_varde = 4
    RULE_vartype = 5
    RULE_idlist = 6

    ruleNames =  [ "program", "manydeclares", "primtype", "arrtype", "varde", 
                   "vartype", "idlist" ]

    EOF = Token.EOF
    LB=1
    RB=2
    LP=3
    RP=4
    LQ=5
    RQ=6
    SEMI=7
    CM=8
    EQ=9
    COL=10
    DD=11
    ADD=12
    MUL=13
    NOTEQ=14
    LESSTN=15
    LESSEQ=16
    SUBNE=17
    DIVSI=18
    GRETN=19
    GREEQ=20
    SP=21
    BREAK=22
    CONTINUE=23
    FOR=24
    TO=25
    DOWNTO=26
    DO=27
    IF=28
    THEN=29
    ELSE=30
    RETURN=31
    WHILE=32
    BEGIN=33
    END=34
    FUNCTION=35
    PROCEDURE=36
    VAR=37
    TRUE=38
    FALSE=39
    ARRAY=40
    OF=41
    REAL=42
    BOOLEAN=43
    INTEGER=44
    STRING=45
    NOT=46
    AND=47
    OR=48
    DIV=49
    MOD=50
    ManyNum=51
    ID=52
    INTLIT=53
    REALLIT=54
    BOOLLIT=55
    STRINGLIT=56
    TYPE=57
    CMT=58
    BLKCMT=59
    TRACMT=60
    BLCMT=61
    LINECMT=62
    ERROR_CHAR=63
    UNCLOSE_STRING=64
    ILLEGAL_ESCAPE=65
    WS=66

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def manydeclares(self):
            return self.getTypedRuleContext(MPParser.ManydeclaresContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.manydeclares()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ManydeclaresContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varde(self):
            return self.getTypedRuleContext(MPParser.VardeContext,0)


        def getRuleIndex(self):
            return MPParser.RULE_manydeclares

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitManydeclares" ):
                return visitor.visitManydeclares(self)
            else:
                return visitor.visitChildren(self)




    def manydeclares(self):

        localctx = MPParser.ManydeclaresContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_manydeclares)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.varde()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PrimtypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(MPParser.BOOLEAN, 0)

        def INTEGER(self):
            return self.getToken(MPParser.INTEGER, 0)

        def REAL(self):
            return self.getToken(MPParser.REAL, 0)

        def STRING(self):
            return self.getToken(MPParser.STRING, 0)

        def getRuleIndex(self):
            return MPParser.RULE_primtype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimtype" ):
                return visitor.visitPrimtype(self)
            else:
                return visitor.visitChildren(self)




    def primtype(self):

        localctx = MPParser.PrimtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_primtype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MPParser.REAL) | (1 << MPParser.BOOLEAN) | (1 << MPParser.INTEGER) | (1 << MPParser.STRING))) != 0)):
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

    class ArrtypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(MPParser.ARRAY, 0)

        def LQ(self):
            return self.getToken(MPParser.LQ, 0)

        def ManyNum(self, i:int=None):
            if i is None:
                return self.getTokens(MPParser.ManyNum)
            else:
                return self.getToken(MPParser.ManyNum, i)

        def SP(self, i:int=None):
            if i is None:
                return self.getTokens(MPParser.SP)
            else:
                return self.getToken(MPParser.SP, i)

        def DD(self):
            return self.getToken(MPParser.DD, 0)

        def RQ(self):
            return self.getToken(MPParser.RQ, 0)

        def OF(self):
            return self.getToken(MPParser.OF, 0)

        def primtype(self):
            return self.getTypedRuleContext(MPParser.PrimtypeContext,0)


        def getRuleIndex(self):
            return MPParser.RULE_arrtype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrtype" ):
                return visitor.visitArrtype(self)
            else:
                return visitor.visitChildren(self)




    def arrtype(self):

        localctx = MPParser.ArrtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_arrtype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.match(MPParser.ARRAY)
            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MPParser.SP:
                self.state = 21
                self.match(MPParser.SP)


            self.state = 24
            self.match(MPParser.LQ)
            self.state = 25
            self.match(MPParser.ManyNum)
            self.state = 26
            self.match(MPParser.SP)
            self.state = 27
            self.match(MPParser.DD)
            self.state = 28
            self.match(MPParser.SP)
            self.state = 29
            self.match(MPParser.ManyNum)
            self.state = 30
            self.match(MPParser.RQ)
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MPParser.SP:
                self.state = 31
                self.match(MPParser.SP)
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 37
            self.match(MPParser.OF)
            self.state = 39 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 38
                self.match(MPParser.SP)
                self.state = 41 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MPParser.SP):
                    break

            self.state = 43
            self.primtype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VardeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MPParser.VAR, 0)

        def SP(self, i:int=None):
            if i is None:
                return self.getTokens(MPParser.SP)
            else:
                return self.getToken(MPParser.SP, i)

        def idlist(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MPParser.IdlistContext)
            else:
                return self.getTypedRuleContext(MPParser.IdlistContext,i)


        def COL(self, i:int=None):
            if i is None:
                return self.getTokens(MPParser.COL)
            else:
                return self.getToken(MPParser.COL, i)

        def vartype(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MPParser.VartypeContext)
            else:
                return self.getTypedRuleContext(MPParser.VartypeContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MPParser.SEMI)
            else:
                return self.getToken(MPParser.SEMI, i)

        def getRuleIndex(self):
            return MPParser.RULE_varde

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarde" ):
                return visitor.visitVarde(self)
            else:
                return visitor.visitChildren(self)




    def varde(self):

        localctx = MPParser.VardeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_varde)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(MPParser.VAR)
            self.state = 47 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 46
                self.match(MPParser.SP)
                self.state = 49 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MPParser.SP):
                    break

            self.state = 74 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 51
                self.idlist()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MPParser.SP:
                    self.state = 52
                    self.match(MPParser.SP)
                    self.state = 57
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 58
                self.match(MPParser.COL)
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MPParser.SP:
                    self.state = 59
                    self.match(MPParser.SP)
                    self.state = 64
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 65
                self.vartype()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MPParser.SP:
                    self.state = 66
                    self.match(MPParser.SP)
                    self.state = 71
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 72
                self.match(MPParser.SEMI)
                self.state = 76 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MPParser.ID):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VartypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primtype(self):
            return self.getTypedRuleContext(MPParser.PrimtypeContext,0)


        def arrtype(self):
            return self.getTypedRuleContext(MPParser.ArrtypeContext,0)


        def getRuleIndex(self):
            return MPParser.RULE_vartype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVartype" ):
                return visitor.visitVartype(self)
            else:
                return visitor.visitChildren(self)




    def vartype(self):

        localctx = MPParser.VartypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_vartype)
        try:
            self.state = 80
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MPParser.REAL, MPParser.BOOLEAN, MPParser.INTEGER, MPParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.primtype()
                pass
            elif token in [MPParser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.arrtype()
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

    class IdlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MPParser.ID)
            else:
                return self.getToken(MPParser.ID, i)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(MPParser.CM)
            else:
                return self.getToken(MPParser.CM, i)

        def getRuleIndex(self):
            return MPParser.RULE_idlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = MPParser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_idlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(MPParser.ID)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MPParser.CM:
                self.state = 83
                self.match(MPParser.CM)
                self.state = 84
                self.match(MPParser.ID)
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





