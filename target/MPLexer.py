# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u0284\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3$\3$")
        buf.write("\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3\'\3\'\3\'")
        buf.write("\3\'\3\'\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3*\3*\3*")
        buf.write("\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3")
        buf.write(",\5,\u016e\n,\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u017c")
        buf.write("\n-\3.\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3\60\3\60\3\60\3")
        buf.write("\60\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\63\3\63\3\63")
        buf.write("\3\63\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\66\3\66\3\67")
        buf.write("\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?")
        buf.write("\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3")
        buf.write("H\3I\3I\3J\3J\3K\3K\3L\3L\3M\3M\3N\3N\3O\3O\3P\6P\u01d4")
        buf.write("\nP\rP\16P\u01d5\3P\3P\3Q\5Q\u01db\nQ\3Q\7Q\u01de\nQ\f")
        buf.write("Q\16Q\u01e1\13Q\3R\6R\u01e4\nR\rR\16R\u01e5\3S\6S\u01e9")
        buf.write("\nS\rS\16S\u01ea\3S\5S\u01ee\nS\3S\7S\u01f1\nS\fS\16S")
        buf.write("\u01f4\13S\3S\7S\u01f7\nS\fS\16S\u01fa\13S\3S\3S\5S\u01fe")
        buf.write("\nS\3S\6S\u0201\nS\rS\16S\u0202\5S\u0205\nS\3S\7S\u0208")
        buf.write("\nS\fS\16S\u020b\13S\3S\5S\u020e\nS\3S\6S\u0211\nS\rS")
        buf.write("\16S\u0212\3S\3S\5S\u0217\nS\3S\6S\u021a\nS\rS\16S\u021b")
        buf.write("\5S\u021e\nS\5S\u0220\nS\3T\3T\3T\3T\3T\3T\3T\3T\3T\5")
        buf.write("T\u022b\nT\3U\3U\3U\3U\7U\u0231\nU\fU\16U\u0234\13U\3")
        buf.write("U\3U\3U\3V\3V\3V\3V\3V\5V\u023e\nV\3W\3W\5W\u0242\nW\3")
        buf.write("W\3W\3X\3X\5X\u0248\nX\3Y\3Y\3Y\3Y\7Y\u024e\nY\fY\16Y")
        buf.write("\u0251\13Y\3Y\3Y\3Y\3Z\3Z\7Z\u0258\nZ\fZ\16Z\u025b\13")
        buf.write("Z\3Z\3Z\3[\3[\3[\3[\7[\u0263\n[\f[\16[\u0266\13[\3\\\3")
        buf.write("\\\3\\\5\\\u026b\n\\\3\\\7\\\u026e\n\\\f\\\16\\\u0271")
        buf.write("\13\\\3\\\3\\\3]\3]\3]\3]\7]\u0279\n]\f]\16]\u027c\13")
        buf.write("]\3]\3]\3]\3]\3^\3^\3^\4\u024f\u0259\2_\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60")
        buf.write("_\61a\62c\63e\64g\65i\2k\2m\2o\2q\2s\2u\2w\2y\2{\2}\2")
        buf.write("\177\2\u0081\2\u0083\2\u0085\2\u0087\2\u0089\2\u008b\2")
        buf.write("\u008d\2\u008f\2\u0091\2\u0093\2\u0095\2\u0097\2\u0099")
        buf.write("\2\u009b\2\u009d\2\u009f\66\u00a1\67\u00a38\u00a59\u00a7")
        buf.write(":\u00a9;\u00ab<\u00ad=\u00af>\u00b1?\u00b3@\u00b5A\u00b7")
        buf.write("B\u00b9C\u00bbD\3\2$\4\2CCcc\4\2DDdd\4\2EEee\4\2FFff\4")
        buf.write("\2GGgg\4\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4\2LLll\4\2MMm")
        buf.write("m\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2SSss\4\2")
        buf.write("TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4\2ZZzz\4")
        buf.write("\2[[{{\4\2\\\\||\3\2\62;\5\2\13\f\17\17\"\"\5\2C\\aac")
        buf.write("|\6\2\62;C\\aac|\n\2$$))^^ddhhppttvv\7\2\n\f\16\17$$)")
        buf.write(")^^\4\2\f\f\17\17\7\2\13\f\16\17$$))^^\2\u028b\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_")
        buf.write("\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2")
        buf.write("\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5")
        buf.write("\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2")
        buf.write("\2\2\u00ad\3\2\2\2\2\u00af\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3")
        buf.write("\3\2\2\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2\2\2\u00b9\3\2\2")
        buf.write("\2\2\u00bb\3\2\2\2\3\u00bd\3\2\2\2\5\u00bf\3\2\2\2\7\u00c1")
        buf.write("\3\2\2\2\t\u00c3\3\2\2\2\13\u00c5\3\2\2\2\r\u00c7\3\2")
        buf.write("\2\2\17\u00c9\3\2\2\2\21\u00cb\3\2\2\2\23\u00cd\3\2\2")
        buf.write("\2\25\u00cf\3\2\2\2\27\u00d1\3\2\2\2\31\u00d4\3\2\2\2")
        buf.write("\33\u00d6\3\2\2\2\35\u00d8\3\2\2\2\37\u00db\3\2\2\2!\u00dd")
        buf.write("\3\2\2\2#\u00e0\3\2\2\2%\u00e2\3\2\2\2\'\u00e4\3\2\2\2")
        buf.write(")\u00e6\3\2\2\2+\u00e9\3\2\2\2-\u00ec\3\2\2\2/\u00f2\3")
        buf.write("\2\2\2\61\u00fb\3\2\2\2\63\u00ff\3\2\2\2\65\u0102\3\2")
        buf.write("\2\2\67\u0109\3\2\2\29\u010c\3\2\2\2;\u010f\3\2\2\2=\u0114")
        buf.write("\3\2\2\2?\u0119\3\2\2\2A\u0120\3\2\2\2C\u0126\3\2\2\2")
        buf.write("E\u012c\3\2\2\2G\u0130\3\2\2\2I\u0139\3\2\2\2K\u0143\3")
        buf.write("\2\2\2M\u0147\3\2\2\2O\u014c\3\2\2\2Q\u0152\3\2\2\2S\u0158")
        buf.write("\3\2\2\2U\u015b\3\2\2\2W\u016d\3\2\2\2Y\u017b\3\2\2\2")
        buf.write("[\u017d\3\2\2\2]\u0184\3\2\2\2_\u0188\3\2\2\2a\u018c\3")
        buf.write("\2\2\2c\u018f\3\2\2\2e\u0193\3\2\2\2g\u0197\3\2\2\2i\u019c")
        buf.write("\3\2\2\2k\u019e\3\2\2\2m\u01a0\3\2\2\2o\u01a2\3\2\2\2")
        buf.write("q\u01a4\3\2\2\2s\u01a6\3\2\2\2u\u01a8\3\2\2\2w\u01aa\3")
        buf.write("\2\2\2y\u01ac\3\2\2\2{\u01ae\3\2\2\2}\u01b0\3\2\2\2\177")
        buf.write("\u01b2\3\2\2\2\u0081\u01b4\3\2\2\2\u0083\u01b6\3\2\2\2")
        buf.write("\u0085\u01b8\3\2\2\2\u0087\u01ba\3\2\2\2\u0089\u01bc\3")
        buf.write("\2\2\2\u008b\u01be\3\2\2\2\u008d\u01c0\3\2\2\2\u008f\u01c2")
        buf.write("\3\2\2\2\u0091\u01c4\3\2\2\2\u0093\u01c6\3\2\2\2\u0095")
        buf.write("\u01c8\3\2\2\2\u0097\u01ca\3\2\2\2\u0099\u01cc\3\2\2\2")
        buf.write("\u009b\u01ce\3\2\2\2\u009d\u01d0\3\2\2\2\u009f\u01d3\3")
        buf.write("\2\2\2\u00a1\u01da\3\2\2\2\u00a3\u01e3\3\2\2\2\u00a5\u021f")
        buf.write("\3\2\2\2\u00a7\u022a\3\2\2\2\u00a9\u022c\3\2\2\2\u00ab")
        buf.write("\u023d\3\2\2\2\u00ad\u0241\3\2\2\2\u00af\u0247\3\2\2\2")
        buf.write("\u00b1\u0249\3\2\2\2\u00b3\u0255\3\2\2\2\u00b5\u025e\3")
        buf.write("\2\2\2\u00b7\u0267\3\2\2\2\u00b9\u0274\3\2\2\2\u00bb\u0281")
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
        buf.write("\2\2\u00e7\u00e8\7?\2\2\u00e8*\3\2\2\2\u00e9\u00ea\7<")
        buf.write("\2\2\u00ea\u00eb\7?\2\2\u00eb,\3\2\2\2\u00ec\u00ed\5k")
        buf.write("\66\2\u00ed\u00ee\5\u008bF\2\u00ee\u00ef\5q9\2\u00ef\u00f0")
        buf.write("\5i\65\2\u00f0\u00f1\5}?\2\u00f1.\3\2\2\2\u00f2\u00f3")
        buf.write("\5m\67\2\u00f3\u00f4\5\u0085C\2\u00f4\u00f5\5\u0083B\2")
        buf.write("\u00f5\u00f6\5\u008fH\2\u00f6\u00f7\5y=\2\u00f7\u00f8")
        buf.write("\5\u0083B\2\u00f8\u00f9\5\u0091I\2\u00f9\u00fa\5q9\2\u00fa")
        buf.write("\60\3\2\2\2\u00fb\u00fc\5s:\2\u00fc\u00fd\5\u0085C\2\u00fd")
        buf.write("\u00fe\5\u008bF\2\u00fe\62\3\2\2\2\u00ff\u0100\5\u008f")
        buf.write("H\2\u0100\u0101\5\u0085C\2\u0101\64\3\2\2\2\u0102\u0103")
        buf.write("\5o8\2\u0103\u0104\5\u0085C\2\u0104\u0105\5\u0095K\2\u0105")
        buf.write("\u0106\5\u0083B\2\u0106\u0107\5\u008fH\2\u0107\u0108\5")
        buf.write("\u0085C\2\u0108\66\3\2\2\2\u0109\u010a\5o8\2\u010a\u010b")
        buf.write("\5\u0085C\2\u010b8\3\2\2\2\u010c\u010d\5y=\2\u010d\u010e")
        buf.write("\5s:\2\u010e:\3\2\2\2\u010f\u0110\5\u008fH\2\u0110\u0111")
        buf.write("\5w<\2\u0111\u0112\5q9\2\u0112\u0113\5\u0083B\2\u0113")
        buf.write("<\3\2\2\2\u0114\u0115\5q9\2\u0115\u0116\5\177@\2\u0116")
        buf.write("\u0117\5\u008dG\2\u0117\u0118\5q9\2\u0118>\3\2\2\2\u0119")
        buf.write("\u011a\5\u008bF\2\u011a\u011b\5q9\2\u011b\u011c\5\u008f")
        buf.write("H\2\u011c\u011d\5\u0091I\2\u011d\u011e\5\u008bF\2\u011e")
        buf.write("\u011f\5\u0083B\2\u011f@\3\2\2\2\u0120\u0121\5\u0095K")
        buf.write("\2\u0121\u0122\5w<\2\u0122\u0123\5y=\2\u0123\u0124\5\177")
        buf.write("@\2\u0124\u0125\5q9\2\u0125B\3\2\2\2\u0126\u0127\5k\66")
        buf.write("\2\u0127\u0128\5q9\2\u0128\u0129\5u;\2\u0129\u012a\5y")
        buf.write("=\2\u012a\u012b\5\u0083B\2\u012bD\3\2\2\2\u012c\u012d")
        buf.write("\5q9\2\u012d\u012e\5\u0083B\2\u012e\u012f\5o8\2\u012f")
        buf.write("F\3\2\2\2\u0130\u0131\5s:\2\u0131\u0132\5\u0091I\2\u0132")
        buf.write("\u0133\5\u0083B\2\u0133\u0134\5m\67\2\u0134\u0135\5\u008f")
        buf.write("H\2\u0135\u0136\5y=\2\u0136\u0137\5\u0085C\2\u0137\u0138")
        buf.write("\5\u0083B\2\u0138H\3\2\2\2\u0139\u013a\5\u0087D\2\u013a")
        buf.write("\u013b\5\u008bF\2\u013b\u013c\5\u0085C\2\u013c\u013d\5")
        buf.write("m\67\2\u013d\u013e\5q9\2\u013e\u013f\5o8\2\u013f\u0140")
        buf.write("\5\u0091I\2\u0140\u0141\5\u008bF\2\u0141\u0142\5q9\2\u0142")
        buf.write("J\3\2\2\2\u0143\u0144\5\u0093J\2\u0144\u0145\5i\65\2\u0145")
        buf.write("\u0146\5\u008bF\2\u0146L\3\2\2\2\u0147\u0148\5\u008fH")
        buf.write("\2\u0148\u0149\5\u008bF\2\u0149\u014a\5\u0091I\2\u014a")
        buf.write("\u014b\5q9\2\u014bN\3\2\2\2\u014c\u014d\5s:\2\u014d\u014e")
        buf.write("\5i\65\2\u014e\u014f\5\177@\2\u014f\u0150\5\u008dG\2\u0150")
        buf.write("\u0151\5q9\2\u0151P\3\2\2\2\u0152\u0153\5i\65\2\u0153")
        buf.write("\u0154\5\u008bF\2\u0154\u0155\5\u008bF\2\u0155\u0156\5")
        buf.write("i\65\2\u0156\u0157\5\u0099M\2\u0157R\3\2\2\2\u0158\u0159")
        buf.write("\5\u0085C\2\u0159\u015a\5s:\2\u015aT\3\2\2\2\u015b\u015c")
        buf.write("\5\u008bF\2\u015c\u015d\5q9\2\u015d\u015e\5i\65\2\u015e")
        buf.write("\u015f\5\177@\2\u015fV\3\2\2\2\u0160\u0161\5k\66\2\u0161")
        buf.write("\u0162\5\u0085C\2\u0162\u0163\5\u0085C\2\u0163\u0164\5")
        buf.write("\177@\2\u0164\u0165\5q9\2\u0165\u0166\5i\65\2\u0166\u0167")
        buf.write("\5\u0083B\2\u0167\u016e\3\2\2\2\u0168\u0169\5k\66\2\u0169")
        buf.write("\u016a\5\u0085C\2\u016a\u016b\5\u0085C\2\u016b\u016c\5")
        buf.write("\177@\2\u016c\u016e\3\2\2\2\u016d\u0160\3\2\2\2\u016d")
        buf.write("\u0168\3\2\2\2\u016eX\3\2\2\2\u016f\u0170\5y=\2\u0170")
        buf.write("\u0171\5\u0083B\2\u0171\u0172\5\u008fH\2\u0172\u0173\5")
        buf.write("q9\2\u0173\u0174\5u;\2\u0174\u0175\5q9\2\u0175\u0176\5")
        buf.write("\u008bF\2\u0176\u017c\3\2\2\2\u0177\u0178\5y=\2\u0178")
        buf.write("\u0179\5\u0083B\2\u0179\u017a\5\u008fH\2\u017a\u017c\3")
        buf.write("\2\2\2\u017b\u016f\3\2\2\2\u017b\u0177\3\2\2\2\u017cZ")
        buf.write("\3\2\2\2\u017d\u017e\5\u008dG\2\u017e\u017f\5\u008fH\2")
        buf.write("\u017f\u0180\5\u008bF\2\u0180\u0181\5y=\2\u0181\u0182")
        buf.write("\5\u0083B\2\u0182\u0183\5u;\2\u0183\\\3\2\2\2\u0184\u0185")
        buf.write("\5\u0083B\2\u0185\u0186\5\u0085C\2\u0186\u0187\5\u008f")
        buf.write("H\2\u0187^\3\2\2\2\u0188\u0189\5i\65\2\u0189\u018a\5\u0083")
        buf.write("B\2\u018a\u018b\5o8\2\u018b`\3\2\2\2\u018c\u018d\5\u0085")
        buf.write("C\2\u018d\u018e\5\u008bF\2\u018eb\3\2\2\2\u018f\u0190")
        buf.write("\5o8\2\u0190\u0191\5y=\2\u0191\u0192\5\u0093J\2\u0192")
        buf.write("d\3\2\2\2\u0193\u0194\5\u0081A\2\u0194\u0195\5\u0085C")
        buf.write("\2\u0195\u0196\5o8\2\u0196f\3\2\2\2\u0197\u0198\5\u0081")
        buf.write("A\2\u0198\u0199\5i\65\2\u0199\u019a\5y=\2\u019a\u019b")
        buf.write("\5\u0083B\2\u019bh\3\2\2\2\u019c\u019d\t\2\2\2\u019dj")
        buf.write("\3\2\2\2\u019e\u019f\t\3\2\2\u019fl\3\2\2\2\u01a0\u01a1")
        buf.write("\t\4\2\2\u01a1n\3\2\2\2\u01a2\u01a3\t\5\2\2\u01a3p\3\2")
        buf.write("\2\2\u01a4\u01a5\t\6\2\2\u01a5r\3\2\2\2\u01a6\u01a7\t")
        buf.write("\7\2\2\u01a7t\3\2\2\2\u01a8\u01a9\t\b\2\2\u01a9v\3\2\2")
        buf.write("\2\u01aa\u01ab\t\t\2\2\u01abx\3\2\2\2\u01ac\u01ad\t\n")
        buf.write("\2\2\u01adz\3\2\2\2\u01ae\u01af\t\13\2\2\u01af|\3\2\2")
        buf.write("\2\u01b0\u01b1\t\f\2\2\u01b1~\3\2\2\2\u01b2\u01b3\t\r")
        buf.write("\2\2\u01b3\u0080\3\2\2\2\u01b4\u01b5\t\16\2\2\u01b5\u0082")
        buf.write("\3\2\2\2\u01b6\u01b7\t\17\2\2\u01b7\u0084\3\2\2\2\u01b8")
        buf.write("\u01b9\t\20\2\2\u01b9\u0086\3\2\2\2\u01ba\u01bb\t\21\2")
        buf.write("\2\u01bb\u0088\3\2\2\2\u01bc\u01bd\t\22\2\2\u01bd\u008a")
        buf.write("\3\2\2\2\u01be\u01bf\t\23\2\2\u01bf\u008c\3\2\2\2\u01c0")
        buf.write("\u01c1\t\24\2\2\u01c1\u008e\3\2\2\2\u01c2\u01c3\t\25\2")
        buf.write("\2\u01c3\u0090\3\2\2\2\u01c4\u01c5\t\26\2\2\u01c5\u0092")
        buf.write("\3\2\2\2\u01c6\u01c7\t\27\2\2\u01c7\u0094\3\2\2\2\u01c8")
        buf.write("\u01c9\t\30\2\2\u01c9\u0096\3\2\2\2\u01ca\u01cb\t\31\2")
        buf.write("\2\u01cb\u0098\3\2\2\2\u01cc\u01cd\t\32\2\2\u01cd\u009a")
        buf.write("\3\2\2\2\u01ce\u01cf\t\33\2\2\u01cf\u009c\3\2\2\2\u01d0")
        buf.write("\u01d1\t\34\2\2\u01d1\u009e\3\2\2\2\u01d2\u01d4\t\35\2")
        buf.write("\2\u01d3\u01d2\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5\u01d3")
        buf.write("\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7")
        buf.write("\u01d8\bP\2\2\u01d8\u00a0\3\2\2\2\u01d9\u01db\t\36\2\2")
        buf.write("\u01da\u01d9\3\2\2\2\u01db\u01df\3\2\2\2\u01dc\u01de\t")
        buf.write("\37\2\2\u01dd\u01dc\3\2\2\2\u01de\u01e1\3\2\2\2\u01df")
        buf.write("\u01dd\3\2\2\2\u01df\u01e0\3\2\2\2\u01e0\u00a2\3\2\2\2")
        buf.write("\u01e1\u01df\3\2\2\2\u01e2\u01e4\t\34\2\2\u01e3\u01e2")
        buf.write("\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e5")
        buf.write("\u01e6\3\2\2\2\u01e6\u00a4\3\2\2\2\u01e7\u01e9\t\34\2")
        buf.write("\2\u01e8\u01e7\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea\u01e8")
        buf.write("\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb\u01ed\3\2\2\2\u01ec")
        buf.write("\u01ee\7\60\2\2\u01ed\u01ec\3\2\2\2\u01ed\u01ee\3\2\2")
        buf.write("\2\u01ee\u01f2\3\2\2\2\u01ef\u01f1\t\34\2\2\u01f0\u01ef")
        buf.write("\3\2\2\2\u01f1\u01f4\3\2\2\2\u01f2\u01f0\3\2\2\2\u01f2")
        buf.write("\u01f3\3\2\2\2\u01f3\u0204\3\2\2\2\u01f4\u01f2\3\2\2\2")
        buf.write("\u01f5\u01f7\t\34\2\2\u01f6\u01f5\3\2\2\2\u01f7\u01fa")
        buf.write("\3\2\2\2\u01f8\u01f6\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9")
        buf.write("\u01fb\3\2\2\2\u01fa\u01f8\3\2\2\2\u01fb\u01fd\t\6\2\2")
        buf.write("\u01fc\u01fe\7/\2\2\u01fd\u01fc\3\2\2\2\u01fd\u01fe\3")
        buf.write("\2\2\2\u01fe\u0200\3\2\2\2\u01ff\u0201\t\34\2\2\u0200")
        buf.write("\u01ff\3\2\2\2\u0201\u0202\3\2\2\2\u0202\u0200\3\2\2\2")
        buf.write("\u0202\u0203\3\2\2\2\u0203\u0205\3\2\2\2\u0204\u01f8\3")
        buf.write("\2\2\2\u0204\u0205\3\2\2\2\u0205\u0220\3\2\2\2\u0206\u0208")
        buf.write("\t\34\2\2\u0207\u0206\3\2\2\2\u0208\u020b\3\2\2\2\u0209")
        buf.write("\u0207\3\2\2\2\u0209\u020a\3\2\2\2\u020a\u020d\3\2\2\2")
        buf.write("\u020b\u0209\3\2\2\2\u020c\u020e\7\60\2\2\u020d\u020c")
        buf.write("\3\2\2\2\u020d\u020e\3\2\2\2\u020e\u0210\3\2\2\2\u020f")
        buf.write("\u0211\t\34\2\2\u0210\u020f\3\2\2\2\u0211\u0212\3\2\2")
        buf.write("\2\u0212\u0210\3\2\2\2\u0212\u0213\3\2\2\2\u0213\u021d")
        buf.write("\3\2\2\2\u0214\u0216\t\6\2\2\u0215\u0217\7/\2\2\u0216")
        buf.write("\u0215\3\2\2\2\u0216\u0217\3\2\2\2\u0217\u0219\3\2\2\2")
        buf.write("\u0218\u021a\t\34\2\2\u0219\u0218\3\2\2\2\u021a\u021b")
        buf.write("\3\2\2\2\u021b\u0219\3\2\2\2\u021b\u021c\3\2\2\2\u021c")
        buf.write("\u021e\3\2\2\2\u021d\u0214\3\2\2\2\u021d\u021e\3\2\2\2")
        buf.write("\u021e\u0220\3\2\2\2\u021f\u01e8\3\2\2\2\u021f\u0209\3")
        buf.write("\2\2\2\u0220\u00a6\3\2\2\2\u0221\u0222\7v\2\2\u0222\u0223")
        buf.write("\7t\2\2\u0223\u0224\7w\2\2\u0224\u022b\7g\2\2\u0225\u0226")
        buf.write("\7h\2\2\u0226\u0227\7c\2\2\u0227\u0228\7n\2\2\u0228\u0229")
        buf.write("\7u\2\2\u0229\u022b\7g\2\2\u022a\u0221\3\2\2\2\u022a\u0225")
        buf.write("\3\2\2\2\u022b\u00a8\3\2\2\2\u022c\u0232\7$\2\2\u022d")
        buf.write("\u022e\7^\2\2\u022e\u0231\t \2\2\u022f\u0231\n!\2\2\u0230")
        buf.write("\u022d\3\2\2\2\u0230\u022f\3\2\2\2\u0231\u0234\3\2\2\2")
        buf.write("\u0232\u0230\3\2\2\2\u0232\u0233\3\2\2\2\u0233\u0235\3")
        buf.write("\2\2\2\u0234\u0232\3\2\2\2\u0235\u0236\7$\2\2\u0236\u0237")
        buf.write("\bU\3\2\u0237\u00aa\3\2\2\2\u0238\u023e\5W,\2\u0239\u023e")
        buf.write("\5Y-\2\u023a\u023e\5U+\2\u023b\u023e\5[.\2\u023c\u023e")
        buf.write("\5Q)\2\u023d\u0238\3\2\2\2\u023d\u0239\3\2\2\2\u023d\u023a")
        buf.write("\3\2\2\2\u023d\u023b\3\2\2\2\u023d\u023c\3\2\2\2\u023e")
        buf.write("\u00ac\3\2\2\2\u023f\u0242\5\u00afX\2\u0240\u0242\5\u00b5")
        buf.write("[\2\u0241\u023f\3\2\2\2\u0241\u0240\3\2\2\2\u0242\u0243")
        buf.write("\3\2\2\2\u0243\u0244\bW\2\2\u0244\u00ae\3\2\2\2\u0245")
        buf.write("\u0248\5\u00b1Y\2\u0246\u0248\5\u00b3Z\2\u0247\u0245\3")
        buf.write("\2\2\2\u0247\u0246\3\2\2\2\u0248\u00b0\3\2\2\2\u0249\u024a")
        buf.write("\7*\2\2\u024a\u024b\7,\2\2\u024b\u024f\3\2\2\2\u024c\u024e")
        buf.write("\13\2\2\2\u024d\u024c\3\2\2\2\u024e\u0251\3\2\2\2\u024f")
        buf.write("\u0250\3\2\2\2\u024f\u024d\3\2\2\2\u0250\u0252\3\2\2\2")
        buf.write("\u0251\u024f\3\2\2\2\u0252\u0253\7,\2\2\u0253\u0254\7")
        buf.write("+\2\2\u0254\u00b2\3\2\2\2\u0255\u0259\7}\2\2\u0256\u0258")
        buf.write("\13\2\2\2\u0257\u0256\3\2\2\2\u0258\u025b\3\2\2\2\u0259")
        buf.write("\u025a\3\2\2\2\u0259\u0257\3\2\2\2\u025a\u025c\3\2\2\2")
        buf.write("\u025b\u0259\3\2\2\2\u025c\u025d\7\177\2\2\u025d\u00b4")
        buf.write("\3\2\2\2\u025e\u025f\7\61\2\2\u025f\u0260\7\61\2\2\u0260")
        buf.write("\u0264\3\2\2\2\u0261\u0263\n\"\2\2\u0262\u0261\3\2\2\2")
        buf.write("\u0263\u0266\3\2\2\2\u0264\u0262\3\2\2\2\u0264\u0265\3")
        buf.write("\2\2\2\u0265\u00b6\3\2\2\2\u0266\u0264\3\2\2\2\u0267\u026f")
        buf.write("\7$\2\2\u0268\u026a\7^\2\2\u0269\u026b\t \2\2\u026a\u0269")
        buf.write("\3\2\2\2\u026b\u026e\3\2\2\2\u026c\u026e\n!\2\2\u026d")
        buf.write("\u0268\3\2\2\2\u026d\u026c\3\2\2\2\u026e\u0271\3\2\2\2")
        buf.write("\u026f\u026d\3\2\2\2\u026f\u0270\3\2\2\2\u0270\u0272\3")
        buf.write("\2\2\2\u0271\u026f\3\2\2\2\u0272\u0273\b\\\4\2\u0273\u00b8")
        buf.write("\3\2\2\2\u0274\u027a\7$\2\2\u0275\u0279\n#\2\2\u0276\u0277")
        buf.write("\7^\2\2\u0277\u0279\t \2\2\u0278\u0275\3\2\2\2\u0278\u0276")
        buf.write("\3\2\2\2\u0279\u027c\3\2\2\2\u027a\u0278\3\2\2\2\u027a")
        buf.write("\u027b\3\2\2\2\u027b\u027d\3\2\2\2\u027c\u027a\3\2\2\2")
        buf.write("\u027d\u027e\7^\2\2\u027e\u027f\n \2\2\u027f\u0280\b]")
        buf.write("\5\2\u0280\u00ba\3\2\2\2\u0281\u0282\13\2\2\2\u0282\u0283")
        buf.write("\b^\6\2\u0283\u00bc\3\2\2\2&\2\u016d\u017b\u01d5\u01da")
        buf.write("\u01dd\u01df\u01e5\u01ea\u01ed\u01f2\u01f8\u01fd\u0202")
        buf.write("\u0204\u0209\u020d\u0212\u0216\u021b\u021d\u021f\u022a")
        buf.write("\u0230\u0232\u023d\u0241\u0247\u024f\u0259\u0264\u026a")
        buf.write("\u026d\u026f\u0278\u027a\7\b\2\2\3U\2\3\\\3\3]\4\3^\5")
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
    WS = 52
    ID = 53
    INTLIT = 54
    REALLIT = 55
    BOOLLIT = 56
    STRINGLIT = 57
    TYPE = 58
    CMT = 59
    BLKCMT = 60
    TRACMT = 61
    BLCMT = 62
    LINECMT = 63
    UNCLOSE_STRING = 64
    ILLEGAL_ESCAPE = 65
    ERROR_CHAR = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "','", "'='", 
            "':'", "'..'", "'+'", "'*'", "'<>'", "'<'", "'<='", "'-'", "'/'", 
            "'>'", "'>='", "':='" ]

    symbolicNames = [ "<INVALID>",
            "LB", "RB", "LP", "RP", "LQ", "RQ", "SEMI", "CM", "EQ", "COL", 
            "DD", "ADD", "MUL", "NOTEQ", "LESSTN", "LESSEQ", "SUBNE", "DIVSI", 
            "GRETN", "GREEQ", "ASSI", "BREAK", "CONTINUE", "FOR", "TO", 
            "DOWNTO", "DO", "IF", "THEN", "ELSE", "RETURN", "WHILE", "BEGIN", 
            "END", "FUNCTION", "PROCEDURE", "VAR", "TRUE", "FALSE", "ARRAY", 
            "OF", "REAL", "BOOLEAN", "INTEGER", "STRING", "NOT", "AND", 
            "OR", "DIV", "MOD", "MAIN", "WS", "ID", "INTLIT", "REALLIT", 
            "BOOLLIT", "STRINGLIT", "TYPE", "CMT", "BLKCMT", "TRACMT", "BLCMT", 
            "LINECMT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "LB", "RB", "LP", "RP", "LQ", "RQ", "SEMI", "CM", "EQ", 
                  "COL", "DD", "ADD", "MUL", "NOTEQ", "LESSTN", "LESSEQ", 
                  "SUBNE", "DIVSI", "GRETN", "GREEQ", "ASSI", "BREAK", "CONTINUE", 
                  "FOR", "TO", "DOWNTO", "DO", "IF", "THEN", "ELSE", "RETURN", 
                  "WHILE", "BEGIN", "END", "FUNCTION", "PROCEDURE", "VAR", 
                  "TRUE", "FALSE", "ARRAY", "OF", "REAL", "BOOLEAN", "INTEGER", 
                  "STRING", "NOT", "AND", "OR", "DIV", "MOD", "MAIN", "A", 
                  "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", 
                  "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", 
                  "X", "Y", "Z", "NUM", "WS", "ID", "INTLIT", "REALLIT", 
                  "BOOLLIT", "STRINGLIT", "TYPE", "CMT", "BLKCMT", "TRACMT", 
                  "BLCMT", "LINECMT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_CHAR" ]

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
            actions[83] = self.STRINGLIT_action 
            actions[90] = self.UNCLOSE_STRING_action 
            actions[91] = self.ILLEGAL_ESCAPE_action 
            actions[92] = self.ERROR_CHAR_action 
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
     


