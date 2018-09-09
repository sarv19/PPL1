# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2G")
        buf.write("\u029d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5")
        buf.write("\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3")
        buf.write("\21\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3%\3%\3")
        buf.write("%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3\'")
        buf.write("\3\'\3\'\3\'\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3*\3*\3")
        buf.write("*\3*\3*\3*\3+\3+\3+\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3")
        buf.write("-\3-\3-\3-\3-\3-\3-\5-\u0176\n-\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\3.\3.\3.\5.\u0184\n.\3/\3/\3/\3/\3/\3/\3/\3\60\3")
        buf.write("\60\3\60\3\60\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\63")
        buf.write("\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65")
        buf.write("\3\66\3\66\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3")
        buf.write(";\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3")
        buf.write("D\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3J\3J\3K\3K\3L\3L\3M\3")
        buf.write("M\3N\3N\3O\3O\3P\3P\3Q\3Q\3R\6R\u01df\nR\rR\16R\u01e0")
        buf.write("\3S\5S\u01e4\nS\3S\7S\u01e7\nS\fS\16S\u01ea\13S\3T\6T")
        buf.write("\u01ed\nT\rT\16T\u01ee\3U\6U\u01f2\nU\rU\16U\u01f3\3U")
        buf.write("\5U\u01f7\nU\3U\7U\u01fa\nU\fU\16U\u01fd\13U\3U\6U\u0200")
        buf.write("\nU\rU\16U\u0201\3U\3U\5U\u0206\nU\3U\6U\u0209\nU\rU\16")
        buf.write("U\u020a\5U\u020d\nU\3U\7U\u0210\nU\fU\16U\u0213\13U\3")
        buf.write("U\5U\u0216\nU\3U\6U\u0219\nU\rU\16U\u021a\3U\3U\5U\u021f")
        buf.write("\nU\3U\6U\u0222\nU\rU\16U\u0223\5U\u0226\nU\5U\u0228\n")
        buf.write("U\3V\3V\3V\3V\3V\3V\3V\3V\3V\5V\u0233\nV\3W\3W\3W\3W\7")
        buf.write("W\u0239\nW\fW\16W\u023c\13W\3W\3W\3X\3X\3X\3X\3X\5X\u0245")
        buf.write("\nX\3Y\3Y\5Y\u0249\nY\3Z\3Z\5Z\u024d\nZ\3[\3[\3[\3[\7")
        buf.write("[\u0253\n[\f[\16[\u0256\13[\3[\3[\3[\3[\3[\3\\\3\\\7\\")
        buf.write("\u025f\n\\\f\\\16\\\u0262\13\\\3\\\3\\\3\\\3\\\3]\3]\3")
        buf.write("]\3]\7]\u026c\n]\f]\16]\u026f\13]\3^\3^\3_\3_\3_\3_\3")
        buf.write("_\7_\u0278\n_\f_\16_\u027b\13_\3`\3`\3`\3`\3`\7`\u0282")
        buf.write("\n`\f`\16`\u0285\13`\3`\6`\u0288\n`\r`\16`\u0289\3`\3")
        buf.write("`\3`\7`\u028f\n`\f`\16`\u0292\13`\3`\5`\u0295\n`\3a\6")
        buf.write("a\u0298\na\ra\16a\u0299\3a\3a\4\u0254\u0260\2b\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m\2o\2q\2s\2u\2w\2")
        buf.write("y\2{\2}\2\177\2\u0081\2\u0083\2\u0085\2\u0087\2\u0089")
        buf.write("\2\u008b\2\u008d\2\u008f\2\u0091\2\u0093\2\u0095\2\u0097")
        buf.write("\2\u0099\2\u009b\2\u009d\2\u009f\2\u00a1\2\u00a38\u00a5")
        buf.write("9\u00a7:\u00a9;\u00ab<\u00ad=\u00af>\u00b1?\u00b3@\u00b5")
        buf.write("A\u00b7B\u00b9C\u00bbD\u00bdE\u00bfF\u00c1G\3\2$\4\2C")
        buf.write("Ccc\4\2DDdd\4\2EEee\4\2FFff\4\2GGgg\4\2HHhh\4\2IIii\4")
        buf.write("\2JJjj\4\2KKkk\4\2LLll\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPp")
        buf.write("p\4\2QQqq\4\2RRrr\4\2SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2")
        buf.write("WWww\4\2XXxx\4\2YYyy\4\2ZZzz\4\2[[{{\4\2\\\\||\3\2\62")
        buf.write(";\5\2C\\aac|\6\2\62;C\\aac|\n\2$$))^^ddhhppttvv\7\2\n")
        buf.write("\f\16\17$$))^^\4\2\f\f\17\17\7\2\13\f\16\17$$))^^\5\2")
        buf.write("\13\f\17\17\"\"\2\u02a9\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2")
        buf.write("!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2")
        buf.write("\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9")
        buf.write("\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2\2\2\u00af\3\2\2")
        buf.write("\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2\2\2\u00b5\3\2\2\2\2\u00b7")
        buf.write("\3\2\2\2\2\u00b9\3\2\2\2\2\u00bb\3\2\2\2\2\u00bd\3\2\2")
        buf.write("\2\2\u00bf\3\2\2\2\2\u00c1\3\2\2\2\3\u00c3\3\2\2\2\5\u00c5")
        buf.write("\3\2\2\2\7\u00c7\3\2\2\2\t\u00c9\3\2\2\2\13\u00cb\3\2")
        buf.write("\2\2\r\u00cd\3\2\2\2\17\u00cf\3\2\2\2\21\u00d1\3\2\2\2")
        buf.write("\23\u00d3\3\2\2\2\25\u00d5\3\2\2\2\27\u00d7\3\2\2\2\31")
        buf.write("\u00da\3\2\2\2\33\u00dc\3\2\2\2\35\u00de\3\2\2\2\37\u00e1")
        buf.write("\3\2\2\2!\u00e3\3\2\2\2#\u00e6\3\2\2\2%\u00e8\3\2\2\2")
        buf.write("\'\u00ea\3\2\2\2)\u00ec\3\2\2\2+\u00ef\3\2\2\2-\u00f1")
        buf.write("\3\2\2\2/\u00f4\3\2\2\2\61\u00fa\3\2\2\2\63\u0103\3\2")
        buf.write("\2\2\65\u0107\3\2\2\2\67\u010a\3\2\2\29\u0111\3\2\2\2")
        buf.write(";\u0114\3\2\2\2=\u0117\3\2\2\2?\u011c\3\2\2\2A\u0121\3")
        buf.write("\2\2\2C\u0128\3\2\2\2E\u012e\3\2\2\2G\u0134\3\2\2\2I\u0138")
        buf.write("\3\2\2\2K\u0141\3\2\2\2M\u014b\3\2\2\2O\u014f\3\2\2\2")
        buf.write("Q\u0154\3\2\2\2S\u015a\3\2\2\2U\u0160\3\2\2\2W\u0163\3")
        buf.write("\2\2\2Y\u0175\3\2\2\2[\u0183\3\2\2\2]\u0185\3\2\2\2_\u018c")
        buf.write("\3\2\2\2a\u0190\3\2\2\2c\u0194\3\2\2\2e\u0197\3\2\2\2")
        buf.write("g\u019b\3\2\2\2i\u019f\3\2\2\2k\u01a3\3\2\2\2m\u01a7\3")
        buf.write("\2\2\2o\u01a9\3\2\2\2q\u01ab\3\2\2\2s\u01ad\3\2\2\2u\u01af")
        buf.write("\3\2\2\2w\u01b1\3\2\2\2y\u01b3\3\2\2\2{\u01b5\3\2\2\2")
        buf.write("}\u01b7\3\2\2\2\177\u01b9\3\2\2\2\u0081\u01bb\3\2\2\2")
        buf.write("\u0083\u01bd\3\2\2\2\u0085\u01bf\3\2\2\2\u0087\u01c1\3")
        buf.write("\2\2\2\u0089\u01c3\3\2\2\2\u008b\u01c5\3\2\2\2\u008d\u01c7")
        buf.write("\3\2\2\2\u008f\u01c9\3\2\2\2\u0091\u01cb\3\2\2\2\u0093")
        buf.write("\u01cd\3\2\2\2\u0095\u01cf\3\2\2\2\u0097\u01d1\3\2\2\2")
        buf.write("\u0099\u01d3\3\2\2\2\u009b\u01d5\3\2\2\2\u009d\u01d7\3")
        buf.write("\2\2\2\u009f\u01d9\3\2\2\2\u00a1\u01db\3\2\2\2\u00a3\u01de")
        buf.write("\3\2\2\2\u00a5\u01e3\3\2\2\2\u00a7\u01ec\3\2\2\2\u00a9")
        buf.write("\u0227\3\2\2\2\u00ab\u0232\3\2\2\2\u00ad\u0234\3\2\2\2")
        buf.write("\u00af\u0244\3\2\2\2\u00b1\u0248\3\2\2\2\u00b3\u024c\3")
        buf.write("\2\2\2\u00b5\u024e\3\2\2\2\u00b7\u025c\3\2\2\2\u00b9\u0267")
        buf.write("\3\2\2\2\u00bb\u0270\3\2\2\2\u00bd\u0272\3\2\2\2\u00bf")
        buf.write("\u027c\3\2\2\2\u00c1\u0297\3\2\2\2\u00c3\u00c4\7*\2\2")
        buf.write("\u00c4\4\3\2\2\2\u00c5\u00c6\7+\2\2\u00c6\6\3\2\2\2\u00c7")
        buf.write("\u00c8\7}\2\2\u00c8\b\3\2\2\2\u00c9\u00ca\7\177\2\2\u00ca")
        buf.write("\n\3\2\2\2\u00cb\u00cc\7]\2\2\u00cc\f\3\2\2\2\u00cd\u00ce")
        buf.write("\7_\2\2\u00ce\16\3\2\2\2\u00cf\u00d0\7=\2\2\u00d0\20\3")
        buf.write("\2\2\2\u00d1\u00d2\7.\2\2\u00d2\22\3\2\2\2\u00d3\u00d4")
        buf.write("\7?\2\2\u00d4\24\3\2\2\2\u00d5\u00d6\7<\2\2\u00d6\26\3")
        buf.write("\2\2\2\u00d7\u00d8\7\60\2\2\u00d8\u00d9\7\60\2\2\u00d9")
        buf.write("\30\3\2\2\2\u00da\u00db\7-\2\2\u00db\32\3\2\2\2\u00dc")
        buf.write("\u00dd\7,\2\2\u00dd\34\3\2\2\2\u00de\u00df\7>\2\2\u00df")
        buf.write("\u00e0\7@\2\2\u00e0\36\3\2\2\2\u00e1\u00e2\7>\2\2\u00e2")
        buf.write(" \3\2\2\2\u00e3\u00e4\7>\2\2\u00e4\u00e5\7?\2\2\u00e5")
        buf.write("\"\3\2\2\2\u00e6\u00e7\7/\2\2\u00e7$\3\2\2\2\u00e8\u00e9")
        buf.write("\7\61\2\2\u00e9&\3\2\2\2\u00ea\u00eb\7@\2\2\u00eb(\3\2")
        buf.write("\2\2\u00ec\u00ed\7@\2\2\u00ed\u00ee\7?\2\2\u00ee*\3\2")
        buf.write("\2\2\u00ef\u00f0\7\"\2\2\u00f0,\3\2\2\2\u00f1\u00f2\7")
        buf.write("<\2\2\u00f2\u00f3\7?\2\2\u00f3.\3\2\2\2\u00f4\u00f5\5")
        buf.write("o8\2\u00f5\u00f6\5\u008fH\2\u00f6\u00f7\5u;\2\u00f7\u00f8")
        buf.write("\5m\67\2\u00f8\u00f9\5\u0081A\2\u00f9\60\3\2\2\2\u00fa")
        buf.write("\u00fb\5q9\2\u00fb\u00fc\5\u0089E\2\u00fc\u00fd\5\u0087")
        buf.write("D\2\u00fd\u00fe\5\u0093J\2\u00fe\u00ff\5}?\2\u00ff\u0100")
        buf.write("\5\u0087D\2\u0100\u0101\5\u0095K\2\u0101\u0102\5u;\2\u0102")
        buf.write("\62\3\2\2\2\u0103\u0104\5w<\2\u0104\u0105\5\u0089E\2\u0105")
        buf.write("\u0106\5\u008fH\2\u0106\64\3\2\2\2\u0107\u0108\5\u0093")
        buf.write("J\2\u0108\u0109\5\u0089E\2\u0109\66\3\2\2\2\u010a\u010b")
        buf.write("\5s:\2\u010b\u010c\5\u0089E\2\u010c\u010d\5\u0099M\2\u010d")
        buf.write("\u010e\5\u0087D\2\u010e\u010f\5\u0093J\2\u010f\u0110\5")
        buf.write("\u0089E\2\u01108\3\2\2\2\u0111\u0112\5s:\2\u0112\u0113")
        buf.write("\5\u0089E\2\u0113:\3\2\2\2\u0114\u0115\5}?\2\u0115\u0116")
        buf.write("\5w<\2\u0116<\3\2\2\2\u0117\u0118\5\u0093J\2\u0118\u0119")
        buf.write("\5{>\2\u0119\u011a\5u;\2\u011a\u011b\5\u0087D\2\u011b")
        buf.write(">\3\2\2\2\u011c\u011d\5u;\2\u011d\u011e\5\u0083B\2\u011e")
        buf.write("\u011f\5\u0091I\2\u011f\u0120\5u;\2\u0120@\3\2\2\2\u0121")
        buf.write("\u0122\5\u008fH\2\u0122\u0123\5u;\2\u0123\u0124\5\u0093")
        buf.write("J\2\u0124\u0125\5\u0095K\2\u0125\u0126\5\u008fH\2\u0126")
        buf.write("\u0127\5\u0087D\2\u0127B\3\2\2\2\u0128\u0129\5\u0099M")
        buf.write("\2\u0129\u012a\5{>\2\u012a\u012b\5}?\2\u012b\u012c\5\u0083")
        buf.write("B\2\u012c\u012d\5u;\2\u012dD\3\2\2\2\u012e\u012f\5o8\2")
        buf.write("\u012f\u0130\5u;\2\u0130\u0131\5y=\2\u0131\u0132\5}?\2")
        buf.write("\u0132\u0133\5\u0087D\2\u0133F\3\2\2\2\u0134\u0135\5u")
        buf.write(";\2\u0135\u0136\5\u0087D\2\u0136\u0137\5s:\2\u0137H\3")
        buf.write("\2\2\2\u0138\u0139\5w<\2\u0139\u013a\5\u0095K\2\u013a")
        buf.write("\u013b\5q9\2\u013b\u013c\5\u0087D\2\u013c\u013d\5\u0093")
        buf.write("J\2\u013d\u013e\5}?\2\u013e\u013f\5\u0089E\2\u013f\u0140")
        buf.write("\5\u0087D\2\u0140J\3\2\2\2\u0141\u0142\5\u008bF\2\u0142")
        buf.write("\u0143\5\u008fH\2\u0143\u0144\5\u0089E\2\u0144\u0145\5")
        buf.write("q9\2\u0145\u0146\5u;\2\u0146\u0147\5s:\2\u0147\u0148\5")
        buf.write("\u0095K\2\u0148\u0149\5\u008fH\2\u0149\u014a\5u;\2\u014a")
        buf.write("L\3\2\2\2\u014b\u014c\5\u0097L\2\u014c\u014d\5m\67\2\u014d")
        buf.write("\u014e\5\u008fH\2\u014eN\3\2\2\2\u014f\u0150\5\u0093J")
        buf.write("\2\u0150\u0151\5\u008fH\2\u0151\u0152\5\u0095K\2\u0152")
        buf.write("\u0153\5u;\2\u0153P\3\2\2\2\u0154\u0155\5w<\2\u0155\u0156")
        buf.write("\5m\67\2\u0156\u0157\5\u0083B\2\u0157\u0158\5\u0091I\2")
        buf.write("\u0158\u0159\5u;\2\u0159R\3\2\2\2\u015a\u015b\5m\67\2")
        buf.write("\u015b\u015c\5\u008fH\2\u015c\u015d\5\u008fH\2\u015d\u015e")
        buf.write("\5m\67\2\u015e\u015f\5\u009dO\2\u015fT\3\2\2\2\u0160\u0161")
        buf.write("\5\u0089E\2\u0161\u0162\5w<\2\u0162V\3\2\2\2\u0163\u0164")
        buf.write("\5\u008fH\2\u0164\u0165\5u;\2\u0165\u0166\5m\67\2\u0166")
        buf.write("\u0167\5\u0083B\2\u0167X\3\2\2\2\u0168\u0169\5o8\2\u0169")
        buf.write("\u016a\5\u0089E\2\u016a\u016b\5\u0089E\2\u016b\u016c\5")
        buf.write("\u0083B\2\u016c\u016d\5u;\2\u016d\u016e\5m\67\2\u016e")
        buf.write("\u016f\5\u0087D\2\u016f\u0176\3\2\2\2\u0170\u0171\5o8")
        buf.write("\2\u0171\u0172\5\u0089E\2\u0172\u0173\5\u0089E\2\u0173")
        buf.write("\u0174\5\u0083B\2\u0174\u0176\3\2\2\2\u0175\u0168\3\2")
        buf.write("\2\2\u0175\u0170\3\2\2\2\u0176Z\3\2\2\2\u0177\u0178\5")
        buf.write("}?\2\u0178\u0179\5\u0087D\2\u0179\u017a\5\u0093J\2\u017a")
        buf.write("\u017b\5u;\2\u017b\u017c\5y=\2\u017c\u017d\5u;\2\u017d")
        buf.write("\u017e\5\u008fH\2\u017e\u0184\3\2\2\2\u017f\u0180\5}?")
        buf.write("\2\u0180\u0181\5\u0087D\2\u0181\u0182\5\u0093J\2\u0182")
        buf.write("\u0184\3\2\2\2\u0183\u0177\3\2\2\2\u0183\u017f\3\2\2\2")
        buf.write("\u0184\\\3\2\2\2\u0185\u0186\5\u0091I\2\u0186\u0187\5")
        buf.write("\u0093J\2\u0187\u0188\5\u008fH\2\u0188\u0189\5}?\2\u0189")
        buf.write("\u018a\5\u0087D\2\u018a\u018b\5y=\2\u018b^\3\2\2\2\u018c")
        buf.write("\u018d\5\u0087D\2\u018d\u018e\5\u0089E\2\u018e\u018f\5")
        buf.write("\u0093J\2\u018f`\3\2\2\2\u0190\u0191\5m\67\2\u0191\u0192")
        buf.write("\5\u0087D\2\u0192\u0193\5s:\2\u0193b\3\2\2\2\u0194\u0195")
        buf.write("\5\u0089E\2\u0195\u0196\5\u008fH\2\u0196d\3\2\2\2\u0197")
        buf.write("\u0198\5s:\2\u0198\u0199\5}?\2\u0199\u019a\5\u0097L\2")
        buf.write("\u019af\3\2\2\2\u019b\u019c\5\u0085C\2\u019c\u019d\5\u0089")
        buf.write("E\2\u019d\u019e\5s:\2\u019eh\3\2\2\2\u019f\u01a0\5a\61")
        buf.write("\2\u01a0\u01a1\5+\26\2\u01a1\u01a2\5=\37\2\u01a2j\3\2")
        buf.write("\2\2\u01a3\u01a4\5c\62\2\u01a4\u01a5\5+\26\2\u01a5\u01a6")
        buf.write("\5? \2\u01a6l\3\2\2\2\u01a7\u01a8\t\2\2\2\u01a8n\3\2\2")
        buf.write("\2\u01a9\u01aa\t\3\2\2\u01aap\3\2\2\2\u01ab\u01ac\t\4")
        buf.write("\2\2\u01acr\3\2\2\2\u01ad\u01ae\t\5\2\2\u01aet\3\2\2\2")
        buf.write("\u01af\u01b0\t\6\2\2\u01b0v\3\2\2\2\u01b1\u01b2\t\7\2")
        buf.write("\2\u01b2x\3\2\2\2\u01b3\u01b4\t\b\2\2\u01b4z\3\2\2\2\u01b5")
        buf.write("\u01b6\t\t\2\2\u01b6|\3\2\2\2\u01b7\u01b8\t\n\2\2\u01b8")
        buf.write("~\3\2\2\2\u01b9\u01ba\t\13\2\2\u01ba\u0080\3\2\2\2\u01bb")
        buf.write("\u01bc\t\f\2\2\u01bc\u0082\3\2\2\2\u01bd\u01be\t\r\2\2")
        buf.write("\u01be\u0084\3\2\2\2\u01bf\u01c0\t\16\2\2\u01c0\u0086")
        buf.write("\3\2\2\2\u01c1\u01c2\t\17\2\2\u01c2\u0088\3\2\2\2\u01c3")
        buf.write("\u01c4\t\20\2\2\u01c4\u008a\3\2\2\2\u01c5\u01c6\t\21\2")
        buf.write("\2\u01c6\u008c\3\2\2\2\u01c7\u01c8\t\22\2\2\u01c8\u008e")
        buf.write("\3\2\2\2\u01c9\u01ca\t\23\2\2\u01ca\u0090\3\2\2\2\u01cb")
        buf.write("\u01cc\t\24\2\2\u01cc\u0092\3\2\2\2\u01cd\u01ce\t\25\2")
        buf.write("\2\u01ce\u0094\3\2\2\2\u01cf\u01d0\t\26\2\2\u01d0\u0096")
        buf.write("\3\2\2\2\u01d1\u01d2\t\27\2\2\u01d2\u0098\3\2\2\2\u01d3")
        buf.write("\u01d4\t\30\2\2\u01d4\u009a\3\2\2\2\u01d5\u01d6\t\31\2")
        buf.write("\2\u01d6\u009c\3\2\2\2\u01d7\u01d8\t\32\2\2\u01d8\u009e")
        buf.write("\3\2\2\2\u01d9\u01da\t\33\2\2\u01da\u00a0\3\2\2\2\u01db")
        buf.write("\u01dc\t\34\2\2\u01dc\u00a2\3\2\2\2\u01dd\u01df\5\u00a1")
        buf.write("Q\2\u01de\u01dd\3\2\2\2\u01df\u01e0\3\2\2\2\u01e0\u01de")
        buf.write("\3\2\2\2\u01e0\u01e1\3\2\2\2\u01e1\u00a4\3\2\2\2\u01e2")
        buf.write("\u01e4\t\35\2\2\u01e3\u01e2\3\2\2\2\u01e4\u01e8\3\2\2")
        buf.write("\2\u01e5\u01e7\t\36\2\2\u01e6\u01e5\3\2\2\2\u01e7\u01ea")
        buf.write("\3\2\2\2\u01e8\u01e6\3\2\2\2\u01e8\u01e9\3\2\2\2\u01e9")
        buf.write("\u00a6\3\2\2\2\u01ea\u01e8\3\2\2\2\u01eb\u01ed\t\34\2")
        buf.write("\2\u01ec\u01eb\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee\u01ec")
        buf.write("\3\2\2\2\u01ee\u01ef\3\2\2\2\u01ef\u00a8\3\2\2\2\u01f0")
        buf.write("\u01f2\t\34\2\2\u01f1\u01f0\3\2\2\2\u01f2\u01f3\3\2\2")
        buf.write("\2\u01f3\u01f1\3\2\2\2\u01f3\u01f4\3\2\2\2\u01f4\u01f6")
        buf.write("\3\2\2\2\u01f5\u01f7\7\60\2\2\u01f6\u01f5\3\2\2\2\u01f6")
        buf.write("\u01f7\3\2\2\2\u01f7\u01fb\3\2\2\2\u01f8\u01fa\t\34\2")
        buf.write("\2\u01f9\u01f8\3\2\2\2\u01fa\u01fd\3\2\2\2\u01fb\u01f9")
        buf.write("\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc\u020c\3\2\2\2\u01fd")
        buf.write("\u01fb\3\2\2\2\u01fe\u0200\t\34\2\2\u01ff\u01fe\3\2\2")
        buf.write("\2\u0200\u0201\3\2\2\2\u0201\u01ff\3\2\2\2\u0201\u0202")
        buf.write("\3\2\2\2\u0202\u0203\3\2\2\2\u0203\u0205\t\6\2\2\u0204")
        buf.write("\u0206\7/\2\2\u0205\u0204\3\2\2\2\u0205\u0206\3\2\2\2")
        buf.write("\u0206\u0208\3\2\2\2\u0207\u0209\t\34\2\2\u0208\u0207")
        buf.write("\3\2\2\2\u0209\u020a\3\2\2\2\u020a\u0208\3\2\2\2\u020a")
        buf.write("\u020b\3\2\2\2\u020b\u020d\3\2\2\2\u020c\u01ff\3\2\2\2")
        buf.write("\u020c\u020d\3\2\2\2\u020d\u0228\3\2\2\2\u020e\u0210\t")
        buf.write("\34\2\2\u020f\u020e\3\2\2\2\u0210\u0213\3\2\2\2\u0211")
        buf.write("\u020f\3\2\2\2\u0211\u0212\3\2\2\2\u0212\u0215\3\2\2\2")
        buf.write("\u0213\u0211\3\2\2\2\u0214\u0216\7\60\2\2\u0215\u0214")
        buf.write("\3\2\2\2\u0215\u0216\3\2\2\2\u0216\u0218\3\2\2\2\u0217")
        buf.write("\u0219\t\34\2\2\u0218\u0217\3\2\2\2\u0219\u021a\3\2\2")
        buf.write("\2\u021a\u0218\3\2\2\2\u021a\u021b\3\2\2\2\u021b\u0225")
        buf.write("\3\2\2\2\u021c\u021e\t\6\2\2\u021d\u021f\7/\2\2\u021e")
        buf.write("\u021d\3\2\2\2\u021e\u021f\3\2\2\2\u021f\u0221\3\2\2\2")
        buf.write("\u0220\u0222\t\34\2\2\u0221\u0220\3\2\2\2\u0222\u0223")
        buf.write("\3\2\2\2\u0223\u0221\3\2\2\2\u0223\u0224\3\2\2\2\u0224")
        buf.write("\u0226\3\2\2\2\u0225\u021c\3\2\2\2\u0225\u0226\3\2\2\2")
        buf.write("\u0226\u0228\3\2\2\2\u0227\u01f1\3\2\2\2\u0227\u0211\3")
        buf.write("\2\2\2\u0228\u00aa\3\2\2\2\u0229\u022a\7v\2\2\u022a\u022b")
        buf.write("\7t\2\2\u022b\u022c\7w\2\2\u022c\u0233\7g\2\2\u022d\u022e")
        buf.write("\7h\2\2\u022e\u022f\7c\2\2\u022f\u0230\7n\2\2\u0230\u0231")
        buf.write("\7u\2\2\u0231\u0233\7g\2\2\u0232\u0229\3\2\2\2\u0232\u022d")
        buf.write("\3\2\2\2\u0233\u00ac\3\2\2\2\u0234\u023a\7$\2\2\u0235")
        buf.write("\u0236\7^\2\2\u0236\u0239\t\37\2\2\u0237\u0239\n \2\2")
        buf.write("\u0238\u0235\3\2\2\2\u0238\u0237\3\2\2\2\u0239\u023c\3")
        buf.write("\2\2\2\u023a\u0238\3\2\2\2\u023a\u023b\3\2\2\2\u023b\u023d")
        buf.write("\3\2\2\2\u023c\u023a\3\2\2\2\u023d\u023e\7$\2\2\u023e")
        buf.write("\u00ae\3\2\2\2\u023f\u0245\5Y-\2\u0240\u0245\5[.\2\u0241")
        buf.write("\u0245\5W,\2\u0242\u0245\5]/\2\u0243\u0245\5S*\2\u0244")
        buf.write("\u023f\3\2\2\2\u0244\u0240\3\2\2\2\u0244\u0241\3\2\2\2")
        buf.write("\u0244\u0242\3\2\2\2\u0244\u0243\3\2\2\2\u0245\u00b0\3")
        buf.write("\2\2\2\u0246\u0249\5\u00b3Z\2\u0247\u0249\5\u00b9]\2\u0248")
        buf.write("\u0246\3\2\2\2\u0248\u0247\3\2\2\2\u0249\u00b2\3\2\2\2")
        buf.write("\u024a\u024d\5\u00b5[\2\u024b\u024d\5\u00b7\\\2\u024c")
        buf.write("\u024a\3\2\2\2\u024c\u024b\3\2\2\2\u024d\u00b4\3\2\2\2")
        buf.write("\u024e\u024f\7*\2\2\u024f\u0250\7,\2\2\u0250\u0254\3\2")
        buf.write("\2\2\u0251\u0253\13\2\2\2\u0252\u0251\3\2\2\2\u0253\u0256")
        buf.write("\3\2\2\2\u0254\u0255\3\2\2\2\u0254\u0252\3\2\2\2\u0255")
        buf.write("\u0257\3\2\2\2\u0256\u0254\3\2\2\2\u0257\u0258\7,\2\2")
        buf.write("\u0258\u0259\7+\2\2\u0259\u025a\3\2\2\2\u025a\u025b\b")
        buf.write("[\2\2\u025b\u00b6\3\2\2\2\u025c\u0260\7}\2\2\u025d\u025f")
        buf.write("\13\2\2\2\u025e\u025d\3\2\2\2\u025f\u0262\3\2\2\2\u0260")
        buf.write("\u0261\3\2\2\2\u0260\u025e\3\2\2\2\u0261\u0263\3\2\2\2")
        buf.write("\u0262\u0260\3\2\2\2\u0263\u0264\7\177\2\2\u0264\u0265")
        buf.write("\3\2\2\2\u0265\u0266\b\\\2\2\u0266\u00b8\3\2\2\2\u0267")
        buf.write("\u0268\7\61\2\2\u0268\u0269\7\61\2\2\u0269\u026d\3\2\2")
        buf.write("\2\u026a\u026c\n!\2\2\u026b\u026a\3\2\2\2\u026c\u026f")
        buf.write("\3\2\2\2\u026d\u026b\3\2\2\2\u026d\u026e\3\2\2\2\u026e")
        buf.write("\u00ba\3\2\2\2\u026f\u026d\3\2\2\2\u0270\u0271\13\2\2")
        buf.write("\2\u0271\u00bc\3\2\2\2\u0272\u0273\b_\3\2\u0273\u0279")
        buf.write("\7$\2\2\u0274\u0275\7^\2\2\u0275\u0278\t\37\2\2\u0276")
        buf.write("\u0278\n\"\2\2\u0277\u0274\3\2\2\2\u0277\u0276\3\2\2\2")
        buf.write("\u0278\u027b\3\2\2\2\u0279\u0277\3\2\2\2\u0279\u027a\3")
        buf.write("\2\2\2\u027a\u00be\3\2\2\2\u027b\u0279\3\2\2\2\u027c\u027d")
        buf.write("\b`\4\2\u027d\u0283\7$\2\2\u027e\u027f\7^\2\2\u027f\u0282")
        buf.write("\t\37\2\2\u0280\u0282\n \2\2\u0281\u027e\3\2\2\2\u0281")
        buf.write("\u0280\3\2\2\2\u0282\u0285\3\2\2\2\u0283\u0281\3\2\2\2")
        buf.write("\u0283\u0284\3\2\2\2\u0284\u0287\3\2\2\2\u0285\u0283\3")
        buf.write("\2\2\2\u0286\u0288\t\"\2\2\u0287\u0286\3\2\2\2\u0288\u0289")
        buf.write("\3\2\2\2\u0289\u0287\3\2\2\2\u0289\u028a\3\2\2\2\u028a")
        buf.write("\u0290\3\2\2\2\u028b\u028c\7^\2\2\u028c\u028f\t\37\2\2")
        buf.write("\u028d\u028f\n \2\2\u028e\u028b\3\2\2\2\u028e\u028d\3")
        buf.write("\2\2\2\u028f\u0292\3\2\2\2\u0290\u028e\3\2\2\2\u0290\u0291")
        buf.write("\3\2\2\2\u0291\u0294\3\2\2\2\u0292\u0290\3\2\2\2\u0293")
        buf.write("\u0295\7$\2\2\u0294\u0293\3\2\2\2\u0294\u0295\3\2\2\2")
        buf.write("\u0295\u00c0\3\2\2\2\u0296\u0298\t#\2\2\u0297\u0296\3")
        buf.write("\2\2\2\u0298\u0299\3\2\2\2\u0299\u0297\3\2\2\2\u0299\u029a")
        buf.write("\3\2\2\2\u029a\u029b\3\2\2\2\u029b\u029c\ba\2\2\u029c")
        buf.write("\u00c2\3\2\2\2*\2\u0175\u0183\u01e0\u01e3\u01e6\u01e8")
        buf.write("\u01ee\u01f3\u01f6\u01fb\u0201\u0205\u020a\u020c\u0211")
        buf.write("\u0215\u021a\u021e\u0223\u0225\u0227\u0232\u0238\u023a")
        buf.write("\u0244\u0248\u024c\u0254\u0260\u026d\u0277\u0279\u0281")
        buf.write("\u0283\u0289\u028e\u0290\u0294\u0299\5\b\2\2\3_\2\3`\3")
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
    ERROR_CHAR = 66
    UNCLOSE_STRING = 67
    ILLEGAL_ESCAPE = 68
    WS = 69

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
            "BLKCMT", "TRACMT", "BLCMT", "LINECMT", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "WS" ]

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
                  "CMT", "BLKCMT", "TRACMT", "BLCMT", "LINECMT", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "WS" ]

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
            actions[93] = self.UNCLOSE_STRING_action 
            actions[94] = self.ILLEGAL_ESCAPE_action 
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
     


