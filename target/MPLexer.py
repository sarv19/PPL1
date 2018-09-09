# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2E")
        buf.write("\u0291\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("^\t^\4_\t_\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7")
        buf.write("\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3")
        buf.write("%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'")
        buf.write("\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3")
        buf.write("+\3+\3+\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3")
        buf.write("-\3-\3-\5-\u0172\n-\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\5.\u0180\n.\3/\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60")
        buf.write("\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\63\3\63")
        buf.write("\3\64\3\64\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38")
        buf.write("\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3")
        buf.write("A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3")
        buf.write("J\3J\3K\3K\3L\3L\3M\3M\3N\3N\3O\3O\3P\6P\u01d3\nP\rP\16")
        buf.write("P\u01d4\3Q\5Q\u01d8\nQ\3Q\7Q\u01db\nQ\fQ\16Q\u01de\13")
        buf.write("Q\3R\6R\u01e1\nR\rR\16R\u01e2\3S\6S\u01e6\nS\rS\16S\u01e7")
        buf.write("\3S\5S\u01eb\nS\3S\7S\u01ee\nS\fS\16S\u01f1\13S\3S\6S")
        buf.write("\u01f4\nS\rS\16S\u01f5\3S\3S\5S\u01fa\nS\3S\6S\u01fd\n")
        buf.write("S\rS\16S\u01fe\5S\u0201\nS\3S\7S\u0204\nS\fS\16S\u0207")
        buf.write("\13S\3S\5S\u020a\nS\3S\6S\u020d\nS\rS\16S\u020e\3S\3S")
        buf.write("\5S\u0213\nS\3S\6S\u0216\nS\rS\16S\u0217\5S\u021a\nS\5")
        buf.write("S\u021c\nS\3T\3T\3T\3T\3T\3T\3T\3T\3T\5T\u0227\nT\3U\3")
        buf.write("U\3U\3U\7U\u022d\nU\fU\16U\u0230\13U\3U\3U\3V\3V\3V\3")
        buf.write("V\3V\5V\u0239\nV\3W\3W\5W\u023d\nW\3X\3X\5X\u0241\nX\3")
        buf.write("Y\3Y\3Y\3Y\7Y\u0247\nY\fY\16Y\u024a\13Y\3Y\3Y\3Y\3Y\3")
        buf.write("Y\3Z\3Z\7Z\u0253\nZ\fZ\16Z\u0256\13Z\3Z\3Z\3Z\3Z\3[\3")
        buf.write("[\3[\3[\7[\u0260\n[\f[\16[\u0263\13[\3\\\3\\\3]\3]\3]")
        buf.write("\3]\3]\7]\u026c\n]\f]\16]\u026f\13]\3^\3^\3^\3^\3^\7^")
        buf.write("\u0276\n^\f^\16^\u0279\13^\3^\6^\u027c\n^\r^\16^\u027d")
        buf.write("\3^\3^\3^\7^\u0283\n^\f^\16^\u0286\13^\3^\5^\u0289\n^")
        buf.write("\3_\6_\u028c\n_\r_\16_\u028d\3_\3_\4\u0248\u0254\2`\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\2k\2m\2o\2q\2s\2u")
        buf.write("\2w\2y\2{\2}\2\177\2\u0081\2\u0083\2\u0085\2\u0087\2\u0089")
        buf.write("\2\u008b\2\u008d\2\u008f\2\u0091\2\u0093\2\u0095\2\u0097")
        buf.write("\2\u0099\2\u009b\2\u009d\2\u009f\66\u00a1\67\u00a38\u00a5")
        buf.write("9\u00a7:\u00a9;\u00ab<\u00ad=\u00af>\u00b1?\u00b3@\u00b5")
        buf.write("A\u00b7B\u00b9C\u00bbD\u00bdE\3\2$\4\2CCcc\4\2DDdd\4\2")
        buf.write("EEee\4\2FFff\4\2GGgg\4\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4")
        buf.write("\2LLll\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRr")
        buf.write("r\4\2SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2")
        buf.write("YYyy\4\2ZZzz\4\2[[{{\4\2\\\\||\3\2\62;\5\2C\\aac|\6\2")
        buf.write("\62;C\\aac|\n\2$$))^^ddhhppttvv\7\2\n\f\16\17$$))^^\4")
        buf.write("\2\f\f\17\17\7\2\13\f\16\17$$))^^\5\2\13\f\17\17\"\"\2")
        buf.write("\u029d\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write("\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2")
        buf.write("\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2")
        buf.write("\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2")
        buf.write("\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3")
        buf.write("\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S")
        buf.write("\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2")
        buf.write("]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2")
        buf.write("\2g\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3")
        buf.write("\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2")
        buf.write("\2\u00ab\3\2\2\2\2\u00ad\3\2\2\2\2\u00af\3\2\2\2\2\u00b1")
        buf.write("\3\2\2\2\2\u00b3\3\2\2\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2")
        buf.write("\2\2\u00b9\3\2\2\2\2\u00bb\3\2\2\2\2\u00bd\3\2\2\2\3\u00bf")
        buf.write("\3\2\2\2\5\u00c1\3\2\2\2\7\u00c3\3\2\2\2\t\u00c5\3\2\2")
        buf.write("\2\13\u00c7\3\2\2\2\r\u00c9\3\2\2\2\17\u00cb\3\2\2\2\21")
        buf.write("\u00cd\3\2\2\2\23\u00cf\3\2\2\2\25\u00d1\3\2\2\2\27\u00d3")
        buf.write("\3\2\2\2\31\u00d6\3\2\2\2\33\u00d8\3\2\2\2\35\u00da\3")
        buf.write("\2\2\2\37\u00dd\3\2\2\2!\u00df\3\2\2\2#\u00e2\3\2\2\2")
        buf.write("%\u00e4\3\2\2\2\'\u00e6\3\2\2\2)\u00e8\3\2\2\2+\u00eb")
        buf.write("\3\2\2\2-\u00ed\3\2\2\2/\u00f0\3\2\2\2\61\u00f6\3\2\2")
        buf.write("\2\63\u00ff\3\2\2\2\65\u0103\3\2\2\2\67\u0106\3\2\2\2")
        buf.write("9\u010d\3\2\2\2;\u0110\3\2\2\2=\u0113\3\2\2\2?\u0118\3")
        buf.write("\2\2\2A\u011d\3\2\2\2C\u0124\3\2\2\2E\u012a\3\2\2\2G\u0130")
        buf.write("\3\2\2\2I\u0134\3\2\2\2K\u013d\3\2\2\2M\u0147\3\2\2\2")
        buf.write("O\u014b\3\2\2\2Q\u0150\3\2\2\2S\u0156\3\2\2\2U\u015c\3")
        buf.write("\2\2\2W\u015f\3\2\2\2Y\u0171\3\2\2\2[\u017f\3\2\2\2]\u0181")
        buf.write("\3\2\2\2_\u0188\3\2\2\2a\u018c\3\2\2\2c\u0190\3\2\2\2")
        buf.write("e\u0193\3\2\2\2g\u0197\3\2\2\2i\u019b\3\2\2\2k\u019d\3")
        buf.write("\2\2\2m\u019f\3\2\2\2o\u01a1\3\2\2\2q\u01a3\3\2\2\2s\u01a5")
        buf.write("\3\2\2\2u\u01a7\3\2\2\2w\u01a9\3\2\2\2y\u01ab\3\2\2\2")
        buf.write("{\u01ad\3\2\2\2}\u01af\3\2\2\2\177\u01b1\3\2\2\2\u0081")
        buf.write("\u01b3\3\2\2\2\u0083\u01b5\3\2\2\2\u0085\u01b7\3\2\2\2")
        buf.write("\u0087\u01b9\3\2\2\2\u0089\u01bb\3\2\2\2\u008b\u01bd\3")
        buf.write("\2\2\2\u008d\u01bf\3\2\2\2\u008f\u01c1\3\2\2\2\u0091\u01c3")
        buf.write("\3\2\2\2\u0093\u01c5\3\2\2\2\u0095\u01c7\3\2\2\2\u0097")
        buf.write("\u01c9\3\2\2\2\u0099\u01cb\3\2\2\2\u009b\u01cd\3\2\2\2")
        buf.write("\u009d\u01cf\3\2\2\2\u009f\u01d2\3\2\2\2\u00a1\u01d7\3")
        buf.write("\2\2\2\u00a3\u01e0\3\2\2\2\u00a5\u021b\3\2\2\2\u00a7\u0226")
        buf.write("\3\2\2\2\u00a9\u0228\3\2\2\2\u00ab\u0238\3\2\2\2\u00ad")
        buf.write("\u023c\3\2\2\2\u00af\u0240\3\2\2\2\u00b1\u0242\3\2\2\2")
        buf.write("\u00b3\u0250\3\2\2\2\u00b5\u025b\3\2\2\2\u00b7\u0264\3")
        buf.write("\2\2\2\u00b9\u0266\3\2\2\2\u00bb\u0270\3\2\2\2\u00bd\u028b")
        buf.write("\3\2\2\2\u00bf\u00c0\7*\2\2\u00c0\4\3\2\2\2\u00c1\u00c2")
        buf.write("\7+\2\2\u00c2\6\3\2\2\2\u00c3\u00c4\7}\2\2\u00c4\b\3\2")
        buf.write("\2\2\u00c5\u00c6\7\177\2\2\u00c6\n\3\2\2\2\u00c7\u00c8")
        buf.write("\7]\2\2\u00c8\f\3\2\2\2\u00c9\u00ca\7_\2\2\u00ca\16\3")
        buf.write("\2\2\2\u00cb\u00cc\7=\2\2\u00cc\20\3\2\2\2\u00cd\u00ce")
        buf.write("\7.\2\2\u00ce\22\3\2\2\2\u00cf\u00d0\7?\2\2\u00d0\24\3")
        buf.write("\2\2\2\u00d1\u00d2\7<\2\2\u00d2\26\3\2\2\2\u00d3\u00d4")
        buf.write("\7\60\2\2\u00d4\u00d5\7\60\2\2\u00d5\30\3\2\2\2\u00d6")
        buf.write("\u00d7\7-\2\2\u00d7\32\3\2\2\2\u00d8\u00d9\7,\2\2\u00d9")
        buf.write("\34\3\2\2\2\u00da\u00db\7>\2\2\u00db\u00dc\7@\2\2\u00dc")
        buf.write("\36\3\2\2\2\u00dd\u00de\7>\2\2\u00de \3\2\2\2\u00df\u00e0")
        buf.write("\7>\2\2\u00e0\u00e1\7?\2\2\u00e1\"\3\2\2\2\u00e2\u00e3")
        buf.write("\7/\2\2\u00e3$\3\2\2\2\u00e4\u00e5\7\61\2\2\u00e5&\3\2")
        buf.write("\2\2\u00e6\u00e7\7@\2\2\u00e7(\3\2\2\2\u00e8\u00e9\7@")
        buf.write("\2\2\u00e9\u00ea\7?\2\2\u00ea*\3\2\2\2\u00eb\u00ec\7\"")
        buf.write("\2\2\u00ec,\3\2\2\2\u00ed\u00ee\7<\2\2\u00ee\u00ef\7?")
        buf.write("\2\2\u00ef.\3\2\2\2\u00f0\u00f1\5k\66\2\u00f1\u00f2\5")
        buf.write("\u008bF\2\u00f2\u00f3\5q9\2\u00f3\u00f4\5i\65\2\u00f4")
        buf.write("\u00f5\5}?\2\u00f5\60\3\2\2\2\u00f6\u00f7\5m\67\2\u00f7")
        buf.write("\u00f8\5\u0085C\2\u00f8\u00f9\5\u0083B\2\u00f9\u00fa\5")
        buf.write("\u008fH\2\u00fa\u00fb\5y=\2\u00fb\u00fc\5\u0083B\2\u00fc")
        buf.write("\u00fd\5\u0091I\2\u00fd\u00fe\5q9\2\u00fe\62\3\2\2\2\u00ff")
        buf.write("\u0100\5s:\2\u0100\u0101\5\u0085C\2\u0101\u0102\5\u008b")
        buf.write("F\2\u0102\64\3\2\2\2\u0103\u0104\5\u008fH\2\u0104\u0105")
        buf.write("\5\u0085C\2\u0105\66\3\2\2\2\u0106\u0107\5o8\2\u0107\u0108")
        buf.write("\5\u0085C\2\u0108\u0109\5\u0095K\2\u0109\u010a\5\u0083")
        buf.write("B\2\u010a\u010b\5\u008fH\2\u010b\u010c\5\u0085C\2\u010c")
        buf.write("8\3\2\2\2\u010d\u010e\5o8\2\u010e\u010f\5\u0085C\2\u010f")
        buf.write(":\3\2\2\2\u0110\u0111\5y=\2\u0111\u0112\5s:\2\u0112<\3")
        buf.write("\2\2\2\u0113\u0114\5\u008fH\2\u0114\u0115\5w<\2\u0115")
        buf.write("\u0116\5q9\2\u0116\u0117\5\u0083B\2\u0117>\3\2\2\2\u0118")
        buf.write("\u0119\5q9\2\u0119\u011a\5\177@\2\u011a\u011b\5\u008d")
        buf.write("G\2\u011b\u011c\5q9\2\u011c@\3\2\2\2\u011d\u011e\5\u008b")
        buf.write("F\2\u011e\u011f\5q9\2\u011f\u0120\5\u008fH\2\u0120\u0121")
        buf.write("\5\u0091I\2\u0121\u0122\5\u008bF\2\u0122\u0123\5\u0083")
        buf.write("B\2\u0123B\3\2\2\2\u0124\u0125\5\u0095K\2\u0125\u0126")
        buf.write("\5w<\2\u0126\u0127\5y=\2\u0127\u0128\5\177@\2\u0128\u0129")
        buf.write("\5q9\2\u0129D\3\2\2\2\u012a\u012b\5k\66\2\u012b\u012c")
        buf.write("\5q9\2\u012c\u012d\5u;\2\u012d\u012e\5y=\2\u012e\u012f")
        buf.write("\5\u0083B\2\u012fF\3\2\2\2\u0130\u0131\5q9\2\u0131\u0132")
        buf.write("\5\u0083B\2\u0132\u0133\5o8\2\u0133H\3\2\2\2\u0134\u0135")
        buf.write("\5s:\2\u0135\u0136\5\u0091I\2\u0136\u0137\5m\67\2\u0137")
        buf.write("\u0138\5\u0083B\2\u0138\u0139\5\u008fH\2\u0139\u013a\5")
        buf.write("y=\2\u013a\u013b\5\u0085C\2\u013b\u013c\5\u0083B\2\u013c")
        buf.write("J\3\2\2\2\u013d\u013e\5\u0087D\2\u013e\u013f\5\u008bF")
        buf.write("\2\u013f\u0140\5\u0085C\2\u0140\u0141\5m\67\2\u0141\u0142")
        buf.write("\5q9\2\u0142\u0143\5o8\2\u0143\u0144\5\u0091I\2\u0144")
        buf.write("\u0145\5\u008bF\2\u0145\u0146\5q9\2\u0146L\3\2\2\2\u0147")
        buf.write("\u0148\5\u0093J\2\u0148\u0149\5i\65\2\u0149\u014a\5\u008b")
        buf.write("F\2\u014aN\3\2\2\2\u014b\u014c\5\u008fH\2\u014c\u014d")
        buf.write("\5\u008bF\2\u014d\u014e\5\u0091I\2\u014e\u014f\5q9\2\u014f")
        buf.write("P\3\2\2\2\u0150\u0151\5s:\2\u0151\u0152\5i\65\2\u0152")
        buf.write("\u0153\5\177@\2\u0153\u0154\5\u008dG\2\u0154\u0155\5q")
        buf.write("9\2\u0155R\3\2\2\2\u0156\u0157\5i\65\2\u0157\u0158\5\u008b")
        buf.write("F\2\u0158\u0159\5\u008bF\2\u0159\u015a\5i\65\2\u015a\u015b")
        buf.write("\5\u0099M\2\u015bT\3\2\2\2\u015c\u015d\5\u0085C\2\u015d")
        buf.write("\u015e\5s:\2\u015eV\3\2\2\2\u015f\u0160\5\u008bF\2\u0160")
        buf.write("\u0161\5q9\2\u0161\u0162\5i\65\2\u0162\u0163\5\177@\2")
        buf.write("\u0163X\3\2\2\2\u0164\u0165\5k\66\2\u0165\u0166\5\u0085")
        buf.write("C\2\u0166\u0167\5\u0085C\2\u0167\u0168\5\177@\2\u0168")
        buf.write("\u0169\5q9\2\u0169\u016a\5i\65\2\u016a\u016b\5\u0083B")
        buf.write("\2\u016b\u0172\3\2\2\2\u016c\u016d\5k\66\2\u016d\u016e")
        buf.write("\5\u0085C\2\u016e\u016f\5\u0085C\2\u016f\u0170\5\177@")
        buf.write("\2\u0170\u0172\3\2\2\2\u0171\u0164\3\2\2\2\u0171\u016c")
        buf.write("\3\2\2\2\u0172Z\3\2\2\2\u0173\u0174\5y=\2\u0174\u0175")
        buf.write("\5\u0083B\2\u0175\u0176\5\u008fH\2\u0176\u0177\5q9\2\u0177")
        buf.write("\u0178\5u;\2\u0178\u0179\5q9\2\u0179\u017a\5\u008bF\2")
        buf.write("\u017a\u0180\3\2\2\2\u017b\u017c\5y=\2\u017c\u017d\5\u0083")
        buf.write("B\2\u017d\u017e\5\u008fH\2\u017e\u0180\3\2\2\2\u017f\u0173")
        buf.write("\3\2\2\2\u017f\u017b\3\2\2\2\u0180\\\3\2\2\2\u0181\u0182")
        buf.write("\5\u008dG\2\u0182\u0183\5\u008fH\2\u0183\u0184\5\u008b")
        buf.write("F\2\u0184\u0185\5y=\2\u0185\u0186\5\u0083B\2\u0186\u0187")
        buf.write("\5u;\2\u0187^\3\2\2\2\u0188\u0189\5\u0083B\2\u0189\u018a")
        buf.write("\5\u0085C\2\u018a\u018b\5\u008fH\2\u018b`\3\2\2\2\u018c")
        buf.write("\u018d\5i\65\2\u018d\u018e\5\u0083B\2\u018e\u018f\5o8")
        buf.write("\2\u018fb\3\2\2\2\u0190\u0191\5\u0085C\2\u0191\u0192\5")
        buf.write("\u008bF\2\u0192d\3\2\2\2\u0193\u0194\5o8\2\u0194\u0195")
        buf.write("\5y=\2\u0195\u0196\5\u0093J\2\u0196f\3\2\2\2\u0197\u0198")
        buf.write("\5\u0081A\2\u0198\u0199\5\u0085C\2\u0199\u019a\5o8\2\u019a")
        buf.write("h\3\2\2\2\u019b\u019c\t\2\2\2\u019cj\3\2\2\2\u019d\u019e")
        buf.write("\t\3\2\2\u019el\3\2\2\2\u019f\u01a0\t\4\2\2\u01a0n\3\2")
        buf.write("\2\2\u01a1\u01a2\t\5\2\2\u01a2p\3\2\2\2\u01a3\u01a4\t")
        buf.write("\6\2\2\u01a4r\3\2\2\2\u01a5\u01a6\t\7\2\2\u01a6t\3\2\2")
        buf.write("\2\u01a7\u01a8\t\b\2\2\u01a8v\3\2\2\2\u01a9\u01aa\t\t")
        buf.write("\2\2\u01aax\3\2\2\2\u01ab\u01ac\t\n\2\2\u01acz\3\2\2\2")
        buf.write("\u01ad\u01ae\t\13\2\2\u01ae|\3\2\2\2\u01af\u01b0\t\f\2")
        buf.write("\2\u01b0~\3\2\2\2\u01b1\u01b2\t\r\2\2\u01b2\u0080\3\2")
        buf.write("\2\2\u01b3\u01b4\t\16\2\2\u01b4\u0082\3\2\2\2\u01b5\u01b6")
        buf.write("\t\17\2\2\u01b6\u0084\3\2\2\2\u01b7\u01b8\t\20\2\2\u01b8")
        buf.write("\u0086\3\2\2\2\u01b9\u01ba\t\21\2\2\u01ba\u0088\3\2\2")
        buf.write("\2\u01bb\u01bc\t\22\2\2\u01bc\u008a\3\2\2\2\u01bd\u01be")
        buf.write("\t\23\2\2\u01be\u008c\3\2\2\2\u01bf\u01c0\t\24\2\2\u01c0")
        buf.write("\u008e\3\2\2\2\u01c1\u01c2\t\25\2\2\u01c2\u0090\3\2\2")
        buf.write("\2\u01c3\u01c4\t\26\2\2\u01c4\u0092\3\2\2\2\u01c5\u01c6")
        buf.write("\t\27\2\2\u01c6\u0094\3\2\2\2\u01c7\u01c8\t\30\2\2\u01c8")
        buf.write("\u0096\3\2\2\2\u01c9\u01ca\t\31\2\2\u01ca\u0098\3\2\2")
        buf.write("\2\u01cb\u01cc\t\32\2\2\u01cc\u009a\3\2\2\2\u01cd\u01ce")
        buf.write("\t\33\2\2\u01ce\u009c\3\2\2\2\u01cf\u01d0\t\34\2\2\u01d0")
        buf.write("\u009e\3\2\2\2\u01d1\u01d3\5\u009dO\2\u01d2\u01d1\3\2")
        buf.write("\2\2\u01d3\u01d4\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d4\u01d5")
        buf.write("\3\2\2\2\u01d5\u00a0\3\2\2\2\u01d6\u01d8\t\35\2\2\u01d7")
        buf.write("\u01d6\3\2\2\2\u01d8\u01dc\3\2\2\2\u01d9\u01db\t\36\2")
        buf.write("\2\u01da\u01d9\3\2\2\2\u01db\u01de\3\2\2\2\u01dc\u01da")
        buf.write("\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd\u00a2\3\2\2\2\u01de")
        buf.write("\u01dc\3\2\2\2\u01df\u01e1\t\34\2\2\u01e0\u01df\3\2\2")
        buf.write("\2\u01e1\u01e2\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e2\u01e3")
        buf.write("\3\2\2\2\u01e3\u00a4\3\2\2\2\u01e4\u01e6\t\34\2\2\u01e5")
        buf.write("\u01e4\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7\u01e5\3\2\2\2")
        buf.write("\u01e7\u01e8\3\2\2\2\u01e8\u01ea\3\2\2\2\u01e9\u01eb\7")
        buf.write("\60\2\2\u01ea\u01e9\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb")
        buf.write("\u01ef\3\2\2\2\u01ec\u01ee\t\34\2\2\u01ed\u01ec\3\2\2")
        buf.write("\2\u01ee\u01f1\3\2\2\2\u01ef\u01ed\3\2\2\2\u01ef\u01f0")
        buf.write("\3\2\2\2\u01f0\u0200\3\2\2\2\u01f1\u01ef\3\2\2\2\u01f2")
        buf.write("\u01f4\t\34\2\2\u01f3\u01f2\3\2\2\2\u01f4\u01f5\3\2\2")
        buf.write("\2\u01f5\u01f3\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6\u01f7")
        buf.write("\3\2\2\2\u01f7\u01f9\t\6\2\2\u01f8\u01fa\7/\2\2\u01f9")
        buf.write("\u01f8\3\2\2\2\u01f9\u01fa\3\2\2\2\u01fa\u01fc\3\2\2\2")
        buf.write("\u01fb\u01fd\t\34\2\2\u01fc\u01fb\3\2\2\2\u01fd\u01fe")
        buf.write("\3\2\2\2\u01fe\u01fc\3\2\2\2\u01fe\u01ff\3\2\2\2\u01ff")
        buf.write("\u0201\3\2\2\2\u0200\u01f3\3\2\2\2\u0200\u0201\3\2\2\2")
        buf.write("\u0201\u021c\3\2\2\2\u0202\u0204\t\34\2\2\u0203\u0202")
        buf.write("\3\2\2\2\u0204\u0207\3\2\2\2\u0205\u0203\3\2\2\2\u0205")
        buf.write("\u0206\3\2\2\2\u0206\u0209\3\2\2\2\u0207\u0205\3\2\2\2")
        buf.write("\u0208\u020a\7\60\2\2\u0209\u0208\3\2\2\2\u0209\u020a")
        buf.write("\3\2\2\2\u020a\u020c\3\2\2\2\u020b\u020d\t\34\2\2\u020c")
        buf.write("\u020b\3\2\2\2\u020d\u020e\3\2\2\2\u020e\u020c\3\2\2\2")
        buf.write("\u020e\u020f\3\2\2\2\u020f\u0219\3\2\2\2\u0210\u0212\t")
        buf.write("\6\2\2\u0211\u0213\7/\2\2\u0212\u0211\3\2\2\2\u0212\u0213")
        buf.write("\3\2\2\2\u0213\u0215\3\2\2\2\u0214\u0216\t\34\2\2\u0215")
        buf.write("\u0214\3\2\2\2\u0216\u0217\3\2\2\2\u0217\u0215\3\2\2\2")
        buf.write("\u0217\u0218\3\2\2\2\u0218\u021a\3\2\2\2\u0219\u0210\3")
        buf.write("\2\2\2\u0219\u021a\3\2\2\2\u021a\u021c\3\2\2\2\u021b\u01e5")
        buf.write("\3\2\2\2\u021b\u0205\3\2\2\2\u021c\u00a6\3\2\2\2\u021d")
        buf.write("\u021e\7v\2\2\u021e\u021f\7t\2\2\u021f\u0220\7w\2\2\u0220")
        buf.write("\u0227\7g\2\2\u0221\u0222\7h\2\2\u0222\u0223\7c\2\2\u0223")
        buf.write("\u0224\7n\2\2\u0224\u0225\7u\2\2\u0225\u0227\7g\2\2\u0226")
        buf.write("\u021d\3\2\2\2\u0226\u0221\3\2\2\2\u0227\u00a8\3\2\2\2")
        buf.write("\u0228\u022e\7$\2\2\u0229\u022a\7^\2\2\u022a\u022d\t\37")
        buf.write("\2\2\u022b\u022d\n \2\2\u022c\u0229\3\2\2\2\u022c\u022b")
        buf.write("\3\2\2\2\u022d\u0230\3\2\2\2\u022e\u022c\3\2\2\2\u022e")
        buf.write("\u022f\3\2\2\2\u022f\u0231\3\2\2\2\u0230\u022e\3\2\2\2")
        buf.write("\u0231\u0232\7$\2\2\u0232\u00aa\3\2\2\2\u0233\u0239\5")
        buf.write("Y-\2\u0234\u0239\5[.\2\u0235\u0239\5W,\2\u0236\u0239\5")
        buf.write("]/\2\u0237\u0239\5S*\2\u0238\u0233\3\2\2\2\u0238\u0234")
        buf.write("\3\2\2\2\u0238\u0235\3\2\2\2\u0238\u0236\3\2\2\2\u0238")
        buf.write("\u0237\3\2\2\2\u0239\u00ac\3\2\2\2\u023a\u023d\5\u00af")
        buf.write("X\2\u023b\u023d\5\u00b5[\2\u023c\u023a\3\2\2\2\u023c\u023b")
        buf.write("\3\2\2\2\u023d\u00ae\3\2\2\2\u023e\u0241\5\u00b1Y\2\u023f")
        buf.write("\u0241\5\u00b3Z\2\u0240\u023e\3\2\2\2\u0240\u023f\3\2")
        buf.write("\2\2\u0241\u00b0\3\2\2\2\u0242\u0243\7*\2\2\u0243\u0244")
        buf.write("\7,\2\2\u0244\u0248\3\2\2\2\u0245\u0247\13\2\2\2\u0246")
        buf.write("\u0245\3\2\2\2\u0247\u024a\3\2\2\2\u0248\u0249\3\2\2\2")
        buf.write("\u0248\u0246\3\2\2\2\u0249\u024b\3\2\2\2\u024a\u0248\3")
        buf.write("\2\2\2\u024b\u024c\7,\2\2\u024c\u024d\7+\2\2\u024d\u024e")
        buf.write("\3\2\2\2\u024e\u024f\bY\2\2\u024f\u00b2\3\2\2\2\u0250")
        buf.write("\u0254\7}\2\2\u0251\u0253\13\2\2\2\u0252\u0251\3\2\2\2")
        buf.write("\u0253\u0256\3\2\2\2\u0254\u0255\3\2\2\2\u0254\u0252\3")
        buf.write("\2\2\2\u0255\u0257\3\2\2\2\u0256\u0254\3\2\2\2\u0257\u0258")
        buf.write("\7\177\2\2\u0258\u0259\3\2\2\2\u0259\u025a\bZ\2\2\u025a")
        buf.write("\u00b4\3\2\2\2\u025b\u025c\7\61\2\2\u025c\u025d\7\61\2")
        buf.write("\2\u025d\u0261\3\2\2\2\u025e\u0260\n!\2\2\u025f\u025e")
        buf.write("\3\2\2\2\u0260\u0263\3\2\2\2\u0261\u025f\3\2\2\2\u0261")
        buf.write("\u0262\3\2\2\2\u0262\u00b6\3\2\2\2\u0263\u0261\3\2\2\2")
        buf.write("\u0264\u0265\13\2\2\2\u0265\u00b8\3\2\2\2\u0266\u0267")
        buf.write("\b]\3\2\u0267\u026d\7$\2\2\u0268\u0269\7^\2\2\u0269\u026c")
        buf.write("\t\37\2\2\u026a\u026c\n\"\2\2\u026b\u0268\3\2\2\2\u026b")
        buf.write("\u026a\3\2\2\2\u026c\u026f\3\2\2\2\u026d\u026b\3\2\2\2")
        buf.write("\u026d\u026e\3\2\2\2\u026e\u00ba\3\2\2\2\u026f\u026d\3")
        buf.write("\2\2\2\u0270\u0271\b^\4\2\u0271\u0277\7$\2\2\u0272\u0273")
        buf.write("\7^\2\2\u0273\u0276\t\37\2\2\u0274\u0276\n \2\2\u0275")
        buf.write("\u0272\3\2\2\2\u0275\u0274\3\2\2\2\u0276\u0279\3\2\2\2")
        buf.write("\u0277\u0275\3\2\2\2\u0277\u0278\3\2\2\2\u0278\u027b\3")
        buf.write("\2\2\2\u0279\u0277\3\2\2\2\u027a\u027c\t\"\2\2\u027b\u027a")
        buf.write("\3\2\2\2\u027c\u027d\3\2\2\2\u027d\u027b\3\2\2\2\u027d")
        buf.write("\u027e\3\2\2\2\u027e\u0284\3\2\2\2\u027f\u0280\7^\2\2")
        buf.write("\u0280\u0283\t\37\2\2\u0281\u0283\n \2\2\u0282\u027f\3")
        buf.write("\2\2\2\u0282\u0281\3\2\2\2\u0283\u0286\3\2\2\2\u0284\u0282")
        buf.write("\3\2\2\2\u0284\u0285\3\2\2\2\u0285\u0288\3\2\2\2\u0286")
        buf.write("\u0284\3\2\2\2\u0287\u0289\7$\2\2\u0288\u0287\3\2\2\2")
        buf.write("\u0288\u0289\3\2\2\2\u0289\u00bc\3\2\2\2\u028a\u028c\t")
        buf.write("#\2\2\u028b\u028a\3\2\2\2\u028c\u028d\3\2\2\2\u028d\u028b")
        buf.write("\3\2\2\2\u028d\u028e\3\2\2\2\u028e\u028f\3\2\2\2\u028f")
        buf.write("\u0290\b_\2\2\u0290\u00be\3\2\2\2*\2\u0171\u017f\u01d4")
        buf.write("\u01d7\u01da\u01dc\u01e2\u01e7\u01ea\u01ef\u01f5\u01f9")
        buf.write("\u01fe\u0200\u0205\u0209\u020e\u0212\u0217\u0219\u021b")
        buf.write("\u0226\u022c\u022e\u0238\u023c\u0240\u0248\u0254\u0261")
        buf.write("\u026b\u026d\u0275\u0277\u027d\u0282\u0284\u0288\u028d")
        buf.write("\5\b\2\2\3]\2\3^\3")
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
    ASSI = 22
    BREAK = 23
    CONTINUE = 24
    FOR = 25
    TO = 26
    DOWNTO = 27
    DO = 28
    IF = 29
    THEN = 30
    ELSE = 31
    RETURN = 32
    WHILE = 33
    BEGIN = 34
    END = 35
    FUNCTION = 36
    PROCEDURE = 37
    VAR = 38
    TRUE = 39
    FALSE = 40
    ARRAY = 41
    OF = 42
    REAL = 43
    BOOLEAN = 44
    INTEGER = 45
    STRING = 46
    NOT = 47
    AND = 48
    OR = 49
    DIV = 50
    MOD = 51
    ManyNum = 52
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
    ERROR_CHAR = 64
    UNCLOSE_STRING = 65
    ILLEGAL_ESCAPE = 66
    WS = 67

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "','", "'='", 
            "':'", "'..'", "'+'", "'*'", "'<>'", "'<'", "'<='", "'-'", "'/'", 
            "'>'", "'>='", "' '", "':='" ]

    symbolicNames = [ "<INVALID>",
            "LB", "RB", "LP", "RP", "LQ", "RQ", "SEMI", "CM", "EQ", "COL", 
            "DD", "ADD", "MUL", "NOTEQ", "LESSTN", "LESSEQ", "SUBNE", "DIVSI", 
            "GRETN", "GREEQ", "SP", "ASSI", "BREAK", "CONTINUE", "FOR", 
            "TO", "DOWNTO", "DO", "IF", "THEN", "ELSE", "RETURN", "WHILE", 
            "BEGIN", "END", "FUNCTION", "PROCEDURE", "VAR", "TRUE", "FALSE", 
            "ARRAY", "OF", "REAL", "BOOLEAN", "INTEGER", "STRING", "NOT", 
            "AND", "OR", "DIV", "MOD", "ManyNum", "ID", "INTLIT", "REALLIT", 
            "BOOLLIT", "STRINGLIT", "TYPE", "CMT", "BLKCMT", "TRACMT", "BLCMT", 
            "LINECMT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "WS" ]

    ruleNames = [ "LB", "RB", "LP", "RP", "LQ", "RQ", "SEMI", "CM", "EQ", 
                  "COL", "DD", "ADD", "MUL", "NOTEQ", "LESSTN", "LESSEQ", 
                  "SUBNE", "DIVSI", "GRETN", "GREEQ", "SP", "ASSI", "BREAK", 
                  "CONTINUE", "FOR", "TO", "DOWNTO", "DO", "IF", "THEN", 
                  "ELSE", "RETURN", "WHILE", "BEGIN", "END", "FUNCTION", 
                  "PROCEDURE", "VAR", "TRUE", "FALSE", "ARRAY", "OF", "REAL", 
                  "BOOLEAN", "INTEGER", "STRING", "NOT", "AND", "OR", "DIV", 
                  "MOD", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", 
                  "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", 
                  "V", "W", "X", "Y", "Z", "NUM", "ManyNum", "ID", "INTLIT", 
                  "REALLIT", "BOOLLIT", "STRINGLIT", "TYPE", "CMT", "BLKCMT", 
                  "TRACMT", "BLCMT", "LINECMT", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "WS" ]

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
            actions[91] = self.UNCLOSE_STRING_action 
            actions[92] = self.ILLEGAL_ESCAPE_action 
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
     


