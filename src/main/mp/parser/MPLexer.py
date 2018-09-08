# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\31")
        buf.write("\u00cb\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3")
        buf.write("\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\21\6\21h\n\21\r\21\16\21i\3\21\3\21\3\22\5\22")
        buf.write("o\n\22\3\22\7\22r\n\22\f\22\16\22u\13\22\3\23\6\23x\n")
        buf.write("\23\r\23\16\23y\3\24\5\24}\n\24\3\24\6\24\u0080\n\24\r")
        buf.write("\24\16\24\u0081\3\24\5\24\u0085\n\24\3\24\7\24\u0088\n")
        buf.write("\24\f\24\16\24\u008b\13\24\3\24\6\24\u008e\n\24\r\24\16")
        buf.write("\24\u008f\3\24\3\24\5\24\u0094\n\24\3\24\6\24\u0097\n")
        buf.write("\24\r\24\16\24\u0098\5\24\u009b\n\24\3\24\5\24\u009e\n")
        buf.write("\24\3\24\7\24\u00a1\n\24\f\24\16\24\u00a4\13\24\3\24\5")
        buf.write("\24\u00a7\n\24\3\24\6\24\u00aa\n\24\r\24\16\24\u00ab\3")
        buf.write("\24\3\24\5\24\u00b0\n\24\3\24\6\24\u00b3\n\24\r\24\16")
        buf.write("\24\u00b4\5\24\u00b7\n\24\5\24\u00b9\n\24\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u00c4\n\25\3\26")
        buf.write("\3\26\3\27\3\27\3\30\3\30\2\2\31\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21")
        buf.write("!\22#\23%\24\'\25)\26+\27-\30/\31\3\2\b\5\2\13\f\17\17")
        buf.write("\"\"\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\4\2--//\4\2GGg")
        buf.write("g\2\u00de\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write("\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#")
        buf.write("\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\3\61\3\2\2\2\5\66\3\2\2\2\7:\3")
        buf.write("\2\2\2\t?\3\2\2\2\13D\3\2\2\2\rL\3\2\2\2\17S\3\2\2\2\21")
        buf.write("U\3\2\2\2\23W\3\2\2\2\25Y\3\2\2\2\27[\3\2\2\2\31]\3\2")
        buf.write("\2\2\33_\3\2\2\2\35a\3\2\2\2\37c\3\2\2\2!g\3\2\2\2#n\3")
        buf.write("\2\2\2%w\3\2\2\2\'\u00b8\3\2\2\2)\u00c3\3\2\2\2+\u00c5")
        buf.write("\3\2\2\2-\u00c7\3\2\2\2/\u00c9\3\2\2\2\61\62\7o\2\2\62")
        buf.write("\63\7c\2\2\63\64\7k\2\2\64\65\7p\2\2\65\4\3\2\2\2\66\67")
        buf.write("\7k\2\2\678\7p\2\289\7v\2\29\6\3\2\2\2:;\7x\2\2;<\7q\2")
        buf.write("\2<=\7k\2\2=>\7f\2\2>\b\3\2\2\2?@\7t\2\2@A\7g\2\2AB\7")
        buf.write("c\2\2BC\7n\2\2C\n\3\2\2\2DE\7d\2\2EF\7q\2\2FG\7q\2\2G")
        buf.write("H\7n\2\2HI\7g\2\2IJ\7c\2\2JK\7p\2\2K\f\3\2\2\2LM\7u\2")
        buf.write("\2MN\7v\2\2NO\7t\2\2OP\7k\2\2PQ\7p\2\2QR\7i\2\2R\16\3")
        buf.write("\2\2\2ST\7*\2\2T\20\3\2\2\2UV\7+\2\2V\22\3\2\2\2WX\7}")
        buf.write("\2\2X\24\3\2\2\2YZ\7\177\2\2Z\26\3\2\2\2[\\\7=\2\2\\\30")
        buf.write("\3\2\2\2]^\7.\2\2^\32\3\2\2\2_`\7?\2\2`\34\3\2\2\2ab\7")
        buf.write("<\2\2b\36\3\2\2\2cd\7\60\2\2de\7\60\2\2e \3\2\2\2fh\t")
        buf.write("\2\2\2gf\3\2\2\2hi\3\2\2\2ig\3\2\2\2ij\3\2\2\2jk\3\2\2")
        buf.write("\2kl\b\21\2\2l\"\3\2\2\2mo\t\3\2\2nm\3\2\2\2os\3\2\2\2")
        buf.write("pr\t\4\2\2qp\3\2\2\2ru\3\2\2\2sq\3\2\2\2st\3\2\2\2t$\3")
        buf.write("\2\2\2us\3\2\2\2vx\t\5\2\2wv\3\2\2\2xy\3\2\2\2yw\3\2\2")
        buf.write("\2yz\3\2\2\2z&\3\2\2\2{}\t\6\2\2|{\3\2\2\2|}\3\2\2\2}")
        buf.write("\177\3\2\2\2~\u0080\t\5\2\2\177~\3\2\2\2\u0080\u0081\3")
        buf.write("\2\2\2\u0081\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0084")
        buf.write("\3\2\2\2\u0083\u0085\7\60\2\2\u0084\u0083\3\2\2\2\u0084")
        buf.write("\u0085\3\2\2\2\u0085\u0089\3\2\2\2\u0086\u0088\t\5\2\2")
        buf.write("\u0087\u0086\3\2\2\2\u0088\u008b\3\2\2\2\u0089\u0087\3")
        buf.write("\2\2\2\u0089\u008a\3\2\2\2\u008a\u009a\3\2\2\2\u008b\u0089")
        buf.write("\3\2\2\2\u008c\u008e\t\5\2\2\u008d\u008c\3\2\2\2\u008e")
        buf.write("\u008f\3\2\2\2\u008f\u008d\3\2\2\2\u008f\u0090\3\2\2\2")
        buf.write("\u0090\u0091\3\2\2\2\u0091\u0093\t\7\2\2\u0092\u0094\7")
        buf.write("/\2\2\u0093\u0092\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u0096")
        buf.write("\3\2\2\2\u0095\u0097\t\5\2\2\u0096\u0095\3\2\2\2\u0097")
        buf.write("\u0098\3\2\2\2\u0098\u0096\3\2\2\2\u0098\u0099\3\2\2\2")
        buf.write("\u0099\u009b\3\2\2\2\u009a\u008d\3\2\2\2\u009a\u009b\3")
        buf.write("\2\2\2\u009b\u00b9\3\2\2\2\u009c\u009e\t\6\2\2\u009d\u009c")
        buf.write("\3\2\2\2\u009d\u009e\3\2\2\2\u009e\u00a2\3\2\2\2\u009f")
        buf.write("\u00a1\t\5\2\2\u00a0\u009f\3\2\2\2\u00a1\u00a4\3\2\2\2")
        buf.write("\u00a2\u00a0\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a6\3")
        buf.write("\2\2\2\u00a4\u00a2\3\2\2\2\u00a5\u00a7\7\60\2\2\u00a6")
        buf.write("\u00a5\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a9\3\2\2\2")
        buf.write("\u00a8\u00aa\t\5\2\2\u00a9\u00a8\3\2\2\2\u00aa\u00ab\3")
        buf.write("\2\2\2\u00ab\u00a9\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00b6")
        buf.write("\3\2\2\2\u00ad\u00af\t\7\2\2\u00ae\u00b0\7/\2\2\u00af")
        buf.write("\u00ae\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b2\3\2\2\2")
        buf.write("\u00b1\u00b3\t\5\2\2\u00b2\u00b1\3\2\2\2\u00b3\u00b4\3")
        buf.write("\2\2\2\u00b4\u00b2\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b7")
        buf.write("\3\2\2\2\u00b6\u00ad\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7")
        buf.write("\u00b9\3\2\2\2\u00b8|\3\2\2\2\u00b8\u009d\3\2\2\2\u00b9")
        buf.write("(\3\2\2\2\u00ba\u00bb\7v\2\2\u00bb\u00bc\7t\2\2\u00bc")
        buf.write("\u00bd\7w\2\2\u00bd\u00c4\7g\2\2\u00be\u00bf\7h\2\2\u00bf")
        buf.write("\u00c0\7c\2\2\u00c0\u00c1\7n\2\2\u00c1\u00c2\7u\2\2\u00c2")
        buf.write("\u00c4\7g\2\2\u00c3\u00ba\3\2\2\2\u00c3\u00be\3\2\2\2")
        buf.write("\u00c4*\3\2\2\2\u00c5\u00c6\13\2\2\2\u00c6,\3\2\2\2\u00c7")
        buf.write("\u00c8\13\2\2\2\u00c8.\3\2\2\2\u00c9\u00ca\13\2\2\2\u00ca")
        buf.write("\60\3\2\2\2\31\2inqsy|\u0081\u0084\u0089\u008f\u0093\u0098")
        buf.write("\u009a\u009d\u00a2\u00a6\u00ab\u00af\u00b4\u00b6\u00b8")
        buf.write("\u00c3\3\b\2\2")
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
    LB = 7
    RB = 8
    LP = 9
    RP = 10
    SEMI = 11
    CM = 12
    EQ = 13
    COL = 14
    DD = 15
    WS = 16
    ID = 17
    INTLIT = 18
    REALLIT = 19
    BOOLLIT = 20
    ERROR_CHAR = 21
    UNCLOSE_STRING = 22
    ILLEGAL_ESCAPE = 23

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'int'", "'void'", "'real'", "'boolean'", "'string'", 
            "'('", "')'", "'{'", "'}'", "';'", "','", "'='", "':'", "'..'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "VOIDTYPE", "REALTYPE", "BOOLEANTYPE", "STRINGTYPE", 
            "LB", "RB", "LP", "RP", "SEMI", "CM", "EQ", "COL", "DD", "WS", 
            "ID", "INTLIT", "REALLIT", "BOOLLIT", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "INTTYPE", "VOIDTYPE", "REALTYPE", "BOOLEANTYPE", 
                  "STRINGTYPE", "LB", "RB", "LP", "RP", "SEMI", "CM", "EQ", 
                  "COL", "DD", "WS", "ID", "INTLIT", "REALLIT", "BOOLLIT", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


