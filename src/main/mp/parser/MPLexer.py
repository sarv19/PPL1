# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2H")
        buf.write("\u029b\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\4b\tb\3\2\3\2\3\3\3\3\3\4\3\4\3")
        buf.write("\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3")
        buf.write("\13\3\f\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3")
        buf.write("!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3")
        buf.write("$\3$\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3%\3%\3")
        buf.write("%\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3")
        buf.write(")\3)\3)\3)\3)\3)\3*\3*\3*\3+\3+\3+\3+\3+\3,\3,\3,\3,\3")
        buf.write(",\3,\3,\3,\3,\3,\3,\3,\3,\5,\u0176\n,\3-\3-\3-\3-\3-\3")
        buf.write("-\3-\3-\3-\3-\3-\3-\5-\u0184\n-\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write("/\3/\3/\3/\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\62\3\62")
        buf.write("\3\62\3\62\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\67\3\67\38")
        buf.write("\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3")
        buf.write("A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3")
        buf.write("J\3J\3K\3K\3L\3L\3M\3M\3N\3N\3O\3O\3P\3P\3Q\3Q\3R\6R\u01e4")
        buf.write("\nR\rR\16R\u01e5\3S\6S\u01e9\nS\rS\16S\u01ea\3S\3S\3T")
        buf.write("\5T\u01f0\nT\3T\7T\u01f3\nT\fT\16T\u01f6\13T\3U\6U\u01f9")
        buf.write("\nU\rU\16U\u01fa\3V\6V\u01fe\nV\rV\16V\u01ff\3V\5V\u0203")
        buf.write("\nV\3V\7V\u0206\nV\fV\16V\u0209\13V\3V\7V\u020c\nV\fV")
        buf.write("\16V\u020f\13V\3V\3V\5V\u0213\nV\3V\6V\u0216\nV\rV\16")
        buf.write("V\u0217\5V\u021a\nV\3V\7V\u021d\nV\fV\16V\u0220\13V\3")
        buf.write("V\5V\u0223\nV\3V\6V\u0226\nV\rV\16V\u0227\3V\3V\5V\u022c")
        buf.write("\nV\3V\6V\u022f\nV\rV\16V\u0230\5V\u0233\nV\5V\u0235\n")
        buf.write("V\3W\3W\3W\3W\3W\3W\3W\3W\3W\5W\u0240\nW\3X\3X\3X\3X\7")
        buf.write("X\u0246\nX\fX\16X\u0249\13X\3X\3X\3X\3Y\3Y\3Y\3Y\3Y\5")
        buf.write("Y\u0253\nY\3Z\3Z\3[\3[\5[\u0259\n[\3[\3[\3\\\3\\\5\\\u025f")
        buf.write("\n\\\3]\3]\3]\3]\7]\u0265\n]\f]\16]\u0268\13]\3]\3]\3")
        buf.write("]\3^\3^\7^\u026f\n^\f^\16^\u0272\13^\3^\3^\3_\3_\3_\3")
        buf.write("_\7_\u027a\n_\f_\16_\u027d\13_\3`\3`\3`\5`\u0282\n`\3")
        buf.write("`\7`\u0285\n`\f`\16`\u0288\13`\3`\3`\3a\3a\3a\3a\7a\u0290")
        buf.write("\na\fa\16a\u0293\13a\3a\3a\3a\3a\3b\3b\3b\4\u0266\u0270")
        buf.write("\2c\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m\2o\2")
        buf.write("q\2s\2u\2w\2y\2{\2}\2\177\2\u0081\2\u0083\2\u0085\2\u0087")
        buf.write("\2\u0089\2\u008b\2\u008d\2\u008f\2\u0091\2\u0093\2\u0095")
        buf.write("\2\u0097\2\u0099\2\u009b\2\u009d\2\u009f\2\u00a1\2\u00a3")
        buf.write("8\u00a59\u00a7:\u00a9;\u00ab<\u00ad=\u00af>\u00b1?\u00b3")
        buf.write("@\u00b5A\u00b7B\u00b9C\u00bbD\u00bdE\u00bfF\u00c1G\u00c3")
        buf.write("H\3\2$\4\2CCcc\4\2DDdd\4\2EEee\4\2FFff\4\2GGgg\4\2HHh")
        buf.write("h\4\2IIii\4\2JJjj\4\2KKkk\4\2LLll\4\2MMmm\4\2NNnn\4\2")
        buf.write("OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2SSss\4\2TTtt\4\2UUuu\4")
        buf.write("\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4\2ZZzz\4\2[[{{\4\2\\\\")
        buf.write("||\3\2\62;\5\2\13\f\17\17\"\"\5\2C\\aac|\6\2\62;C\\aa")
        buf.write("c|\n\2$$))^^ddhhppttvv\7\2\n\f\16\17$$))^^\4\2\f\f\17")
        buf.write("\17\7\2\13\f\16\17$$))^^\2\u02a3\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2")
        buf.write(")\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2")
        buf.write("\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2")
        buf.write(";\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2")
        buf.write("\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2")
        buf.write("\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2")
        buf.write("\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3")
        buf.write("\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k")
        buf.write("\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2")
        buf.write("\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2\2\2\u00af")
        buf.write("\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2\2\2\u00b5\3\2\2")
        buf.write("\2\2\u00b7\3\2\2\2\2\u00b9\3\2\2\2\2\u00bb\3\2\2\2\2\u00bd")
        buf.write("\3\2\2\2\2\u00bf\3\2\2\2\2\u00c1\3\2\2\2\2\u00c3\3\2\2")
        buf.write("\2\3\u00c5\3\2\2\2\5\u00c7\3\2\2\2\7\u00c9\3\2\2\2\t\u00cb")
        buf.write("\3\2\2\2\13\u00cd\3\2\2\2\r\u00cf\3\2\2\2\17\u00d1\3\2")
        buf.write("\2\2\21\u00d3\3\2\2\2\23\u00d5\3\2\2\2\25\u00d7\3\2\2")
        buf.write("\2\27\u00d9\3\2\2\2\31\u00dc\3\2\2\2\33\u00de\3\2\2\2")
        buf.write("\35\u00e0\3\2\2\2\37\u00e3\3\2\2\2!\u00e5\3\2\2\2#\u00e8")
        buf.write("\3\2\2\2%\u00ea\3\2\2\2\'\u00ec\3\2\2\2)\u00ee\3\2\2\2")
        buf.write("+\u00f1\3\2\2\2-\u00f4\3\2\2\2/\u00fa\3\2\2\2\61\u0103")
        buf.write("\3\2\2\2\63\u0107\3\2\2\2\65\u010a\3\2\2\2\67\u0111\3")
        buf.write("\2\2\29\u0114\3\2\2\2;\u0117\3\2\2\2=\u011c\3\2\2\2?\u0121")
        buf.write("\3\2\2\2A\u0128\3\2\2\2C\u012e\3\2\2\2E\u0134\3\2\2\2")
        buf.write("G\u0138\3\2\2\2I\u0141\3\2\2\2K\u014b\3\2\2\2M\u014f\3")
        buf.write("\2\2\2O\u0154\3\2\2\2Q\u015a\3\2\2\2S\u0160\3\2\2\2U\u0163")
        buf.write("\3\2\2\2W\u0175\3\2\2\2Y\u0183\3\2\2\2[\u0185\3\2\2\2")
        buf.write("]\u018c\3\2\2\2_\u0190\3\2\2\2a\u0194\3\2\2\2c\u0197\3")
        buf.write("\2\2\2e\u019b\3\2\2\2g\u019f\3\2\2\2i\u01a4\3\2\2\2k\u01a8")
        buf.write("\3\2\2\2m\u01ac\3\2\2\2o\u01ae\3\2\2\2q\u01b0\3\2\2\2")
        buf.write("s\u01b2\3\2\2\2u\u01b4\3\2\2\2w\u01b6\3\2\2\2y\u01b8\3")
        buf.write("\2\2\2{\u01ba\3\2\2\2}\u01bc\3\2\2\2\177\u01be\3\2\2\2")
        buf.write("\u0081\u01c0\3\2\2\2\u0083\u01c2\3\2\2\2\u0085\u01c4\3")
        buf.write("\2\2\2\u0087\u01c6\3\2\2\2\u0089\u01c8\3\2\2\2\u008b\u01ca")
        buf.write("\3\2\2\2\u008d\u01cc\3\2\2\2\u008f\u01ce\3\2\2\2\u0091")
        buf.write("\u01d0\3\2\2\2\u0093\u01d2\3\2\2\2\u0095\u01d4\3\2\2\2")
        buf.write("\u0097\u01d6\3\2\2\2\u0099\u01d8\3\2\2\2\u009b\u01da\3")
        buf.write("\2\2\2\u009d\u01dc\3\2\2\2\u009f\u01de\3\2\2\2\u00a1\u01e0")
        buf.write("\3\2\2\2\u00a3\u01e3\3\2\2\2\u00a5\u01e8\3\2\2\2\u00a7")
        buf.write("\u01ef\3\2\2\2\u00a9\u01f8\3\2\2\2\u00ab\u0234\3\2\2\2")
        buf.write("\u00ad\u023f\3\2\2\2\u00af\u0241\3\2\2\2\u00b1\u0252\3")
        buf.write("\2\2\2\u00b3\u0254\3\2\2\2\u00b5\u0258\3\2\2\2\u00b7\u025e")
        buf.write("\3\2\2\2\u00b9\u0260\3\2\2\2\u00bb\u026c\3\2\2\2\u00bd")
        buf.write("\u0275\3\2\2\2\u00bf\u027e\3\2\2\2\u00c1\u028b\3\2\2\2")
        buf.write("\u00c3\u0298\3\2\2\2\u00c5\u00c6\7*\2\2\u00c6\4\3\2\2")
        buf.write("\2\u00c7\u00c8\7+\2\2\u00c8\6\3\2\2\2\u00c9\u00ca\7}\2")
        buf.write("\2\u00ca\b\3\2\2\2\u00cb\u00cc\7\177\2\2\u00cc\n\3\2\2")
        buf.write("\2\u00cd\u00ce\7]\2\2\u00ce\f\3\2\2\2\u00cf\u00d0\7_\2")
        buf.write("\2\u00d0\16\3\2\2\2\u00d1\u00d2\7=\2\2\u00d2\20\3\2\2")
        buf.write("\2\u00d3\u00d4\7.\2\2\u00d4\22\3\2\2\2\u00d5\u00d6\7?")
        buf.write("\2\2\u00d6\24\3\2\2\2\u00d7\u00d8\7<\2\2\u00d8\26\3\2")
        buf.write("\2\2\u00d9\u00da\7\60\2\2\u00da\u00db\7\60\2\2\u00db\30")
        buf.write("\3\2\2\2\u00dc\u00dd\7-\2\2\u00dd\32\3\2\2\2\u00de\u00df")
        buf.write("\7,\2\2\u00df\34\3\2\2\2\u00e0\u00e1\7>\2\2\u00e1\u00e2")
        buf.write("\7@\2\2\u00e2\36\3\2\2\2\u00e3\u00e4\7>\2\2\u00e4 \3\2")
        buf.write("\2\2\u00e5\u00e6\7>\2\2\u00e6\u00e7\7?\2\2\u00e7\"\3\2")
        buf.write("\2\2\u00e8\u00e9\7/\2\2\u00e9$\3\2\2\2\u00ea\u00eb\7\61")
        buf.write("\2\2\u00eb&\3\2\2\2\u00ec\u00ed\7@\2\2\u00ed(\3\2\2\2")
        buf.write("\u00ee\u00ef\7@\2\2\u00ef\u00f0\7?\2\2\u00f0*\3\2\2\2")
        buf.write("\u00f1\u00f2\7<\2\2\u00f2\u00f3\7?\2\2\u00f3,\3\2\2\2")
        buf.write("\u00f4\u00f5\5o8\2\u00f5\u00f6\5\u008fH\2\u00f6\u00f7")
        buf.write("\5u;\2\u00f7\u00f8\5m\67\2\u00f8\u00f9\5\u0081A\2\u00f9")
        buf.write(".\3\2\2\2\u00fa\u00fb\5q9\2\u00fb\u00fc\5\u0089E\2\u00fc")
        buf.write("\u00fd\5\u0087D\2\u00fd\u00fe\5\u0093J\2\u00fe\u00ff\5")
        buf.write("}?\2\u00ff\u0100\5\u0087D\2\u0100\u0101\5\u0095K\2\u0101")
        buf.write("\u0102\5u;\2\u0102\60\3\2\2\2\u0103\u0104\5w<\2\u0104")
        buf.write("\u0105\5\u0089E\2\u0105\u0106\5\u008fH\2\u0106\62\3\2")
        buf.write("\2\2\u0107\u0108\5\u0093J\2\u0108\u0109\5\u0089E\2\u0109")
        buf.write("\64\3\2\2\2\u010a\u010b\5s:\2\u010b\u010c\5\u0089E\2\u010c")
        buf.write("\u010d\5\u0099M\2\u010d\u010e\5\u0087D\2\u010e\u010f\5")
        buf.write("\u0093J\2\u010f\u0110\5\u0089E\2\u0110\66\3\2\2\2\u0111")
        buf.write("\u0112\5s:\2\u0112\u0113\5\u0089E\2\u01138\3\2\2\2\u0114")
        buf.write("\u0115\5}?\2\u0115\u0116\5w<\2\u0116:\3\2\2\2\u0117\u0118")
        buf.write("\5\u0093J\2\u0118\u0119\5{>\2\u0119\u011a\5u;\2\u011a")
        buf.write("\u011b\5\u0087D\2\u011b<\3\2\2\2\u011c\u011d\5u;\2\u011d")
        buf.write("\u011e\5\u0083B\2\u011e\u011f\5\u0091I\2\u011f\u0120\5")
        buf.write("u;\2\u0120>\3\2\2\2\u0121\u0122\5\u008fH\2\u0122\u0123")
        buf.write("\5u;\2\u0123\u0124\5\u0093J\2\u0124\u0125\5\u0095K\2\u0125")
        buf.write("\u0126\5\u008fH\2\u0126\u0127\5\u0087D\2\u0127@\3\2\2")
        buf.write("\2\u0128\u0129\5\u0099M\2\u0129\u012a\5{>\2\u012a\u012b")
        buf.write("\5}?\2\u012b\u012c\5\u0083B\2\u012c\u012d\5u;\2\u012d")
        buf.write("B\3\2\2\2\u012e\u012f\5o8\2\u012f\u0130\5u;\2\u0130\u0131")
        buf.write("\5y=\2\u0131\u0132\5}?\2\u0132\u0133\5\u0087D\2\u0133")
        buf.write("D\3\2\2\2\u0134\u0135\5u;\2\u0135\u0136\5\u0087D\2\u0136")
        buf.write("\u0137\5s:\2\u0137F\3\2\2\2\u0138\u0139\5w<\2\u0139\u013a")
        buf.write("\5\u0095K\2\u013a\u013b\5\u0087D\2\u013b\u013c\5q9\2\u013c")
        buf.write("\u013d\5\u0093J\2\u013d\u013e\5}?\2\u013e\u013f\5\u0089")
        buf.write("E\2\u013f\u0140\5\u0087D\2\u0140H\3\2\2\2\u0141\u0142")
        buf.write("\5\u008bF\2\u0142\u0143\5\u008fH\2\u0143\u0144\5\u0089")
        buf.write("E\2\u0144\u0145\5q9\2\u0145\u0146\5u;\2\u0146\u0147\5")
        buf.write("s:\2\u0147\u0148\5\u0095K\2\u0148\u0149\5\u008fH\2\u0149")
        buf.write("\u014a\5u;\2\u014aJ\3\2\2\2\u014b\u014c\5\u0097L\2\u014c")
        buf.write("\u014d\5m\67\2\u014d\u014e\5\u008fH\2\u014eL\3\2\2\2\u014f")
        buf.write("\u0150\5\u0093J\2\u0150\u0151\5\u008fH\2\u0151\u0152\5")
        buf.write("\u0095K\2\u0152\u0153\5u;\2\u0153N\3\2\2\2\u0154\u0155")
        buf.write("\5w<\2\u0155\u0156\5m\67\2\u0156\u0157\5\u0083B\2\u0157")
        buf.write("\u0158\5\u0091I\2\u0158\u0159\5u;\2\u0159P\3\2\2\2\u015a")
        buf.write("\u015b\5m\67\2\u015b\u015c\5\u008fH\2\u015c\u015d\5\u008f")
        buf.write("H\2\u015d\u015e\5m\67\2\u015e\u015f\5\u009dO\2\u015fR")
        buf.write("\3\2\2\2\u0160\u0161\5\u0089E\2\u0161\u0162\5w<\2\u0162")
        buf.write("T\3\2\2\2\u0163\u0164\5\u008fH\2\u0164\u0165\5u;\2\u0165")
        buf.write("\u0166\5m\67\2\u0166\u0167\5\u0083B\2\u0167V\3\2\2\2\u0168")
        buf.write("\u0169\5o8\2\u0169\u016a\5\u0089E\2\u016a\u016b\5\u0089")
        buf.write("E\2\u016b\u016c\5\u0083B\2\u016c\u016d\5u;\2\u016d\u016e")
        buf.write("\5m\67\2\u016e\u016f\5\u0087D\2\u016f\u0176\3\2\2\2\u0170")
        buf.write("\u0171\5o8\2\u0171\u0172\5\u0089E\2\u0172\u0173\5\u0089")
        buf.write("E\2\u0173\u0174\5\u0083B\2\u0174\u0176\3\2\2\2\u0175\u0168")
        buf.write("\3\2\2\2\u0175\u0170\3\2\2\2\u0176X\3\2\2\2\u0177\u0178")
        buf.write("\5}?\2\u0178\u0179\5\u0087D\2\u0179\u017a\5\u0093J\2\u017a")
        buf.write("\u017b\5u;\2\u017b\u017c\5y=\2\u017c\u017d\5u;\2\u017d")
        buf.write("\u017e\5\u008fH\2\u017e\u0184\3\2\2\2\u017f\u0180\5}?")
        buf.write("\2\u0180\u0181\5\u0087D\2\u0181\u0182\5\u0093J\2\u0182")
        buf.write("\u0184\3\2\2\2\u0183\u0177\3\2\2\2\u0183\u017f\3\2\2\2")
        buf.write("\u0184Z\3\2\2\2\u0185\u0186\5\u0091I\2\u0186\u0187\5\u0093")
        buf.write("J\2\u0187\u0188\5\u008fH\2\u0188\u0189\5}?\2\u0189\u018a")
        buf.write("\5\u0087D\2\u018a\u018b\5y=\2\u018b\\\3\2\2\2\u018c\u018d")
        buf.write("\5\u0087D\2\u018d\u018e\5\u0089E\2\u018e\u018f\5\u0093")
        buf.write("J\2\u018f^\3\2\2\2\u0190\u0191\5m\67\2\u0191\u0192\5\u0087")
        buf.write("D\2\u0192\u0193\5s:\2\u0193`\3\2\2\2\u0194\u0195\5\u0089")
        buf.write("E\2\u0195\u0196\5\u008fH\2\u0196b\3\2\2\2\u0197\u0198")
        buf.write("\5s:\2\u0198\u0199\5}?\2\u0199\u019a\5\u0097L\2\u019a")
        buf.write("d\3\2\2\2\u019b\u019c\5\u0085C\2\u019c\u019d\5\u0089E")
        buf.write("\2\u019d\u019e\5s:\2\u019ef\3\2\2\2\u019f\u01a0\5\u0085")
        buf.write("C\2\u01a0\u01a1\5m\67\2\u01a1\u01a2\5}?\2\u01a2\u01a3")
        buf.write("\5\u0087D\2\u01a3h\3\2\2\2\u01a4\u01a5\5_\60\2\u01a5\u01a6")
        buf.write("\5\u00b3Z\2\u01a6\u01a7\5;\36\2\u01a7j\3\2\2\2\u01a8\u01a9")
        buf.write("\5a\61\2\u01a9\u01aa\5\u00b3Z\2\u01aa\u01ab\5=\37\2\u01ab")
        buf.write("l\3\2\2\2\u01ac\u01ad\t\2\2\2\u01adn\3\2\2\2\u01ae\u01af")
        buf.write("\t\3\2\2\u01afp\3\2\2\2\u01b0\u01b1\t\4\2\2\u01b1r\3\2")
        buf.write("\2\2\u01b2\u01b3\t\5\2\2\u01b3t\3\2\2\2\u01b4\u01b5\t")
        buf.write("\6\2\2\u01b5v\3\2\2\2\u01b6\u01b7\t\7\2\2\u01b7x\3\2\2")
        buf.write("\2\u01b8\u01b9\t\b\2\2\u01b9z\3\2\2\2\u01ba\u01bb\t\t")
        buf.write("\2\2\u01bb|\3\2\2\2\u01bc\u01bd\t\n\2\2\u01bd~\3\2\2\2")
        buf.write("\u01be\u01bf\t\13\2\2\u01bf\u0080\3\2\2\2\u01c0\u01c1")
        buf.write("\t\f\2\2\u01c1\u0082\3\2\2\2\u01c2\u01c3\t\r\2\2\u01c3")
        buf.write("\u0084\3\2\2\2\u01c4\u01c5\t\16\2\2\u01c5\u0086\3\2\2")
        buf.write("\2\u01c6\u01c7\t\17\2\2\u01c7\u0088\3\2\2\2\u01c8\u01c9")
        buf.write("\t\20\2\2\u01c9\u008a\3\2\2\2\u01ca\u01cb\t\21\2\2\u01cb")
        buf.write("\u008c\3\2\2\2\u01cc\u01cd\t\22\2\2\u01cd\u008e\3\2\2")
        buf.write("\2\u01ce\u01cf\t\23\2\2\u01cf\u0090\3\2\2\2\u01d0\u01d1")
        buf.write("\t\24\2\2\u01d1\u0092\3\2\2\2\u01d2\u01d3\t\25\2\2\u01d3")
        buf.write("\u0094\3\2\2\2\u01d4\u01d5\t\26\2\2\u01d5\u0096\3\2\2")
        buf.write("\2\u01d6\u01d7\t\27\2\2\u01d7\u0098\3\2\2\2\u01d8\u01d9")
        buf.write("\t\30\2\2\u01d9\u009a\3\2\2\2\u01da\u01db\t\31\2\2\u01db")
        buf.write("\u009c\3\2\2\2\u01dc\u01dd\t\32\2\2\u01dd\u009e\3\2\2")
        buf.write("\2\u01de\u01df\t\33\2\2\u01df\u00a0\3\2\2\2\u01e0\u01e1")
        buf.write("\t\34\2\2\u01e1\u00a2\3\2\2\2\u01e2\u01e4\5\u00a1Q\2\u01e3")
        buf.write("\u01e2\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5\u01e3\3\2\2\2")
        buf.write("\u01e5\u01e6\3\2\2\2\u01e6\u00a4\3\2\2\2\u01e7\u01e9\t")
        buf.write("\35\2\2\u01e8\u01e7\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea")
        buf.write("\u01e8\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb\u01ec\3\2\2\2")
        buf.write("\u01ec\u01ed\bS\2\2\u01ed\u00a6\3\2\2\2\u01ee\u01f0\t")
        buf.write("\36\2\2\u01ef\u01ee\3\2\2\2\u01f0\u01f4\3\2\2\2\u01f1")
        buf.write("\u01f3\t\37\2\2\u01f2\u01f1\3\2\2\2\u01f3\u01f6\3\2\2")
        buf.write("\2\u01f4\u01f2\3\2\2\2\u01f4\u01f5\3\2\2\2\u01f5\u00a8")
        buf.write("\3\2\2\2\u01f6\u01f4\3\2\2\2\u01f7\u01f9\t\34\2\2\u01f8")
        buf.write("\u01f7\3\2\2\2\u01f9\u01fa\3\2\2\2\u01fa\u01f8\3\2\2\2")
        buf.write("\u01fa\u01fb\3\2\2\2\u01fb\u00aa\3\2\2\2\u01fc\u01fe\t")
        buf.write("\34\2\2\u01fd\u01fc\3\2\2\2\u01fe\u01ff\3\2\2\2\u01ff")
        buf.write("\u01fd\3\2\2\2\u01ff\u0200\3\2\2\2\u0200\u0202\3\2\2\2")
        buf.write("\u0201\u0203\7\60\2\2\u0202\u0201\3\2\2\2\u0202\u0203")
        buf.write("\3\2\2\2\u0203\u0207\3\2\2\2\u0204\u0206\t\34\2\2\u0205")
        buf.write("\u0204\3\2\2\2\u0206\u0209\3\2\2\2\u0207\u0205\3\2\2\2")
        buf.write("\u0207\u0208\3\2\2\2\u0208\u0219\3\2\2\2\u0209\u0207\3")
        buf.write("\2\2\2\u020a\u020c\t\34\2\2\u020b\u020a\3\2\2\2\u020c")
        buf.write("\u020f\3\2\2\2\u020d\u020b\3\2\2\2\u020d\u020e\3\2\2\2")
        buf.write("\u020e\u0210\3\2\2\2\u020f\u020d\3\2\2\2\u0210\u0212\t")
        buf.write("\6\2\2\u0211\u0213\7/\2\2\u0212\u0211\3\2\2\2\u0212\u0213")
        buf.write("\3\2\2\2\u0213\u0215\3\2\2\2\u0214\u0216\t\34\2\2\u0215")
        buf.write("\u0214\3\2\2\2\u0216\u0217\3\2\2\2\u0217\u0215\3\2\2\2")
        buf.write("\u0217\u0218\3\2\2\2\u0218\u021a\3\2\2\2\u0219\u020d\3")
        buf.write("\2\2\2\u0219\u021a\3\2\2\2\u021a\u0235\3\2\2\2\u021b\u021d")
        buf.write("\t\34\2\2\u021c\u021b\3\2\2\2\u021d\u0220\3\2\2\2\u021e")
        buf.write("\u021c\3\2\2\2\u021e\u021f\3\2\2\2\u021f\u0222\3\2\2\2")
        buf.write("\u0220\u021e\3\2\2\2\u0221\u0223\7\60\2\2\u0222\u0221")
        buf.write("\3\2\2\2\u0222\u0223\3\2\2\2\u0223\u0225\3\2\2\2\u0224")
        buf.write("\u0226\t\34\2\2\u0225\u0224\3\2\2\2\u0226\u0227\3\2\2")
        buf.write("\2\u0227\u0225\3\2\2\2\u0227\u0228\3\2\2\2\u0228\u0232")
        buf.write("\3\2\2\2\u0229\u022b\t\6\2\2\u022a\u022c\7/\2\2\u022b")
        buf.write("\u022a\3\2\2\2\u022b\u022c\3\2\2\2\u022c\u022e\3\2\2\2")
        buf.write("\u022d\u022f\t\34\2\2\u022e\u022d\3\2\2\2\u022f\u0230")
        buf.write("\3\2\2\2\u0230\u022e\3\2\2\2\u0230\u0231\3\2\2\2\u0231")
        buf.write("\u0233\3\2\2\2\u0232\u0229\3\2\2\2\u0232\u0233\3\2\2\2")
        buf.write("\u0233\u0235\3\2\2\2\u0234\u01fd\3\2\2\2\u0234\u021e\3")
        buf.write("\2\2\2\u0235\u00ac\3\2\2\2\u0236\u0237\7v\2\2\u0237\u0238")
        buf.write("\7t\2\2\u0238\u0239\7w\2\2\u0239\u0240\7g\2\2\u023a\u023b")
        buf.write("\7h\2\2\u023b\u023c\7c\2\2\u023c\u023d\7n\2\2\u023d\u023e")
        buf.write("\7u\2\2\u023e\u0240\7g\2\2\u023f\u0236\3\2\2\2\u023f\u023a")
        buf.write("\3\2\2\2\u0240\u00ae\3\2\2\2\u0241\u0247\7$\2\2\u0242")
        buf.write("\u0243\7^\2\2\u0243\u0246\t \2\2\u0244\u0246\n!\2\2\u0245")
        buf.write("\u0242\3\2\2\2\u0245\u0244\3\2\2\2\u0246\u0249\3\2\2\2")
        buf.write("\u0247\u0245\3\2\2\2\u0247\u0248\3\2\2\2\u0248\u024a\3")
        buf.write("\2\2\2\u0249\u0247\3\2\2\2\u024a\u024b\7$\2\2\u024b\u024c")
        buf.write("\bX\3\2\u024c\u00b0\3\2\2\2\u024d\u0253\5W,\2\u024e\u0253")
        buf.write("\5Y-\2\u024f\u0253\5U+\2\u0250\u0253\5[.\2\u0251\u0253")
        buf.write("\5Q)\2\u0252\u024d\3\2\2\2\u0252\u024e\3\2\2\2\u0252\u024f")
        buf.write("\3\2\2\2\u0252\u0250\3\2\2\2\u0252\u0251\3\2\2\2\u0253")
        buf.write("\u00b2\3\2\2\2\u0254\u0255\7\"\2\2\u0255\u00b4\3\2\2\2")
        buf.write("\u0256\u0259\5\u00b7\\\2\u0257\u0259\5\u00bd_\2\u0258")
        buf.write("\u0256\3\2\2\2\u0258\u0257\3\2\2\2\u0259\u025a\3\2\2\2")
        buf.write("\u025a\u025b\b[\2\2\u025b\u00b6\3\2\2\2\u025c\u025f\5")
        buf.write("\u00b9]\2\u025d\u025f\5\u00bb^\2\u025e\u025c\3\2\2\2\u025e")
        buf.write("\u025d\3\2\2\2\u025f\u00b8\3\2\2\2\u0260\u0261\7*\2\2")
        buf.write("\u0261\u0262\7,\2\2\u0262\u0266\3\2\2\2\u0263\u0265\13")
        buf.write("\2\2\2\u0264\u0263\3\2\2\2\u0265\u0268\3\2\2\2\u0266\u0267")
        buf.write("\3\2\2\2\u0266\u0264\3\2\2\2\u0267\u0269\3\2\2\2\u0268")
        buf.write("\u0266\3\2\2\2\u0269\u026a\7,\2\2\u026a\u026b\7+\2\2\u026b")
        buf.write("\u00ba\3\2\2\2\u026c\u0270\7}\2\2\u026d\u026f\13\2\2\2")
        buf.write("\u026e\u026d\3\2\2\2\u026f\u0272\3\2\2\2\u0270\u0271\3")
        buf.write("\2\2\2\u0270\u026e\3\2\2\2\u0271\u0273\3\2\2\2\u0272\u0270")
        buf.write("\3\2\2\2\u0273\u0274\7\177\2\2\u0274\u00bc\3\2\2\2\u0275")
        buf.write("\u0276\7\61\2\2\u0276\u0277\7\61\2\2\u0277\u027b\3\2\2")
        buf.write("\2\u0278\u027a\n\"\2\2\u0279\u0278\3\2\2\2\u027a\u027d")
        buf.write("\3\2\2\2\u027b\u0279\3\2\2\2\u027b\u027c\3\2\2\2\u027c")
        buf.write("\u00be\3\2\2\2\u027d\u027b\3\2\2\2\u027e\u0286\7$\2\2")
        buf.write("\u027f\u0281\7^\2\2\u0280\u0282\t \2\2\u0281\u0280\3\2")
        buf.write("\2\2\u0282\u0285\3\2\2\2\u0283\u0285\n!\2\2\u0284\u027f")
        buf.write("\3\2\2\2\u0284\u0283\3\2\2\2\u0285\u0288\3\2\2\2\u0286")
        buf.write("\u0284\3\2\2\2\u0286\u0287\3\2\2\2\u0287\u0289\3\2\2\2")
        buf.write("\u0288\u0286\3\2\2\2\u0289\u028a\b`\4\2\u028a\u00c0\3")
        buf.write("\2\2\2\u028b\u0291\7$\2\2\u028c\u0290\n#\2\2\u028d\u028e")
        buf.write("\7^\2\2\u028e\u0290\t \2\2\u028f\u028c\3\2\2\2\u028f\u028d")
        buf.write("\3\2\2\2\u0290\u0293\3\2\2\2\u0291\u028f\3\2\2\2\u0291")
        buf.write("\u0292\3\2\2\2\u0292\u0294\3\2\2\2\u0293\u0291\3\2\2\2")
        buf.write("\u0294\u0295\7^\2\2\u0295\u0296\n \2\2\u0296\u0297\ba")
        buf.write("\5\2\u0297\u00c2\3\2\2\2\u0298\u0299\13\2\2\2\u0299\u029a")
        buf.write("\bb\6\2\u029a\u00c4\3\2\2\2\'\2\u0175\u0183\u01e5\u01ea")
        buf.write("\u01ef\u01f2\u01f4\u01fa\u01ff\u0202\u0207\u020d\u0212")
        buf.write("\u0217\u0219\u021e\u0222\u0227\u022b\u0230\u0232\u0234")
        buf.write("\u023f\u0245\u0247\u0252\u0258\u025e\u0266\u0270\u027b")
        buf.write("\u0281\u0284\u0286\u028f\u0291\7\b\2\2\3X\2\3`\3\3a\4")
        buf.write("\3b\5")
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
    ASSI = 21
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
    MAIN = 51
    ANDTHEN = 52
    ORELSE = 53
    ManyNum = 54
    WS = 55
    ID = 56
    INTLIT = 57
    REALLIT = 58
    BOOLLIT = 59
    STRINGLIT = 60
    TYPE = 61
    SP = 62
    CMT = 63
    BLKCMT = 64
    TRACMT = 65
    BLCMT = 66
    LINECMT = 67
    UNCLOSE_STRING = 68
    ILLEGAL_ESCAPE = 69
    ERROR_CHAR = 70

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "','", "'='", 
            "':'", "'..'", "'+'", "'*'", "'<>'", "'<'", "'<='", "'-'", "'/'", 
            "'>'", "'>='", "':='", "' '" ]

    symbolicNames = [ "<INVALID>",
            "LB", "RB", "LP", "RP", "LQ", "RQ", "SEMI", "CM", "EQ", "COL", 
            "DD", "ADD", "MUL", "NOTEQ", "LESSTN", "LESSEQ", "SUBNE", "DIVSI", 
            "GRETN", "GREEQ", "ASSI", "BREAK", "CONTINUE", "FOR", "TO", 
            "DOWNTO", "DO", "IF", "THEN", "ELSE", "RETURN", "WHILE", "BEGIN", 
            "END", "FUNCTION", "PROCEDURE", "VAR", "TRUE", "FALSE", "ARRAY", 
            "OF", "REAL", "BOOLEAN", "INTEGER", "STRING", "NOT", "AND", 
            "OR", "DIV", "MOD", "MAIN", "ANDTHEN", "ORELSE", "ManyNum", 
            "WS", "ID", "INTLIT", "REALLIT", "BOOLLIT", "STRINGLIT", "TYPE", 
            "SP", "CMT", "BLKCMT", "TRACMT", "BLCMT", "LINECMT", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "LB", "RB", "LP", "RP", "LQ", "RQ", "SEMI", "CM", "EQ", 
                  "COL", "DD", "ADD", "MUL", "NOTEQ", "LESSTN", "LESSEQ", 
                  "SUBNE", "DIVSI", "GRETN", "GREEQ", "ASSI", "BREAK", "CONTINUE", 
                  "FOR", "TO", "DOWNTO", "DO", "IF", "THEN", "ELSE", "RETURN", 
                  "WHILE", "BEGIN", "END", "FUNCTION", "PROCEDURE", "VAR", 
                  "TRUE", "FALSE", "ARRAY", "OF", "REAL", "BOOLEAN", "INTEGER", 
                  "STRING", "NOT", "AND", "OR", "DIV", "MOD", "MAIN", "ANDTHEN", 
                  "ORELSE", "A", "B", "C", "D", "E", "F", "G", "H", "I", 
                  "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", 
                  "U", "V", "W", "X", "Y", "Z", "NUM", "ManyNum", "WS", 
                  "ID", "INTLIT", "REALLIT", "BOOLLIT", "STRINGLIT", "TYPE", 
                  "SP", "CMT", "BLKCMT", "TRACMT", "BLCMT", "LINECMT", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

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
            actions[86] = self.STRINGLIT_action 
            actions[94] = self.UNCLOSE_STRING_action 
            actions[95] = self.ILLEGAL_ESCAPE_action 
            actions[96] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:len(self.text) - 1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise UncloseString(self.text[1:])
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise IllegalEscape(self.text[1:])
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


