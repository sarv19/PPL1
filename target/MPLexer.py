# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2H")
        buf.write("\u02b2\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\3\25\3\25\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3")
        buf.write("%\3%\3%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3")
        buf.write("&\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3*")
        buf.write("\3*\3*\3*\3*\3*\3+\3+\3+\3,\3,\3,\3,\3,\3-\3-\3-\3-\3")
        buf.write("-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u0178\n-\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\3.\3.\3.\3.\3.\5.\u0186\n.\3/\3/\3/\3/\3/\3/\3/\3")
        buf.write("\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\62\3\62\3\62")
        buf.write("\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\65\3\65\3\65")
        buf.write("\3\65\3\66\3\66\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:")
        buf.write("\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3")
        buf.write("C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3J\3J\3K\3K\3L\3")
        buf.write("L\3M\3M\3N\3N\3O\3O\3P\3P\3Q\3Q\3R\6R\u01e1\nR\rR\16R")
        buf.write("\u01e2\3S\5S\u01e6\nS\3S\7S\u01e9\nS\fS\16S\u01ec\13S")
        buf.write("\3T\6T\u01ef\nT\rT\16T\u01f0\3U\6U\u01f4\nU\rU\16U\u01f5")
        buf.write("\3U\5U\u01f9\nU\3U\7U\u01fc\nU\fU\16U\u01ff\13U\3U\6U")
        buf.write("\u0202\nU\rU\16U\u0203\3U\3U\5U\u0208\nU\3U\6U\u020b\n")
        buf.write("U\rU\16U\u020c\5U\u020f\nU\3U\7U\u0212\nU\fU\16U\u0215")
        buf.write("\13U\3U\5U\u0218\nU\3U\6U\u021b\nU\rU\16U\u021c\3U\3U")
        buf.write("\5U\u0221\nU\3U\6U\u0224\nU\rU\16U\u0225\5U\u0228\nU\5")
        buf.write("U\u022a\nU\3V\3V\3V\3V\3V\3V\3V\3V\3V\5V\u0235\nV\3W\3")
        buf.write("W\3W\3W\7W\u023b\nW\fW\16W\u023e\13W\3W\3W\3W\3X\3X\3")
        buf.write("X\3X\3X\5X\u0248\nX\3Y\3Y\5Y\u024c\nY\3Y\3Y\3Z\3Z\5Z\u0252")
        buf.write("\nZ\3[\3[\3[\3[\7[\u0258\n[\f[\16[\u025b\13[\3[\3[\3[")
        buf.write("\3\\\3\\\7\\\u0262\n\\\f\\\16\\\u0265\13\\\3\\\3\\\3]")
        buf.write("\3]\3]\3]\7]\u026d\n]\f]\16]\u0270\13]\3^\3^\3^\3^\7^")
        buf.write("\u0276\n^\f^\16^\u0279\13^\3^\3^\3_\3_\3_\3_\7_\u0281")
        buf.write("\n_\f_\16_\u0284\13_\3_\6_\u0287\n_\r_\16_\u0288\3_\7")
        buf.write("_\u028c\n_\f_\16_\u028f\13_\3_\3_\3_\3`\3`\3`\3`\7`\u0298")
        buf.write("\n`\f`\16`\u029b\13`\3`\6`\u029e\n`\r`\16`\u029f\3`\7")
        buf.write("`\u02a3\n`\f`\16`\u02a6\13`\3`\3`\3a\3a\3b\6b\u02ad\n")
        buf.write("b\rb\16b\u02ae\3b\3b\5\u0259\u0263\u028d\2c\3\3\5\4\7")
        buf.write("\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m\2o\2q\2s\2u\2w\2")
        buf.write("y\2{\2}\2\177\2\u0081\2\u0083\2\u0085\2\u0087\2\u0089")
        buf.write("\2\u008b\2\u008d\2\u008f\2\u0091\2\u0093\2\u0095\2\u0097")
        buf.write("\2\u0099\2\u009b\2\u009d\2\u009f\2\u00a1\2\u00a38\u00a5")
        buf.write("9\u00a7:\u00a9;\u00ab<\u00ad=\u00af>\u00b1?\u00b3@\u00b5")
        buf.write("A\u00b7B\u00b9C\u00bbD\u00bdE\u00bfF\u00c1G\u00c3H\3\2")
        buf.write("%\4\2CCcc\4\2DDdd\4\2EEee\4\2FFff\4\2GGgg\4\2HHhh\4\2")
        buf.write("IIii\4\2JJjj\4\2KKkk\4\2LLll\4\2MMmm\4\2NNnn\4\2OOoo\4")
        buf.write("\2PPpp\4\2QQqq\4\2RRrr\4\2SSss\4\2TTtt\4\2UUuu\4\2VVv")
        buf.write("v\4\2WWww\4\2XXxx\4\2YYyy\4\2ZZzz\4\2[[{{\4\2\\\\||\3")
        buf.write("\2\62;\5\2C\\aac|\6\2\62;C\\aac|\n\2$$))^^ddhhppttvv\7")
        buf.write("\2\n\f\16\17$$))^^\4\2\f\f\17\17\7\2\13\f\16\17$$))^^")
        buf.write("\3\2$$\5\2\13\f\17\17\"\"\2\u02c0\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37")
        buf.write("\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2")
        buf.write("\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2")
        buf.write("\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2")
        buf.write("\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2")
        buf.write("\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2")
        buf.write("\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3")
        buf.write("\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a")
        buf.write("\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2")
        buf.write("k\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2")
        buf.write("\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2\2\2")
        buf.write("\u00af\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2\2\2\u00b5")
        buf.write("\3\2\2\2\2\u00b7\3\2\2\2\2\u00b9\3\2\2\2\2\u00bb\3\2\2")
        buf.write("\2\2\u00bd\3\2\2\2\2\u00bf\3\2\2\2\2\u00c1\3\2\2\2\2\u00c3")
        buf.write("\3\2\2\2\3\u00c5\3\2\2\2\5\u00c7\3\2\2\2\7\u00c9\3\2\2")
        buf.write("\2\t\u00cb\3\2\2\2\13\u00cd\3\2\2\2\r\u00cf\3\2\2\2\17")
        buf.write("\u00d1\3\2\2\2\21\u00d3\3\2\2\2\23\u00d5\3\2\2\2\25\u00d7")
        buf.write("\3\2\2\2\27\u00d9\3\2\2\2\31\u00dc\3\2\2\2\33\u00de\3")
        buf.write("\2\2\2\35\u00e0\3\2\2\2\37\u00e3\3\2\2\2!\u00e5\3\2\2")
        buf.write("\2#\u00e8\3\2\2\2%\u00ea\3\2\2\2\'\u00ec\3\2\2\2)\u00ee")
        buf.write("\3\2\2\2+\u00f1\3\2\2\2-\u00f3\3\2\2\2/\u00f6\3\2\2\2")
        buf.write("\61\u00fc\3\2\2\2\63\u0105\3\2\2\2\65\u0109\3\2\2\2\67")
        buf.write("\u010c\3\2\2\29\u0113\3\2\2\2;\u0116\3\2\2\2=\u0119\3")
        buf.write("\2\2\2?\u011e\3\2\2\2A\u0123\3\2\2\2C\u012a\3\2\2\2E\u0130")
        buf.write("\3\2\2\2G\u0136\3\2\2\2I\u013a\3\2\2\2K\u0143\3\2\2\2")
        buf.write("M\u014d\3\2\2\2O\u0151\3\2\2\2Q\u0156\3\2\2\2S\u015c\3")
        buf.write("\2\2\2U\u0162\3\2\2\2W\u0165\3\2\2\2Y\u0177\3\2\2\2[\u0185")
        buf.write("\3\2\2\2]\u0187\3\2\2\2_\u018e\3\2\2\2a\u0192\3\2\2\2")
        buf.write("c\u0196\3\2\2\2e\u0199\3\2\2\2g\u019d\3\2\2\2i\u01a1\3")
        buf.write("\2\2\2k\u01a5\3\2\2\2m\u01a9\3\2\2\2o\u01ab\3\2\2\2q\u01ad")
        buf.write("\3\2\2\2s\u01af\3\2\2\2u\u01b1\3\2\2\2w\u01b3\3\2\2\2")
        buf.write("y\u01b5\3\2\2\2{\u01b7\3\2\2\2}\u01b9\3\2\2\2\177\u01bb")
        buf.write("\3\2\2\2\u0081\u01bd\3\2\2\2\u0083\u01bf\3\2\2\2\u0085")
        buf.write("\u01c1\3\2\2\2\u0087\u01c3\3\2\2\2\u0089\u01c5\3\2\2\2")
        buf.write("\u008b\u01c7\3\2\2\2\u008d\u01c9\3\2\2\2\u008f\u01cb\3")
        buf.write("\2\2\2\u0091\u01cd\3\2\2\2\u0093\u01cf\3\2\2\2\u0095\u01d1")
        buf.write("\3\2\2\2\u0097\u01d3\3\2\2\2\u0099\u01d5\3\2\2\2\u009b")
        buf.write("\u01d7\3\2\2\2\u009d\u01d9\3\2\2\2\u009f\u01db\3\2\2\2")
        buf.write("\u00a1\u01dd\3\2\2\2\u00a3\u01e0\3\2\2\2\u00a5\u01e5\3")
        buf.write("\2\2\2\u00a7\u01ee\3\2\2\2\u00a9\u0229\3\2\2\2\u00ab\u0234")
        buf.write("\3\2\2\2\u00ad\u0236\3\2\2\2\u00af\u0247\3\2\2\2\u00b1")
        buf.write("\u024b\3\2\2\2\u00b3\u0251\3\2\2\2\u00b5\u0253\3\2\2\2")
        buf.write("\u00b7\u025f\3\2\2\2\u00b9\u0268\3\2\2\2\u00bb\u0271\3")
        buf.write("\2\2\2\u00bd\u027c\3\2\2\2\u00bf\u0293\3\2\2\2\u00c1\u02a9")
        buf.write("\3\2\2\2\u00c3\u02ac\3\2\2\2\u00c5\u00c6\7*\2\2\u00c6")
        buf.write("\4\3\2\2\2\u00c7\u00c8\7+\2\2\u00c8\6\3\2\2\2\u00c9\u00ca")
        buf.write("\7}\2\2\u00ca\b\3\2\2\2\u00cb\u00cc\7\177\2\2\u00cc\n")
        buf.write("\3\2\2\2\u00cd\u00ce\7]\2\2\u00ce\f\3\2\2\2\u00cf\u00d0")
        buf.write("\7_\2\2\u00d0\16\3\2\2\2\u00d1\u00d2\7=\2\2\u00d2\20\3")
        buf.write("\2\2\2\u00d3\u00d4\7.\2\2\u00d4\22\3\2\2\2\u00d5\u00d6")
        buf.write("\7?\2\2\u00d6\24\3\2\2\2\u00d7\u00d8\7<\2\2\u00d8\26\3")
        buf.write("\2\2\2\u00d9\u00da\7\60\2\2\u00da\u00db\7\60\2\2\u00db")
        buf.write("\30\3\2\2\2\u00dc\u00dd\7-\2\2\u00dd\32\3\2\2\2\u00de")
        buf.write("\u00df\7,\2\2\u00df\34\3\2\2\2\u00e0\u00e1\7>\2\2\u00e1")
        buf.write("\u00e2\7@\2\2\u00e2\36\3\2\2\2\u00e3\u00e4\7>\2\2\u00e4")
        buf.write(" \3\2\2\2\u00e5\u00e6\7>\2\2\u00e6\u00e7\7?\2\2\u00e7")
        buf.write("\"\3\2\2\2\u00e8\u00e9\7/\2\2\u00e9$\3\2\2\2\u00ea\u00eb")
        buf.write("\7\61\2\2\u00eb&\3\2\2\2\u00ec\u00ed\7@\2\2\u00ed(\3\2")
        buf.write("\2\2\u00ee\u00ef\7@\2\2\u00ef\u00f0\7?\2\2\u00f0*\3\2")
        buf.write("\2\2\u00f1\u00f2\7\"\2\2\u00f2,\3\2\2\2\u00f3\u00f4\7")
        buf.write("<\2\2\u00f4\u00f5\7?\2\2\u00f5.\3\2\2\2\u00f6\u00f7\5")
        buf.write("o8\2\u00f7\u00f8\5\u008fH\2\u00f8\u00f9\5u;\2\u00f9\u00fa")
        buf.write("\5m\67\2\u00fa\u00fb\5\u0081A\2\u00fb\60\3\2\2\2\u00fc")
        buf.write("\u00fd\5q9\2\u00fd\u00fe\5\u0089E\2\u00fe\u00ff\5\u0087")
        buf.write("D\2\u00ff\u0100\5\u0093J\2\u0100\u0101\5}?\2\u0101\u0102")
        buf.write("\5\u0087D\2\u0102\u0103\5\u0095K\2\u0103\u0104\5u;\2\u0104")
        buf.write("\62\3\2\2\2\u0105\u0106\5w<\2\u0106\u0107\5\u0089E\2\u0107")
        buf.write("\u0108\5\u008fH\2\u0108\64\3\2\2\2\u0109\u010a\5\u0093")
        buf.write("J\2\u010a\u010b\5\u0089E\2\u010b\66\3\2\2\2\u010c\u010d")
        buf.write("\5s:\2\u010d\u010e\5\u0089E\2\u010e\u010f\5\u0099M\2\u010f")
        buf.write("\u0110\5\u0087D\2\u0110\u0111\5\u0093J\2\u0111\u0112\5")
        buf.write("\u0089E\2\u01128\3\2\2\2\u0113\u0114\5s:\2\u0114\u0115")
        buf.write("\5\u0089E\2\u0115:\3\2\2\2\u0116\u0117\5}?\2\u0117\u0118")
        buf.write("\5w<\2\u0118<\3\2\2\2\u0119\u011a\5\u0093J\2\u011a\u011b")
        buf.write("\5{>\2\u011b\u011c\5u;\2\u011c\u011d\5\u0087D\2\u011d")
        buf.write(">\3\2\2\2\u011e\u011f\5u;\2\u011f\u0120\5\u0083B\2\u0120")
        buf.write("\u0121\5\u0091I\2\u0121\u0122\5u;\2\u0122@\3\2\2\2\u0123")
        buf.write("\u0124\5\u008fH\2\u0124\u0125\5u;\2\u0125\u0126\5\u0093")
        buf.write("J\2\u0126\u0127\5\u0095K\2\u0127\u0128\5\u008fH\2\u0128")
        buf.write("\u0129\5\u0087D\2\u0129B\3\2\2\2\u012a\u012b\5\u0099M")
        buf.write("\2\u012b\u012c\5{>\2\u012c\u012d\5}?\2\u012d\u012e\5\u0083")
        buf.write("B\2\u012e\u012f\5u;\2\u012fD\3\2\2\2\u0130\u0131\5o8\2")
        buf.write("\u0131\u0132\5u;\2\u0132\u0133\5y=\2\u0133\u0134\5}?\2")
        buf.write("\u0134\u0135\5\u0087D\2\u0135F\3\2\2\2\u0136\u0137\5u")
        buf.write(";\2\u0137\u0138\5\u0087D\2\u0138\u0139\5s:\2\u0139H\3")
        buf.write("\2\2\2\u013a\u013b\5w<\2\u013b\u013c\5\u0095K\2\u013c")
        buf.write("\u013d\5\u0087D\2\u013d\u013e\5q9\2\u013e\u013f\5\u0093")
        buf.write("J\2\u013f\u0140\5}?\2\u0140\u0141\5\u0089E\2\u0141\u0142")
        buf.write("\5\u0087D\2\u0142J\3\2\2\2\u0143\u0144\5\u008bF\2\u0144")
        buf.write("\u0145\5\u008fH\2\u0145\u0146\5\u0089E\2\u0146\u0147\5")
        buf.write("q9\2\u0147\u0148\5u;\2\u0148\u0149\5s:\2\u0149\u014a\5")
        buf.write("\u0095K\2\u014a\u014b\5\u008fH\2\u014b\u014c\5u;\2\u014c")
        buf.write("L\3\2\2\2\u014d\u014e\5\u0097L\2\u014e\u014f\5m\67\2\u014f")
        buf.write("\u0150\5\u008fH\2\u0150N\3\2\2\2\u0151\u0152\5\u0093J")
        buf.write("\2\u0152\u0153\5\u008fH\2\u0153\u0154\5\u0095K\2\u0154")
        buf.write("\u0155\5u;\2\u0155P\3\2\2\2\u0156\u0157\5w<\2\u0157\u0158")
        buf.write("\5m\67\2\u0158\u0159\5\u0083B\2\u0159\u015a\5\u0091I\2")
        buf.write("\u015a\u015b\5u;\2\u015bR\3\2\2\2\u015c\u015d\5m\67\2")
        buf.write("\u015d\u015e\5\u008fH\2\u015e\u015f\5\u008fH\2\u015f\u0160")
        buf.write("\5m\67\2\u0160\u0161\5\u009dO\2\u0161T\3\2\2\2\u0162\u0163")
        buf.write("\5\u0089E\2\u0163\u0164\5w<\2\u0164V\3\2\2\2\u0165\u0166")
        buf.write("\5\u008fH\2\u0166\u0167\5u;\2\u0167\u0168\5m\67\2\u0168")
        buf.write("\u0169\5\u0083B\2\u0169X\3\2\2\2\u016a\u016b\5o8\2\u016b")
        buf.write("\u016c\5\u0089E\2\u016c\u016d\5\u0089E\2\u016d\u016e\5")
        buf.write("\u0083B\2\u016e\u016f\5u;\2\u016f\u0170\5m\67\2\u0170")
        buf.write("\u0171\5\u0087D\2\u0171\u0178\3\2\2\2\u0172\u0173\5o8")
        buf.write("\2\u0173\u0174\5\u0089E\2\u0174\u0175\5\u0089E\2\u0175")
        buf.write("\u0176\5\u0083B\2\u0176\u0178\3\2\2\2\u0177\u016a\3\2")
        buf.write("\2\2\u0177\u0172\3\2\2\2\u0178Z\3\2\2\2\u0179\u017a\5")
        buf.write("}?\2\u017a\u017b\5\u0087D\2\u017b\u017c\5\u0093J\2\u017c")
        buf.write("\u017d\5u;\2\u017d\u017e\5y=\2\u017e\u017f\5u;\2\u017f")
        buf.write("\u0180\5\u008fH\2\u0180\u0186\3\2\2\2\u0181\u0182\5}?")
        buf.write("\2\u0182\u0183\5\u0087D\2\u0183\u0184\5\u0093J\2\u0184")
        buf.write("\u0186\3\2\2\2\u0185\u0179\3\2\2\2\u0185\u0181\3\2\2\2")
        buf.write("\u0186\\\3\2\2\2\u0187\u0188\5\u0091I\2\u0188\u0189\5")
        buf.write("\u0093J\2\u0189\u018a\5\u008fH\2\u018a\u018b\5}?\2\u018b")
        buf.write("\u018c\5\u0087D\2\u018c\u018d\5y=\2\u018d^\3\2\2\2\u018e")
        buf.write("\u018f\5\u0087D\2\u018f\u0190\5\u0089E\2\u0190\u0191\5")
        buf.write("\u0093J\2\u0191`\3\2\2\2\u0192\u0193\5m\67\2\u0193\u0194")
        buf.write("\5\u0087D\2\u0194\u0195\5s:\2\u0195b\3\2\2\2\u0196\u0197")
        buf.write("\5\u0089E\2\u0197\u0198\5\u008fH\2\u0198d\3\2\2\2\u0199")
        buf.write("\u019a\5s:\2\u019a\u019b\5}?\2\u019b\u019c\5\u0097L\2")
        buf.write("\u019cf\3\2\2\2\u019d\u019e\5\u0085C\2\u019e\u019f\5\u0089")
        buf.write("E\2\u019f\u01a0\5s:\2\u01a0h\3\2\2\2\u01a1\u01a2\5a\61")
        buf.write("\2\u01a2\u01a3\5+\26\2\u01a3\u01a4\5=\37\2\u01a4j\3\2")
        buf.write("\2\2\u01a5\u01a6\5c\62\2\u01a6\u01a7\5+\26\2\u01a7\u01a8")
        buf.write("\5? \2\u01a8l\3\2\2\2\u01a9\u01aa\t\2\2\2\u01aan\3\2\2")
        buf.write("\2\u01ab\u01ac\t\3\2\2\u01acp\3\2\2\2\u01ad\u01ae\t\4")
        buf.write("\2\2\u01aer\3\2\2\2\u01af\u01b0\t\5\2\2\u01b0t\3\2\2\2")
        buf.write("\u01b1\u01b2\t\6\2\2\u01b2v\3\2\2\2\u01b3\u01b4\t\7\2")
        buf.write("\2\u01b4x\3\2\2\2\u01b5\u01b6\t\b\2\2\u01b6z\3\2\2\2\u01b7")
        buf.write("\u01b8\t\t\2\2\u01b8|\3\2\2\2\u01b9\u01ba\t\n\2\2\u01ba")
        buf.write("~\3\2\2\2\u01bb\u01bc\t\13\2\2\u01bc\u0080\3\2\2\2\u01bd")
        buf.write("\u01be\t\f\2\2\u01be\u0082\3\2\2\2\u01bf\u01c0\t\r\2\2")
        buf.write("\u01c0\u0084\3\2\2\2\u01c1\u01c2\t\16\2\2\u01c2\u0086")
        buf.write("\3\2\2\2\u01c3\u01c4\t\17\2\2\u01c4\u0088\3\2\2\2\u01c5")
        buf.write("\u01c6\t\20\2\2\u01c6\u008a\3\2\2\2\u01c7\u01c8\t\21\2")
        buf.write("\2\u01c8\u008c\3\2\2\2\u01c9\u01ca\t\22\2\2\u01ca\u008e")
        buf.write("\3\2\2\2\u01cb\u01cc\t\23\2\2\u01cc\u0090\3\2\2\2\u01cd")
        buf.write("\u01ce\t\24\2\2\u01ce\u0092\3\2\2\2\u01cf\u01d0\t\25\2")
        buf.write("\2\u01d0\u0094\3\2\2\2\u01d1\u01d2\t\26\2\2\u01d2\u0096")
        buf.write("\3\2\2\2\u01d3\u01d4\t\27\2\2\u01d4\u0098\3\2\2\2\u01d5")
        buf.write("\u01d6\t\30\2\2\u01d6\u009a\3\2\2\2\u01d7\u01d8\t\31\2")
        buf.write("\2\u01d8\u009c\3\2\2\2\u01d9\u01da\t\32\2\2\u01da\u009e")
        buf.write("\3\2\2\2\u01db\u01dc\t\33\2\2\u01dc\u00a0\3\2\2\2\u01dd")
        buf.write("\u01de\t\34\2\2\u01de\u00a2\3\2\2\2\u01df\u01e1\5\u00a1")
        buf.write("Q\2\u01e0\u01df\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e2\u01e0")
        buf.write("\3\2\2\2\u01e2\u01e3\3\2\2\2\u01e3\u00a4\3\2\2\2\u01e4")
        buf.write("\u01e6\t\35\2\2\u01e5\u01e4\3\2\2\2\u01e6\u01ea\3\2\2")
        buf.write("\2\u01e7\u01e9\t\36\2\2\u01e8\u01e7\3\2\2\2\u01e9\u01ec")
        buf.write("\3\2\2\2\u01ea\u01e8\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb")
        buf.write("\u00a6\3\2\2\2\u01ec\u01ea\3\2\2\2\u01ed\u01ef\t\34\2")
        buf.write("\2\u01ee\u01ed\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0\u01ee")
        buf.write("\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1\u00a8\3\2\2\2\u01f2")
        buf.write("\u01f4\t\34\2\2\u01f3\u01f2\3\2\2\2\u01f4\u01f5\3\2\2")
        buf.write("\2\u01f5\u01f3\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6\u01f8")
        buf.write("\3\2\2\2\u01f7\u01f9\7\60\2\2\u01f8\u01f7\3\2\2\2\u01f8")
        buf.write("\u01f9\3\2\2\2\u01f9\u01fd\3\2\2\2\u01fa\u01fc\t\34\2")
        buf.write("\2\u01fb\u01fa\3\2\2\2\u01fc\u01ff\3\2\2\2\u01fd\u01fb")
        buf.write("\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fe\u020e\3\2\2\2\u01ff")
        buf.write("\u01fd\3\2\2\2\u0200\u0202\t\34\2\2\u0201\u0200\3\2\2")
        buf.write("\2\u0202\u0203\3\2\2\2\u0203\u0201\3\2\2\2\u0203\u0204")
        buf.write("\3\2\2\2\u0204\u0205\3\2\2\2\u0205\u0207\t\6\2\2\u0206")
        buf.write("\u0208\7/\2\2\u0207\u0206\3\2\2\2\u0207\u0208\3\2\2\2")
        buf.write("\u0208\u020a\3\2\2\2\u0209\u020b\t\34\2\2\u020a\u0209")
        buf.write("\3\2\2\2\u020b\u020c\3\2\2\2\u020c\u020a\3\2\2\2\u020c")
        buf.write("\u020d\3\2\2\2\u020d\u020f\3\2\2\2\u020e\u0201\3\2\2\2")
        buf.write("\u020e\u020f\3\2\2\2\u020f\u022a\3\2\2\2\u0210\u0212\t")
        buf.write("\34\2\2\u0211\u0210\3\2\2\2\u0212\u0215\3\2\2\2\u0213")
        buf.write("\u0211\3\2\2\2\u0213\u0214\3\2\2\2\u0214\u0217\3\2\2\2")
        buf.write("\u0215\u0213\3\2\2\2\u0216\u0218\7\60\2\2\u0217\u0216")
        buf.write("\3\2\2\2\u0217\u0218\3\2\2\2\u0218\u021a\3\2\2\2\u0219")
        buf.write("\u021b\t\34\2\2\u021a\u0219\3\2\2\2\u021b\u021c\3\2\2")
        buf.write("\2\u021c\u021a\3\2\2\2\u021c\u021d\3\2\2\2\u021d\u0227")
        buf.write("\3\2\2\2\u021e\u0220\t\6\2\2\u021f\u0221\7/\2\2\u0220")
        buf.write("\u021f\3\2\2\2\u0220\u0221\3\2\2\2\u0221\u0223\3\2\2\2")
        buf.write("\u0222\u0224\t\34\2\2\u0223\u0222\3\2\2\2\u0224\u0225")
        buf.write("\3\2\2\2\u0225\u0223\3\2\2\2\u0225\u0226\3\2\2\2\u0226")
        buf.write("\u0228\3\2\2\2\u0227\u021e\3\2\2\2\u0227\u0228\3\2\2\2")
        buf.write("\u0228\u022a\3\2\2\2\u0229\u01f3\3\2\2\2\u0229\u0213\3")
        buf.write("\2\2\2\u022a\u00aa\3\2\2\2\u022b\u022c\7v\2\2\u022c\u022d")
        buf.write("\7t\2\2\u022d\u022e\7w\2\2\u022e\u0235\7g\2\2\u022f\u0230")
        buf.write("\7h\2\2\u0230\u0231\7c\2\2\u0231\u0232\7n\2\2\u0232\u0233")
        buf.write("\7u\2\2\u0233\u0235\7g\2\2\u0234\u022b\3\2\2\2\u0234\u022f")
        buf.write("\3\2\2\2\u0235\u00ac\3\2\2\2\u0236\u023c\7$\2\2\u0237")
        buf.write("\u0238\7^\2\2\u0238\u023b\t\37\2\2\u0239\u023b\n \2\2")
        buf.write("\u023a\u0237\3\2\2\2\u023a\u0239\3\2\2\2\u023b\u023e\3")
        buf.write("\2\2\2\u023c\u023a\3\2\2\2\u023c\u023d\3\2\2\2\u023d\u023f")
        buf.write("\3\2\2\2\u023e\u023c\3\2\2\2\u023f\u0240\7$\2\2\u0240")
        buf.write("\u0241\bW\2\2\u0241\u00ae\3\2\2\2\u0242\u0248\5Y-\2\u0243")
        buf.write("\u0248\5[.\2\u0244\u0248\5W,\2\u0245\u0248\5]/\2\u0246")
        buf.write("\u0248\5S*\2\u0247\u0242\3\2\2\2\u0247\u0243\3\2\2\2\u0247")
        buf.write("\u0244\3\2\2\2\u0247\u0245\3\2\2\2\u0247\u0246\3\2\2\2")
        buf.write("\u0248\u00b0\3\2\2\2\u0249\u024c\5\u00b3Z\2\u024a\u024c")
        buf.write("\5\u00b9]\2\u024b\u0249\3\2\2\2\u024b\u024a\3\2\2\2\u024c")
        buf.write("\u024d\3\2\2\2\u024d\u024e\bY\3\2\u024e\u00b2\3\2\2\2")
        buf.write("\u024f\u0252\5\u00b5[\2\u0250\u0252\5\u00b7\\\2\u0251")
        buf.write("\u024f\3\2\2\2\u0251\u0250\3\2\2\2\u0252\u00b4\3\2\2\2")
        buf.write("\u0253\u0254\7*\2\2\u0254\u0255\7,\2\2\u0255\u0259\3\2")
        buf.write("\2\2\u0256\u0258\13\2\2\2\u0257\u0256\3\2\2\2\u0258\u025b")
        buf.write("\3\2\2\2\u0259\u025a\3\2\2\2\u0259\u0257\3\2\2\2\u025a")
        buf.write("\u025c\3\2\2\2\u025b\u0259\3\2\2\2\u025c\u025d\7,\2\2")
        buf.write("\u025d\u025e\7+\2\2\u025e\u00b6\3\2\2\2\u025f\u0263\7")
        buf.write("}\2\2\u0260\u0262\13\2\2\2\u0261\u0260\3\2\2\2\u0262\u0265")
        buf.write("\3\2\2\2\u0263\u0264\3\2\2\2\u0263\u0261\3\2\2\2\u0264")
        buf.write("\u0266\3\2\2\2\u0265\u0263\3\2\2\2\u0266\u0267\7\177\2")
        buf.write("\2\u0267\u00b8\3\2\2\2\u0268\u0269\7\61\2\2\u0269\u026a")
        buf.write("\7\61\2\2\u026a\u026e\3\2\2\2\u026b\u026d\n!\2\2\u026c")
        buf.write("\u026b\3\2\2\2\u026d\u0270\3\2\2\2\u026e\u026c\3\2\2\2")
        buf.write("\u026e\u026f\3\2\2\2\u026f\u00ba\3\2\2\2\u0270\u026e\3")
        buf.write("\2\2\2\u0271\u0277\7$\2\2\u0272\u0273\7^\2\2\u0273\u0276")
        buf.write("\t\37\2\2\u0274\u0276\n\"\2\2\u0275\u0272\3\2\2\2\u0275")
        buf.write("\u0274\3\2\2\2\u0276\u0279\3\2\2\2\u0277\u0275\3\2\2\2")
        buf.write("\u0277\u0278\3\2\2\2\u0278\u027a\3\2\2\2\u0279\u0277\3")
        buf.write("\2\2\2\u027a\u027b\b^\4\2\u027b\u00bc\3\2\2\2\u027c\u0282")
        buf.write("\7$\2\2\u027d\u027e\7^\2\2\u027e\u0281\t\37\2\2\u027f")
        buf.write("\u0281\n \2\2\u0280\u027d\3\2\2\2\u0280\u027f\3\2\2\2")
        buf.write("\u0281\u0284\3\2\2\2\u0282\u0280\3\2\2\2\u0282\u0283\3")
        buf.write("\2\2\2\u0283\u0286\3\2\2\2\u0284\u0282\3\2\2\2\u0285\u0287")
        buf.write("\t\"\2\2\u0286\u0285\3\2\2\2\u0287\u0288\3\2\2\2\u0288")
        buf.write("\u0286\3\2\2\2\u0288\u0289\3\2\2\2\u0289\u028d\3\2\2\2")
        buf.write("\u028a\u028c\13\2\2\2\u028b\u028a\3\2\2\2\u028c\u028f")
        buf.write("\3\2\2\2\u028d\u028e\3\2\2\2\u028d\u028b\3\2\2\2\u028e")
        buf.write("\u0290\3\2\2\2\u028f\u028d\3\2\2\2\u0290\u0291\7$\2\2")
        buf.write("\u0291\u0292\b_\5\2\u0292\u00be\3\2\2\2\u0293\u0299\7")
        buf.write("$\2\2\u0294\u0295\7^\2\2\u0295\u0298\t\37\2\2\u0296\u0298")
        buf.write("\n \2\2\u0297\u0294\3\2\2\2\u0297\u0296\3\2\2\2\u0298")
        buf.write("\u029b\3\2\2\2\u0299\u0297\3\2\2\2\u0299\u029a\3\2\2\2")
        buf.write("\u029a\u029d\3\2\2\2\u029b\u0299\3\2\2\2\u029c\u029e\t")
        buf.write("\"\2\2\u029d\u029c\3\2\2\2\u029e\u029f\3\2\2\2\u029f\u029d")
        buf.write("\3\2\2\2\u029f\u02a0\3\2\2\2\u02a0\u02a4\3\2\2\2\u02a1")
        buf.write("\u02a3\n#\2\2\u02a2\u02a1\3\2\2\2\u02a3\u02a6\3\2\2\2")
        buf.write("\u02a4\u02a2\3\2\2\2\u02a4\u02a5\3\2\2\2\u02a5\u02a7\3")
        buf.write("\2\2\2\u02a6\u02a4\3\2\2\2\u02a7\u02a8\b`\6\2\u02a8\u00c0")
        buf.write("\3\2\2\2\u02a9\u02aa\13\2\2\2\u02aa\u00c2\3\2\2\2\u02ab")
        buf.write("\u02ad\t$\2\2\u02ac\u02ab\3\2\2\2\u02ad\u02ae\3\2\2\2")
        buf.write("\u02ae\u02ac\3\2\2\2\u02ae\u02af\3\2\2\2\u02af\u02b0\3")
        buf.write("\2\2\2\u02b0\u02b1\bb\3\2\u02b1\u00c4\3\2\2\2,\2\u0177")
        buf.write("\u0185\u01e2\u01e5\u01e8\u01ea\u01f0\u01f5\u01f8\u01fd")
        buf.write("\u0203\u0207\u020c\u020e\u0213\u0217\u021c\u0220\u0225")
        buf.write("\u0227\u0229\u0234\u023a\u023c\u0247\u024b\u0251\u0259")
        buf.write("\u0263\u026e\u0275\u0277\u0280\u0282\u0288\u028d\u0297")
        buf.write("\u0299\u029f\u02a4\u02ae\7\3W\2\b\2\2\3^\3\3_\4\3`\5")
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
    ANDTHEN = 52
    ORELSE = 53
    ManyNum = 54
    ID = 55
    INTLIT = 56
    REALLIT = 57
    BOOLLIT = 58
    STRINGLIT = 59
    TYPE = 60
    CMT = 61
    BLKCMT = 62
    TRACMT = 63
    BLCMT = 64
    LINECMT = 65
    UNCLOSE_STRING = 66
    ILLEGAL_ESCAPE1 = 67
    ILLEGAL_ESCAPE2 = 68
    ERROR_CHAR = 69
    WS = 70

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
            "AND", "OR", "DIV", "MOD", "ANDTHEN", "ORELSE", "ManyNum", "ID", 
            "INTLIT", "REALLIT", "BOOLLIT", "STRINGLIT", "TYPE", "CMT", 
            "BLKCMT", "TRACMT", "BLCMT", "LINECMT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE1", 
            "ILLEGAL_ESCAPE2", "ERROR_CHAR", "WS" ]

    ruleNames = [ "LB", "RB", "LP", "RP", "LQ", "RQ", "SEMI", "CM", "EQ", 
                  "COL", "DD", "ADD", "MUL", "NOTEQ", "LESSTN", "LESSEQ", 
                  "SUBNE", "DIVSI", "GRETN", "GREEQ", "SP", "ASSI", "BREAK", 
                  "CONTINUE", "FOR", "TO", "DOWNTO", "DO", "IF", "THEN", 
                  "ELSE", "RETURN", "WHILE", "BEGIN", "END", "FUNCTION", 
                  "PROCEDURE", "VAR", "TRUE", "FALSE", "ARRAY", "OF", "REAL", 
                  "BOOLEAN", "INTEGER", "STRING", "NOT", "AND", "OR", "DIV", 
                  "MOD", "ANDTHEN", "ORELSE", "A", "B", "C", "D", "E", "F", 
                  "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", 
                  "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "NUM", "ManyNum", 
                  "ID", "INTLIT", "REALLIT", "BOOLLIT", "STRINGLIT", "TYPE", 
                  "CMT", "BLKCMT", "TRACMT", "BLCMT", "LINECMT", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE1", "ILLEGAL_ESCAPE2", "ERROR_CHAR", "WS" ]

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
            actions[85] = self.STRINGLIT_action 
            actions[92] = self.UNCLOSE_STRING_action 
            actions[93] = self.ILLEGAL_ESCAPE1_action 
            actions[94] = self.ILLEGAL_ESCAPE2_action 
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

            									raise UncloseString(self.text[1:len(self.text)])
     

    def ILLEGAL_ESCAPE1_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise IllegalEscape(self.text[1:len(self.text) - 1])
     

    def ILLEGAL_ESCAPE2_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise IllegalEscape(self.text[1:len(self.text)])
     


