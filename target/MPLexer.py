# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\33")
        buf.write("\u00e5\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3")
        buf.write("\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3")
        buf.write("\17\3\20\3\20\3\21\3\21\3\21\3\22\6\22x\n\22\r\22\16\22")
        buf.write("y\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\25\3\25\3")
        buf.write("\26\3\26\3\27\5\27\u0089\n\27\3\27\7\27\u008c\n\27\f\27")
        buf.write("\16\27\u008f\13\27\3\30\6\30\u0092\n\30\r\30\16\30\u0093")
        buf.write("\3\31\5\31\u0097\n\31\3\31\6\31\u009a\n\31\r\31\16\31")
        buf.write("\u009b\3\31\5\31\u009f\n\31\3\31\7\31\u00a2\n\31\f\31")
        buf.write("\16\31\u00a5\13\31\3\31\6\31\u00a8\n\31\r\31\16\31\u00a9")
        buf.write("\3\31\3\31\5\31\u00ae\n\31\3\31\6\31\u00b1\n\31\r\31\16")
        buf.write("\31\u00b2\5\31\u00b5\n\31\3\31\5\31\u00b8\n\31\3\31\7")
        buf.write("\31\u00bb\n\31\f\31\16\31\u00be\13\31\3\31\5\31\u00c1")
        buf.write("\n\31\3\31\6\31\u00c4\n\31\r\31\16\31\u00c5\3\31\3\31")
        buf.write("\5\31\u00ca\n\31\3\31\6\31\u00cd\n\31\r\31\16\31\u00ce")
        buf.write("\5\31\u00d1\n\31\5\31\u00d3\n\31\3\32\3\32\3\32\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\32\5\32\u00de\n\32\3\33\3\33\3\34")
        buf.write("\3\34\3\35\3\35\2\2\36\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\2)\2+\2-\25/\26\61\27\63\30\65\31\67\329\33\3\2\13")
        buf.write("\5\2\13\f\17\17\"\"\4\2CCcc\4\2PPpp\4\2PPff\5\2C\\aac")
        buf.write("|\6\2\62;C\\aac|\3\2\62;\4\2--//\4\2GGgg\2\u00f5\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\3;\3\2\2\2\5@\3\2")
        buf.write("\2\2\7D\3\2\2\2\tI\3\2\2\2\13N\3\2\2\2\rV\3\2\2\2\17]")
        buf.write("\3\2\2\2\21c\3\2\2\2\23e\3\2\2\2\25g\3\2\2\2\27i\3\2\2")
        buf.write("\2\31k\3\2\2\2\33m\3\2\2\2\35o\3\2\2\2\37q\3\2\2\2!s\3")
        buf.write("\2\2\2#w\3\2\2\2%}\3\2\2\2\'\u0081\3\2\2\2)\u0083\3\2")
        buf.write("\2\2+\u0085\3\2\2\2-\u0088\3\2\2\2/\u0091\3\2\2\2\61\u00d2")
        buf.write("\3\2\2\2\63\u00dd\3\2\2\2\65\u00df\3\2\2\2\67\u00e1\3")
        buf.write("\2\2\29\u00e3\3\2\2\2;<\7o\2\2<=\7c\2\2=>\7k\2\2>?\7p")
        buf.write("\2\2?\4\3\2\2\2@A\7k\2\2AB\7p\2\2BC\7v\2\2C\6\3\2\2\2")
        buf.write("DE\7x\2\2EF\7q\2\2FG\7k\2\2GH\7f\2\2H\b\3\2\2\2IJ\7t\2")
        buf.write("\2JK\7g\2\2KL\7c\2\2LM\7n\2\2M\n\3\2\2\2NO\7d\2\2OP\7")
        buf.write("q\2\2PQ\7q\2\2QR\7n\2\2RS\7g\2\2ST\7c\2\2TU\7p\2\2U\f")
        buf.write("\3\2\2\2VW\7u\2\2WX\7v\2\2XY\7t\2\2YZ\7k\2\2Z[\7p\2\2")
        buf.write("[\\\7i\2\2\\\16\3\2\2\2]^\7c\2\2^_\7t\2\2_`\7t\2\2`a\7")
        buf.write("c\2\2ab\7{\2\2b\20\3\2\2\2cd\7*\2\2d\22\3\2\2\2ef\7+\2")
        buf.write("\2f\24\3\2\2\2gh\7}\2\2h\26\3\2\2\2ij\7\177\2\2j\30\3")
        buf.write("\2\2\2kl\7=\2\2l\32\3\2\2\2mn\7.\2\2n\34\3\2\2\2op\7?")
        buf.write("\2\2p\36\3\2\2\2qr\7<\2\2r \3\2\2\2st\7\60\2\2tu\7\60")
        buf.write("\2\2u\"\3\2\2\2vx\t\2\2\2wv\3\2\2\2xy\3\2\2\2yw\3\2\2")
        buf.write("\2yz\3\2\2\2z{\3\2\2\2{|\b\22\2\2|$\3\2\2\2}~\5\'\24\2")
        buf.write("~\177\5)\25\2\177\u0080\5+\26\2\u0080&\3\2\2\2\u0081\u0082")
        buf.write("\t\3\2\2\u0082(\3\2\2\2\u0083\u0084\t\4\2\2\u0084*\3\2")
        buf.write("\2\2\u0085\u0086\t\5\2\2\u0086,\3\2\2\2\u0087\u0089\t")
        buf.write("\6\2\2\u0088\u0087\3\2\2\2\u0089\u008d\3\2\2\2\u008a\u008c")
        buf.write("\t\7\2\2\u008b\u008a\3\2\2\2\u008c\u008f\3\2\2\2\u008d")
        buf.write("\u008b\3\2\2\2\u008d\u008e\3\2\2\2\u008e.\3\2\2\2\u008f")
        buf.write("\u008d\3\2\2\2\u0090\u0092\t\b\2\2\u0091\u0090\3\2\2\2")
        buf.write("\u0092\u0093\3\2\2\2\u0093\u0091\3\2\2\2\u0093\u0094\3")
        buf.write("\2\2\2\u0094\60\3\2\2\2\u0095\u0097\t\t\2\2\u0096\u0095")
        buf.write("\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0099\3\2\2\2\u0098")
        buf.write("\u009a\t\b\2\2\u0099\u0098\3\2\2\2\u009a\u009b\3\2\2\2")
        buf.write("\u009b\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u009e\3")
        buf.write("\2\2\2\u009d\u009f\7\60\2\2\u009e\u009d\3\2\2\2\u009e")
        buf.write("\u009f\3\2\2\2\u009f\u00a3\3\2\2\2\u00a0\u00a2\t\b\2\2")
        buf.write("\u00a1\u00a0\3\2\2\2\u00a2\u00a5\3\2\2\2\u00a3\u00a1\3")
        buf.write("\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00b4\3\2\2\2\u00a5\u00a3")
        buf.write("\3\2\2\2\u00a6\u00a8\t\b\2\2\u00a7\u00a6\3\2\2\2\u00a8")
        buf.write("\u00a9\3\2\2\2\u00a9\u00a7\3\2\2\2\u00a9\u00aa\3\2\2\2")
        buf.write("\u00aa\u00ab\3\2\2\2\u00ab\u00ad\t\n\2\2\u00ac\u00ae\7")
        buf.write("/\2\2\u00ad\u00ac\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00b0")
        buf.write("\3\2\2\2\u00af\u00b1\t\b\2\2\u00b0\u00af\3\2\2\2\u00b1")
        buf.write("\u00b2\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b2\u00b3\3\2\2\2")
        buf.write("\u00b3\u00b5\3\2\2\2\u00b4\u00a7\3\2\2\2\u00b4\u00b5\3")
        buf.write("\2\2\2\u00b5\u00d3\3\2\2\2\u00b6\u00b8\t\t\2\2\u00b7\u00b6")
        buf.write("\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00bc\3\2\2\2\u00b9")
        buf.write("\u00bb\t\b\2\2\u00ba\u00b9\3\2\2\2\u00bb\u00be\3\2\2\2")
        buf.write("\u00bc\u00ba\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\u00c0\3")
        buf.write("\2\2\2\u00be\u00bc\3\2\2\2\u00bf\u00c1\7\60\2\2\u00c0")
        buf.write("\u00bf\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00c3\3\2\2\2")
        buf.write("\u00c2\u00c4\t\b\2\2\u00c3\u00c2\3\2\2\2\u00c4\u00c5\3")
        buf.write("\2\2\2\u00c5\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00d0")
        buf.write("\3\2\2\2\u00c7\u00c9\t\n\2\2\u00c8\u00ca\7/\2\2\u00c9")
        buf.write("\u00c8\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00cc\3\2\2\2")
        buf.write("\u00cb\u00cd\t\b\2\2\u00cc\u00cb\3\2\2\2\u00cd\u00ce\3")
        buf.write("\2\2\2\u00ce\u00cc\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d1")
        buf.write("\3\2\2\2\u00d0\u00c7\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1")
        buf.write("\u00d3\3\2\2\2\u00d2\u0096\3\2\2\2\u00d2\u00b7\3\2\2\2")
        buf.write("\u00d3\62\3\2\2\2\u00d4\u00d5\7v\2\2\u00d5\u00d6\7t\2")
        buf.write("\2\u00d6\u00d7\7w\2\2\u00d7\u00de\7g\2\2\u00d8\u00d9\7")
        buf.write("h\2\2\u00d9\u00da\7c\2\2\u00da\u00db\7n\2\2\u00db\u00dc")
        buf.write("\7u\2\2\u00dc\u00de\7g\2\2\u00dd\u00d4\3\2\2\2\u00dd\u00d8")
        buf.write("\3\2\2\2\u00de\64\3\2\2\2\u00df\u00e0\13\2\2\2\u00e0\66")
        buf.write("\3\2\2\2\u00e1\u00e2\13\2\2\2\u00e28\3\2\2\2\u00e3\u00e4")
        buf.write("\13\2\2\2\u00e4:\3\2\2\2\31\2y\u0088\u008b\u008d\u0093")
        buf.write("\u0096\u009b\u009e\u00a3\u00a9\u00ad\u00b2\u00b4\u00b7")
        buf.write("\u00bc\u00c0\u00c5\u00c9\u00ce\u00d0\u00d2\u00dd\3\b\2")
        buf.write("\2")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    INTTYPE = 2
    VOIDTYPE = 3
    REALTYPE = 4
    BOOLEANTYPE = 5
    STRINGTYPE = 6
    ARRAYTYPE = 7
    LB = 8
    RB = 9
    LP = 10
    RP = 11
    SEMI = 12
    CM = 13
    EQ = 14
    COL = 15
    DD = 16
    WS = 17
    AND = 18
    ID = 19
    INTLIT = 20
    REALLIT = 21
    BOOLLIT = 22
    ERROR_CHAR = 23
    UNCLOSE_STRING = 24
    ILLEGAL_ESCAPE = 25

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'int'", "'void'", "'real'", "'boolean'", "'string'", 
            "'array'", "'('", "')'", "'{'", "'}'", "';'", "','", "'='", 
            "':'", "'..'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "VOIDTYPE", "REALTYPE", "BOOLEANTYPE", "STRINGTYPE", 
            "ARRAYTYPE", "LB", "RB", "LP", "RP", "SEMI", "CM", "EQ", "COL", 
            "DD", "WS", "AND", "ID", "INTLIT", "REALLIT", "BOOLLIT", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "INTTYPE", "VOIDTYPE", "REALTYPE", "BOOLEANTYPE", 
                  "STRINGTYPE", "ARRAYTYPE", "LB", "RB", "LP", "RP", "SEMI", 
                  "CM", "EQ", "COL", "DD", "WS", "AND", "A", "N", "D", "ID", 
                  "INTLIT", "REALLIT", "BOOLLIT", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


