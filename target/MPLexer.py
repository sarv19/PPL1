# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u028c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3")
        buf.write("\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3")
        buf.write("\16\3\16\3\17\3\17\3\17\3\20\3\20\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3%\3")
        buf.write("%\3%\3%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3\'\3\'\3\'\3\'")
        buf.write("\3\'\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3*\3*\3*\3+\3")
        buf.write("+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\5,\u016d")
        buf.write("\n,\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u017b\n-\3")
        buf.write(".\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3")
        buf.write("\61\3\61\3\61\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63")
        buf.write("\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3")
        buf.write(":\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3")
        buf.write("C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3J\3J\3K\3K\3")
        buf.write("L\3L\3M\3M\3N\3N\3O\6O\u01ce\nO\rO\16O\u01cf\3P\5P\u01d3")
        buf.write("\nP\3P\7P\u01d6\nP\fP\16P\u01d9\13P\3Q\6Q\u01dc\nQ\rQ")
        buf.write("\16Q\u01dd\3R\6R\u01e1\nR\rR\16R\u01e2\3R\5R\u01e6\nR")
        buf.write("\3R\7R\u01e9\nR\fR\16R\u01ec\13R\3R\6R\u01ef\nR\rR\16")
        buf.write("R\u01f0\3R\3R\5R\u01f5\nR\3R\6R\u01f8\nR\rR\16R\u01f9")
        buf.write("\5R\u01fc\nR\3R\7R\u01ff\nR\fR\16R\u0202\13R\3R\5R\u0205")
        buf.write("\nR\3R\6R\u0208\nR\rR\16R\u0209\3R\3R\5R\u020e\nR\3R\6")
        buf.write("R\u0211\nR\rR\16R\u0212\5R\u0215\nR\5R\u0217\nR\3S\3S")
        buf.write("\3S\3S\3S\3S\3S\3S\3S\5S\u0222\nS\3T\3T\3T\3T\7T\u0228")
        buf.write("\nT\fT\16T\u022b\13T\3T\3T\3U\3U\3U\3U\3U\5U\u0234\nU")
        buf.write("\3V\3V\5V\u0238\nV\3W\3W\5W\u023c\nW\3X\3X\3X\3X\7X\u0242")
        buf.write("\nX\fX\16X\u0245\13X\3X\3X\3X\3X\3X\3Y\3Y\7Y\u024e\nY")
        buf.write("\fY\16Y\u0251\13Y\3Y\3Y\3Y\3Y\3Z\3Z\3Z\3Z\7Z\u025b\nZ")
        buf.write("\fZ\16Z\u025e\13Z\3[\3[\3\\\3\\\3\\\3\\\3\\\7\\\u0267")
        buf.write("\n\\\f\\\16\\\u026a\13\\\3]\3]\3]\3]\3]\7]\u0271\n]\f")
        buf.write("]\16]\u0274\13]\3]\6]\u0277\n]\r]\16]\u0278\3]\3]\3]\7")
        buf.write("]\u027e\n]\f]\16]\u0281\13]\3]\5]\u0284\n]\3^\6^\u0287")
        buf.write("\n^\r^\16^\u0288\3^\3^\4\u0243\u024f\2_\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60")
        buf.write("_\61a\62c\63e\64g\2i\2k\2m\2o\2q\2s\2u\2w\2y\2{\2}\2\177")
        buf.write("\2\u0081\2\u0083\2\u0085\2\u0087\2\u0089\2\u008b\2\u008d")
        buf.write("\2\u008f\2\u0091\2\u0093\2\u0095\2\u0097\2\u0099\2\u009b")
        buf.write("\2\u009d\65\u009f\66\u00a1\67\u00a38\u00a59\u00a7:\u00a9")
        buf.write(";\u00ab<\u00ad=\u00af>\u00b1?\u00b3@\u00b5A\u00b7B\u00b9")
        buf.write("C\u00bbD\3\2$\4\2CCcc\4\2DDdd\4\2EEee\4\2FFff\4\2GGgg")
        buf.write("\4\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4\2LLll\4\2MMmm\4\2N")
        buf.write("Nnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2SSss\4\2TTtt\4")
        buf.write("\2UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4\2ZZzz\4\2[[{")
        buf.write("{\4\2\\\\||\3\2\62;\5\2C\\aac|\6\2\62;C\\aac|\n\2$$))")
        buf.write("^^ddhhppttvv\7\2\n\f\16\17$$))^^\4\2\f\f\17\17\7\2\13")
        buf.write("\f\16\17$$))^^\5\2\13\f\17\17\"\"\2\u0298\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'")
        buf.write("\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2")
        buf.write("\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29")
        buf.write("\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write("C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2")
        buf.write("\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2")
        buf.write("\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2")
        buf.write("\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2\u009d\3\2\2\2")
        buf.write("\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5")
        buf.write("\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2")
        buf.write("\2\2\u00ad\3\2\2\2\2\u00af\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3")
        buf.write("\3\2\2\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2\2\2\u00b9\3\2\2")
        buf.write("\2\2\u00bb\3\2\2\2\3\u00bd\3\2\2\2\5\u00bf\3\2\2\2\7\u00c1")
        buf.write("\3\2\2\2\t\u00c3\3\2\2\2\13\u00c5\3\2\2\2\r\u00c7\3\2")
        buf.write("\2\2\17\u00c9\3\2\2\2\21\u00cb\3\2\2\2\23\u00cd\3\2\2")
        buf.write("\2\25\u00cf\3\2\2\2\27\u00d1\3\2\2\2\31\u00d4\3\2\2\2")
        buf.write("\33\u00d6\3\2\2\2\35\u00d8\3\2\2\2\37\u00db\3\2\2\2!\u00dd")
        buf.write("\3\2\2\2#\u00e0\3\2\2\2%\u00e2\3\2\2\2\'\u00e4\3\2\2\2")
        buf.write(")\u00e6\3\2\2\2+\u00e9\3\2\2\2-\u00eb\3\2\2\2/\u00f1\3")
        buf.write("\2\2\2\61\u00fa\3\2\2\2\63\u00fe\3\2\2\2\65\u0101\3\2")
        buf.write("\2\2\67\u0108\3\2\2\29\u010b\3\2\2\2;\u010e\3\2\2\2=\u0113")
        buf.write("\3\2\2\2?\u0118\3\2\2\2A\u011f\3\2\2\2C\u0125\3\2\2\2")
        buf.write("E\u012b\3\2\2\2G\u012f\3\2\2\2I\u0138\3\2\2\2K\u0142\3")
        buf.write("\2\2\2M\u0146\3\2\2\2O\u014b\3\2\2\2Q\u0151\3\2\2\2S\u0157")
        buf.write("\3\2\2\2U\u015a\3\2\2\2W\u016c\3\2\2\2Y\u017a\3\2\2\2")
        buf.write("[\u017c\3\2\2\2]\u0183\3\2\2\2_\u0187\3\2\2\2a\u018b\3")
        buf.write("\2\2\2c\u018e\3\2\2\2e\u0192\3\2\2\2g\u0196\3\2\2\2i\u0198")
        buf.write("\3\2\2\2k\u019a\3\2\2\2m\u019c\3\2\2\2o\u019e\3\2\2\2")
        buf.write("q\u01a0\3\2\2\2s\u01a2\3\2\2\2u\u01a4\3\2\2\2w\u01a6\3")
        buf.write("\2\2\2y\u01a8\3\2\2\2{\u01aa\3\2\2\2}\u01ac\3\2\2\2\177")
        buf.write("\u01ae\3\2\2\2\u0081\u01b0\3\2\2\2\u0083\u01b2\3\2\2\2")
        buf.write("\u0085\u01b4\3\2\2\2\u0087\u01b6\3\2\2\2\u0089\u01b8\3")
        buf.write("\2\2\2\u008b\u01ba\3\2\2\2\u008d\u01bc\3\2\2\2\u008f\u01be")
        buf.write("\3\2\2\2\u0091\u01c0\3\2\2\2\u0093\u01c2\3\2\2\2\u0095")
        buf.write("\u01c4\3\2\2\2\u0097\u01c6\3\2\2\2\u0099\u01c8\3\2\2\2")
        buf.write("\u009b\u01ca\3\2\2\2\u009d\u01cd\3\2\2\2\u009f\u01d2\3")
        buf.write("\2\2\2\u00a1\u01db\3\2\2\2\u00a3\u0216\3\2\2\2\u00a5\u0221")
        buf.write("\3\2\2\2\u00a7\u0223\3\2\2\2\u00a9\u0233\3\2\2\2\u00ab")
        buf.write("\u0237\3\2\2\2\u00ad\u023b\3\2\2\2\u00af\u023d\3\2\2\2")
        buf.write("\u00b1\u024b\3\2\2\2\u00b3\u0256\3\2\2\2\u00b5\u025f\3")
        buf.write("\2\2\2\u00b7\u0261\3\2\2\2\u00b9\u026b\3\2\2\2\u00bb\u0286")
        buf.write("\3\2\2\2\u00bd\u00be\7*\2\2\u00be\4\3\2\2\2\u00bf\u00c0")
        buf.write("\7+\2\2\u00c0\6\3\2\2\2\u00c1\u00c2\7}\2\2\u00c2\b\3\2")
        buf.write("\2\2\u00c3\u00c4\7\177\2\2\u00c4\n\3\2\2\2\u00c5\u00c6")
        buf.write("\7]\2\2\u00c6\f\3\2\2\2\u00c7\u00c8\7_\2\2\u00c8\16\3")
        buf.write("\2\2\2\u00c9\u00ca\7=\2\2\u00ca\20\3\2\2\2\u00cb\u00cc")
        buf.write("\7.\2\2\u00cc\22\3\2\2\2\u00cd\u00ce\7?\2\2\u00ce\24\3")
        buf.write("\2\2\2\u00cf\u00d0\7<\2\2\u00d0\26\3\2\2\2\u00d1\u00d2")
        buf.write("\7\60\2\2\u00d2\u00d3\7\60\2\2\u00d3\30\3\2\2\2\u00d4")
        buf.write("\u00d5\7-\2\2\u00d5\32\3\2\2\2\u00d6\u00d7\7,\2\2\u00d7")
        buf.write("\34\3\2\2\2\u00d8\u00d9\7>\2\2\u00d9\u00da\7@\2\2\u00da")
        buf.write("\36\3\2\2\2\u00db\u00dc\7>\2\2\u00dc \3\2\2\2\u00dd\u00de")
        buf.write("\7>\2\2\u00de\u00df\7?\2\2\u00df\"\3\2\2\2\u00e0\u00e1")
        buf.write("\7/\2\2\u00e1$\3\2\2\2\u00e2\u00e3\7\61\2\2\u00e3&\3\2")
        buf.write("\2\2\u00e4\u00e5\7@\2\2\u00e5(\3\2\2\2\u00e6\u00e7\7@")
        buf.write("\2\2\u00e7\u00e8\7?\2\2\u00e8*\3\2\2\2\u00e9\u00ea\7\"")
        buf.write("\2\2\u00ea,\3\2\2\2\u00eb\u00ec\5i\65\2\u00ec\u00ed\5")
        buf.write("\u0089E\2\u00ed\u00ee\5o8\2\u00ee\u00ef\5g\64\2\u00ef")
        buf.write("\u00f0\5{>\2\u00f0.\3\2\2\2\u00f1\u00f2\5k\66\2\u00f2")
        buf.write("\u00f3\5\u0083B\2\u00f3\u00f4\5\u0081A\2\u00f4\u00f5\5")
        buf.write("\u008dG\2\u00f5\u00f6\5w<\2\u00f6\u00f7\5\u0081A\2\u00f7")
        buf.write("\u00f8\5\u008fH\2\u00f8\u00f9\5o8\2\u00f9\60\3\2\2\2\u00fa")
        buf.write("\u00fb\5q9\2\u00fb\u00fc\5\u0083B\2\u00fc\u00fd\5\u0089")
        buf.write("E\2\u00fd\62\3\2\2\2\u00fe\u00ff\5\u008dG\2\u00ff\u0100")
        buf.write("\5\u0083B\2\u0100\64\3\2\2\2\u0101\u0102\5m\67\2\u0102")
        buf.write("\u0103\5\u0083B\2\u0103\u0104\5\u0093J\2\u0104\u0105\5")
        buf.write("\u0081A\2\u0105\u0106\5\u008dG\2\u0106\u0107\5\u0083B")
        buf.write("\2\u0107\66\3\2\2\2\u0108\u0109\5m\67\2\u0109\u010a\5")
        buf.write("\u0083B\2\u010a8\3\2\2\2\u010b\u010c\5w<\2\u010c\u010d")
        buf.write("\5q9\2\u010d:\3\2\2\2\u010e\u010f\5\u008dG\2\u010f\u0110")
        buf.write("\5u;\2\u0110\u0111\5o8\2\u0111\u0112\5\u0081A\2\u0112")
        buf.write("<\3\2\2\2\u0113\u0114\5o8\2\u0114\u0115\5}?\2\u0115\u0116")
        buf.write("\5\u008bF\2\u0116\u0117\5o8\2\u0117>\3\2\2\2\u0118\u0119")
        buf.write("\5\u0089E\2\u0119\u011a\5o8\2\u011a\u011b\5\u008dG\2\u011b")
        buf.write("\u011c\5\u008fH\2\u011c\u011d\5\u0089E\2\u011d\u011e\5")
        buf.write("\u0081A\2\u011e@\3\2\2\2\u011f\u0120\5\u0093J\2\u0120")
        buf.write("\u0121\5u;\2\u0121\u0122\5w<\2\u0122\u0123\5}?\2\u0123")
        buf.write("\u0124\5o8\2\u0124B\3\2\2\2\u0125\u0126\5i\65\2\u0126")
        buf.write("\u0127\5o8\2\u0127\u0128\5s:\2\u0128\u0129\5w<\2\u0129")
        buf.write("\u012a\5\u0081A\2\u012aD\3\2\2\2\u012b\u012c\5o8\2\u012c")
        buf.write("\u012d\5\u0081A\2\u012d\u012e\5m\67\2\u012eF\3\2\2\2\u012f")
        buf.write("\u0130\5q9\2\u0130\u0131\5\u008fH\2\u0131\u0132\5k\66")
        buf.write("\2\u0132\u0133\5\u0081A\2\u0133\u0134\5\u008dG\2\u0134")
        buf.write("\u0135\5w<\2\u0135\u0136\5\u0083B\2\u0136\u0137\5\u0081")
        buf.write("A\2\u0137H\3\2\2\2\u0138\u0139\5\u0085C\2\u0139\u013a")
        buf.write("\5\u0089E\2\u013a\u013b\5\u0083B\2\u013b\u013c\5k\66\2")
        buf.write("\u013c\u013d\5o8\2\u013d\u013e\5m\67\2\u013e\u013f\5\u008f")
        buf.write("H\2\u013f\u0140\5\u0089E\2\u0140\u0141\5o8\2\u0141J\3")
        buf.write("\2\2\2\u0142\u0143\5\u0091I\2\u0143\u0144\5g\64\2\u0144")
        buf.write("\u0145\5\u0089E\2\u0145L\3\2\2\2\u0146\u0147\5\u008dG")
        buf.write("\2\u0147\u0148\5\u0089E\2\u0148\u0149\5\u008fH\2\u0149")
        buf.write("\u014a\5o8\2\u014aN\3\2\2\2\u014b\u014c\5q9\2\u014c\u014d")
        buf.write("\5g\64\2\u014d\u014e\5}?\2\u014e\u014f\5\u008bF\2\u014f")
        buf.write("\u0150\5o8\2\u0150P\3\2\2\2\u0151\u0152\5g\64\2\u0152")
        buf.write("\u0153\5\u0089E\2\u0153\u0154\5\u0089E\2\u0154\u0155\5")
        buf.write("g\64\2\u0155\u0156\5\u0097L\2\u0156R\3\2\2\2\u0157\u0158")
        buf.write("\5\u0083B\2\u0158\u0159\5q9\2\u0159T\3\2\2\2\u015a\u015b")
        buf.write("\5\u0089E\2\u015b\u015c\5o8\2\u015c\u015d\5g\64\2\u015d")
        buf.write("\u015e\5}?\2\u015eV\3\2\2\2\u015f\u0160\5i\65\2\u0160")
        buf.write("\u0161\5\u0083B\2\u0161\u0162\5\u0083B\2\u0162\u0163\5")
        buf.write("}?\2\u0163\u0164\5o8\2\u0164\u0165\5g\64\2\u0165\u0166")
        buf.write("\5\u0081A\2\u0166\u016d\3\2\2\2\u0167\u0168\5i\65\2\u0168")
        buf.write("\u0169\5\u0083B\2\u0169\u016a\5\u0083B\2\u016a\u016b\5")
        buf.write("}?\2\u016b\u016d\3\2\2\2\u016c\u015f\3\2\2\2\u016c\u0167")
        buf.write("\3\2\2\2\u016dX\3\2\2\2\u016e\u016f\5w<\2\u016f\u0170")
        buf.write("\5\u0081A\2\u0170\u0171\5\u008dG\2\u0171\u0172\5o8\2\u0172")
        buf.write("\u0173\5s:\2\u0173\u0174\5o8\2\u0174\u0175\5\u0089E\2")
        buf.write("\u0175\u017b\3\2\2\2\u0176\u0177\5w<\2\u0177\u0178\5\u0081")
        buf.write("A\2\u0178\u0179\5\u008dG\2\u0179\u017b\3\2\2\2\u017a\u016e")
        buf.write("\3\2\2\2\u017a\u0176\3\2\2\2\u017bZ\3\2\2\2\u017c\u017d")
        buf.write("\5\u008bF\2\u017d\u017e\5\u008dG\2\u017e\u017f\5\u0089")
        buf.write("E\2\u017f\u0180\5w<\2\u0180\u0181\5\u0081A\2\u0181\u0182")
        buf.write("\5s:\2\u0182\\\3\2\2\2\u0183\u0184\5\u0081A\2\u0184\u0185")
        buf.write("\5\u0083B\2\u0185\u0186\5\u008dG\2\u0186^\3\2\2\2\u0187")
        buf.write("\u0188\5g\64\2\u0188\u0189\5\u0081A\2\u0189\u018a\5m\67")
        buf.write("\2\u018a`\3\2\2\2\u018b\u018c\5\u0083B\2\u018c\u018d\5")
        buf.write("\u0089E\2\u018db\3\2\2\2\u018e\u018f\5m\67\2\u018f\u0190")
        buf.write("\5w<\2\u0190\u0191\5\u0091I\2\u0191d\3\2\2\2\u0192\u0193")
        buf.write("\5\177@\2\u0193\u0194\5\u0083B\2\u0194\u0195\5m\67\2\u0195")
        buf.write("f\3\2\2\2\u0196\u0197\t\2\2\2\u0197h\3\2\2\2\u0198\u0199")
        buf.write("\t\3\2\2\u0199j\3\2\2\2\u019a\u019b\t\4\2\2\u019bl\3\2")
        buf.write("\2\2\u019c\u019d\t\5\2\2\u019dn\3\2\2\2\u019e\u019f\t")
        buf.write("\6\2\2\u019fp\3\2\2\2\u01a0\u01a1\t\7\2\2\u01a1r\3\2\2")
        buf.write("\2\u01a2\u01a3\t\b\2\2\u01a3t\3\2\2\2\u01a4\u01a5\t\t")
        buf.write("\2\2\u01a5v\3\2\2\2\u01a6\u01a7\t\n\2\2\u01a7x\3\2\2\2")
        buf.write("\u01a8\u01a9\t\13\2\2\u01a9z\3\2\2\2\u01aa\u01ab\t\f\2")
        buf.write("\2\u01ab|\3\2\2\2\u01ac\u01ad\t\r\2\2\u01ad~\3\2\2\2\u01ae")
        buf.write("\u01af\t\16\2\2\u01af\u0080\3\2\2\2\u01b0\u01b1\t\17\2")
        buf.write("\2\u01b1\u0082\3\2\2\2\u01b2\u01b3\t\20\2\2\u01b3\u0084")
        buf.write("\3\2\2\2\u01b4\u01b5\t\21\2\2\u01b5\u0086\3\2\2\2\u01b6")
        buf.write("\u01b7\t\22\2\2\u01b7\u0088\3\2\2\2\u01b8\u01b9\t\23\2")
        buf.write("\2\u01b9\u008a\3\2\2\2\u01ba\u01bb\t\24\2\2\u01bb\u008c")
        buf.write("\3\2\2\2\u01bc\u01bd\t\25\2\2\u01bd\u008e\3\2\2\2\u01be")
        buf.write("\u01bf\t\26\2\2\u01bf\u0090\3\2\2\2\u01c0\u01c1\t\27\2")
        buf.write("\2\u01c1\u0092\3\2\2\2\u01c2\u01c3\t\30\2\2\u01c3\u0094")
        buf.write("\3\2\2\2\u01c4\u01c5\t\31\2\2\u01c5\u0096\3\2\2\2\u01c6")
        buf.write("\u01c7\t\32\2\2\u01c7\u0098\3\2\2\2\u01c8\u01c9\t\33\2")
        buf.write("\2\u01c9\u009a\3\2\2\2\u01ca\u01cb\t\34\2\2\u01cb\u009c")
        buf.write("\3\2\2\2\u01cc\u01ce\5\u009bN\2\u01cd\u01cc\3\2\2\2\u01ce")
        buf.write("\u01cf\3\2\2\2\u01cf\u01cd\3\2\2\2\u01cf\u01d0\3\2\2\2")
        buf.write("\u01d0\u009e\3\2\2\2\u01d1\u01d3\t\35\2\2\u01d2\u01d1")
        buf.write("\3\2\2\2\u01d3\u01d7\3\2\2\2\u01d4\u01d6\t\36\2\2\u01d5")
        buf.write("\u01d4\3\2\2\2\u01d6\u01d9\3\2\2\2\u01d7\u01d5\3\2\2\2")
        buf.write("\u01d7\u01d8\3\2\2\2\u01d8\u00a0\3\2\2\2\u01d9\u01d7\3")
        buf.write("\2\2\2\u01da\u01dc\t\34\2\2\u01db\u01da\3\2\2\2\u01dc")
        buf.write("\u01dd\3\2\2\2\u01dd\u01db\3\2\2\2\u01dd\u01de\3\2\2\2")
        buf.write("\u01de\u00a2\3\2\2\2\u01df\u01e1\t\34\2\2\u01e0\u01df")
        buf.write("\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e2")
        buf.write("\u01e3\3\2\2\2\u01e3\u01e5\3\2\2\2\u01e4\u01e6\7\60\2")
        buf.write("\2\u01e5\u01e4\3\2\2\2\u01e5\u01e6\3\2\2\2\u01e6\u01ea")
        buf.write("\3\2\2\2\u01e7\u01e9\t\34\2\2\u01e8\u01e7\3\2\2\2\u01e9")
        buf.write("\u01ec\3\2\2\2\u01ea\u01e8\3\2\2\2\u01ea\u01eb\3\2\2\2")
        buf.write("\u01eb\u01fb\3\2\2\2\u01ec\u01ea\3\2\2\2\u01ed\u01ef\t")
        buf.write("\34\2\2\u01ee\u01ed\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0")
        buf.write("\u01ee\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1\u01f2\3\2\2\2")
        buf.write("\u01f2\u01f4\t\6\2\2\u01f3\u01f5\7/\2\2\u01f4\u01f3\3")
        buf.write("\2\2\2\u01f4\u01f5\3\2\2\2\u01f5\u01f7\3\2\2\2\u01f6\u01f8")
        buf.write("\t\34\2\2\u01f7\u01f6\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9")
        buf.write("\u01f7\3\2\2\2\u01f9\u01fa\3\2\2\2\u01fa\u01fc\3\2\2\2")
        buf.write("\u01fb\u01ee\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc\u0217\3")
        buf.write("\2\2\2\u01fd\u01ff\t\34\2\2\u01fe\u01fd\3\2\2\2\u01ff")
        buf.write("\u0202\3\2\2\2\u0200\u01fe\3\2\2\2\u0200\u0201\3\2\2\2")
        buf.write("\u0201\u0204\3\2\2\2\u0202\u0200\3\2\2\2\u0203\u0205\7")
        buf.write("\60\2\2\u0204\u0203\3\2\2\2\u0204\u0205\3\2\2\2\u0205")
        buf.write("\u0207\3\2\2\2\u0206\u0208\t\34\2\2\u0207\u0206\3\2\2")
        buf.write("\2\u0208\u0209\3\2\2\2\u0209\u0207\3\2\2\2\u0209\u020a")
        buf.write("\3\2\2\2\u020a\u0214\3\2\2\2\u020b\u020d\t\6\2\2\u020c")
        buf.write("\u020e\7/\2\2\u020d\u020c\3\2\2\2\u020d\u020e\3\2\2\2")
        buf.write("\u020e\u0210\3\2\2\2\u020f\u0211\t\34\2\2\u0210\u020f")
        buf.write("\3\2\2\2\u0211\u0212\3\2\2\2\u0212\u0210\3\2\2\2\u0212")
        buf.write("\u0213\3\2\2\2\u0213\u0215\3\2\2\2\u0214\u020b\3\2\2\2")
        buf.write("\u0214\u0215\3\2\2\2\u0215\u0217\3\2\2\2\u0216\u01e0\3")
        buf.write("\2\2\2\u0216\u0200\3\2\2\2\u0217\u00a4\3\2\2\2\u0218\u0219")
        buf.write("\7v\2\2\u0219\u021a\7t\2\2\u021a\u021b\7w\2\2\u021b\u0222")
        buf.write("\7g\2\2\u021c\u021d\7h\2\2\u021d\u021e\7c\2\2\u021e\u021f")
        buf.write("\7n\2\2\u021f\u0220\7u\2\2\u0220\u0222\7g\2\2\u0221\u0218")
        buf.write("\3\2\2\2\u0221\u021c\3\2\2\2\u0222\u00a6\3\2\2\2\u0223")
        buf.write("\u0229\7$\2\2\u0224\u0225\7^\2\2\u0225\u0228\t\37\2\2")
        buf.write("\u0226\u0228\n \2\2\u0227\u0224\3\2\2\2\u0227\u0226\3")
        buf.write("\2\2\2\u0228\u022b\3\2\2\2\u0229\u0227\3\2\2\2\u0229\u022a")
        buf.write("\3\2\2\2\u022a\u022c\3\2\2\2\u022b\u0229\3\2\2\2\u022c")
        buf.write("\u022d\7$\2\2\u022d\u00a8\3\2\2\2\u022e\u0234\5W,\2\u022f")
        buf.write("\u0234\5Y-\2\u0230\u0234\5U+\2\u0231\u0234\5[.\2\u0232")
        buf.write("\u0234\5Q)\2\u0233\u022e\3\2\2\2\u0233\u022f\3\2\2\2\u0233")
        buf.write("\u0230\3\2\2\2\u0233\u0231\3\2\2\2\u0233\u0232\3\2\2\2")
        buf.write("\u0234\u00aa\3\2\2\2\u0235\u0238\5\u00adW\2\u0236\u0238")
        buf.write("\5\u00b3Z\2\u0237\u0235\3\2\2\2\u0237\u0236\3\2\2\2\u0238")
        buf.write("\u00ac\3\2\2\2\u0239\u023c\5\u00afX\2\u023a\u023c\5\u00b1")
        buf.write("Y\2\u023b\u0239\3\2\2\2\u023b\u023a\3\2\2\2\u023c\u00ae")
        buf.write("\3\2\2\2\u023d\u023e\7*\2\2\u023e\u023f\7,\2\2\u023f\u0243")
        buf.write("\3\2\2\2\u0240\u0242\13\2\2\2\u0241\u0240\3\2\2\2\u0242")
        buf.write("\u0245\3\2\2\2\u0243\u0244\3\2\2\2\u0243\u0241\3\2\2\2")
        buf.write("\u0244\u0246\3\2\2\2\u0245\u0243\3\2\2\2\u0246\u0247\7")
        buf.write(",\2\2\u0247\u0248\7+\2\2\u0248\u0249\3\2\2\2\u0249\u024a")
        buf.write("\bX\2\2\u024a\u00b0\3\2\2\2\u024b\u024f\7}\2\2\u024c\u024e")
        buf.write("\13\2\2\2\u024d\u024c\3\2\2\2\u024e\u0251\3\2\2\2\u024f")
        buf.write("\u0250\3\2\2\2\u024f\u024d\3\2\2\2\u0250\u0252\3\2\2\2")
        buf.write("\u0251\u024f\3\2\2\2\u0252\u0253\7\177\2\2\u0253\u0254")
        buf.write("\3\2\2\2\u0254\u0255\bY\2\2\u0255\u00b2\3\2\2\2\u0256")
        buf.write("\u0257\7\61\2\2\u0257\u0258\7\61\2\2\u0258\u025c\3\2\2")
        buf.write("\2\u0259\u025b\n!\2\2\u025a\u0259\3\2\2\2\u025b\u025e")
        buf.write("\3\2\2\2\u025c\u025a\3\2\2\2\u025c\u025d\3\2\2\2\u025d")
        buf.write("\u00b4\3\2\2\2\u025e\u025c\3\2\2\2\u025f\u0260\13\2\2")
        buf.write("\2\u0260\u00b6\3\2\2\2\u0261\u0262\b\\\3\2\u0262\u0268")
        buf.write("\7$\2\2\u0263\u0264\7^\2\2\u0264\u0267\t\37\2\2\u0265")
        buf.write("\u0267\n\"\2\2\u0266\u0263\3\2\2\2\u0266\u0265\3\2\2\2")
        buf.write("\u0267\u026a\3\2\2\2\u0268\u0266\3\2\2\2\u0268\u0269\3")
        buf.write("\2\2\2\u0269\u00b8\3\2\2\2\u026a\u0268\3\2\2\2\u026b\u026c")
        buf.write("\b]\4\2\u026c\u0272\7$\2\2\u026d\u026e\7^\2\2\u026e\u0271")
        buf.write("\t\37\2\2\u026f\u0271\n \2\2\u0270\u026d\3\2\2\2\u0270")
        buf.write("\u026f\3\2\2\2\u0271\u0274\3\2\2\2\u0272\u0270\3\2\2\2")
        buf.write("\u0272\u0273\3\2\2\2\u0273\u0276\3\2\2\2\u0274\u0272\3")
        buf.write("\2\2\2\u0275\u0277\t\"\2\2\u0276\u0275\3\2\2\2\u0277\u0278")
        buf.write("\3\2\2\2\u0278\u0276\3\2\2\2\u0278\u0279\3\2\2\2\u0279")
        buf.write("\u027f\3\2\2\2\u027a\u027b\7^\2\2\u027b\u027e\t\37\2\2")
        buf.write("\u027c\u027e\n \2\2\u027d\u027a\3\2\2\2\u027d\u027c\3")
        buf.write("\2\2\2\u027e\u0281\3\2\2\2\u027f\u027d\3\2\2\2\u027f\u0280")
        buf.write("\3\2\2\2\u0280\u0283\3\2\2\2\u0281\u027f\3\2\2\2\u0282")
        buf.write("\u0284\7$\2\2\u0283\u0282\3\2\2\2\u0283\u0284\3\2\2\2")
        buf.write("\u0284\u00ba\3\2\2\2\u0285\u0287\t#\2\2\u0286\u0285\3")
        buf.write("\2\2\2\u0287\u0288\3\2\2\2\u0288\u0286\3\2\2\2\u0288\u0289")
        buf.write("\3\2\2\2\u0289\u028a\3\2\2\2\u028a\u028b\b^\2\2\u028b")
        buf.write("\u00bc\3\2\2\2*\2\u016c\u017a\u01cf\u01d2\u01d5\u01d7")
        buf.write("\u01dd\u01e2\u01e5\u01ea\u01f0\u01f4\u01f9\u01fb\u0200")
        buf.write("\u0204\u0209\u020d\u0212\u0214\u0216\u0221\u0227\u0229")
        buf.write("\u0233\u0237\u023b\u0243\u024f\u025c\u0266\u0268\u0270")
        buf.write("\u0272\u0278\u027d\u027f\u0283\u0288\5\b\2\2\3\\\2\3]")
        buf.write("\3")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LB = 1
    RB = 2
    LP = 3
    RP = 4
    LQ = 5
    RQ = 6
    SEMI = 7
    CM = 8
    EQ = 9
    COL = 10
    DD = 11
    ADD = 12
    MUL = 13
    NOTEQ = 14
    LESSTN = 15
    LESSEQ = 16
    SUBNE = 17
    DIVSI = 18
    GRETN = 19
    GREEQ = 20
    SP = 21
    BREAK = 22
    CONTINUE = 23
    FOR = 24
    TO = 25
    DOWNTO = 26
    DO = 27
    IF = 28
    THEN = 29
    ELSE = 30
    RETURN = 31
    WHILE = 32
    BEGIN = 33
    END = 34
    FUNCTION = 35
    PROCEDURE = 36
    VAR = 37
    TRUE = 38
    FALSE = 39
    ARRAY = 40
    OF = 41
    REAL = 42
    BOOLEAN = 43
    INTEGER = 44
    STRING = 45
    NOT = 46
    AND = 47
    OR = 48
    DIV = 49
    MOD = 50
    ManyNum = 51
    ID = 52
    INTLIT = 53
    REALLIT = 54
    BOOLLIT = 55
    STRINGLIT = 56
    TYPE = 57
    CMT = 58
    BLKCMT = 59
    TRACMT = 60
    BLCMT = 61
    LINECMT = 62
    ERROR_CHAR = 63
    UNCLOSE_STRING = 64
    ILLEGAL_ESCAPE = 65
    WS = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "','", "'='", 
            "':'", "'..'", "'+'", "'*'", "'<>'", "'<'", "'<='", "'-'", "'/'", 
            "'>'", "'>='", "' '" ]

    symbolicNames = [ "<INVALID>",
            "LB", "RB", "LP", "RP", "LQ", "RQ", "SEMI", "CM", "EQ", "COL", 
            "DD", "ADD", "MUL", "NOTEQ", "LESSTN", "LESSEQ", "SUBNE", "DIVSI", 
            "GRETN", "GREEQ", "SP", "BREAK", "CONTINUE", "FOR", "TO", "DOWNTO", 
            "DO", "IF", "THEN", "ELSE", "RETURN", "WHILE", "BEGIN", "END", 
            "FUNCTION", "PROCEDURE", "VAR", "TRUE", "FALSE", "ARRAY", "OF", 
            "REAL", "BOOLEAN", "INTEGER", "STRING", "NOT", "AND", "OR", 
            "DIV", "MOD", "ManyNum", "ID", "INTLIT", "REALLIT", "BOOLLIT", 
            "STRINGLIT", "TYPE", "CMT", "BLKCMT", "TRACMT", "BLCMT", "LINECMT", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "WS" ]

    ruleNames = [ "LB", "RB", "LP", "RP", "LQ", "RQ", "SEMI", "CM", "EQ", 
                  "COL", "DD", "ADD", "MUL", "NOTEQ", "LESSTN", "LESSEQ", 
                  "SUBNE", "DIVSI", "GRETN", "GREEQ", "SP", "BREAK", "CONTINUE", 
                  "FOR", "TO", "DOWNTO", "DO", "IF", "THEN", "ELSE", "RETURN", 
                  "WHILE", "BEGIN", "END", "FUNCTION", "PROCEDURE", "VAR", 
                  "TRUE", "FALSE", "ARRAY", "OF", "REAL", "BOOLEAN", "INTEGER", 
                  "STRING", "NOT", "AND", "OR", "DIV", "MOD", "A", "B", 
                  "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
                  "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", 
                  "Y", "Z", "NUM", "ManyNum", "ID", "INTLIT", "REALLIT", 
                  "BOOLLIT", "STRINGLIT", "TYPE", "CMT", "BLKCMT", "TRACMT", 
                  "BLCMT", "LINECMT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "WS" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[90] = self.UNCLOSE_STRING_action 
            actions[91] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise UncloseString(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise IllegalEscape(self.text)
     


