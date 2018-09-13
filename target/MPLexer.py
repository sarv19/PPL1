# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u0267\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\3")
        buf.write("\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b")
        buf.write("\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\16\3")
        buf.write("\16\3\17\3\17\3\17\3\20\3\20\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\23\3\23\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26\3\27")
        buf.write("\3\27\5\27\u00ed\n\27\3\30\3\30\3\30\3\30\3\30\3\30\3")
        buf.write("\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3%\3%\3%\3")
        buf.write("%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'")
        buf.write("\3\'\3\'\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*")
        buf.write("\3*\3*\3+\3+\3+\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3")
        buf.write("-\3.\3.\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3/\3/\3/\3\60\3")
        buf.write("\60\3\60\3\60\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\63")
        buf.write("\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3")
        buf.write("<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3")
        buf.write("E\3F\3F\3G\3G\3H\3H\3I\3I\3J\3J\3K\3K\3L\3L\3M\3M\3N\3")
        buf.write("N\3O\3O\3P\3P\3Q\6Q\u01c9\nQ\rQ\16Q\u01ca\3Q\3Q\3R\5R")
        buf.write("\u01d0\nR\3R\7R\u01d3\nR\fR\16R\u01d6\13R\3S\6S\u01d9")
        buf.write("\nS\rS\16S\u01da\3T\6T\u01de\nT\rT\16T\u01df\3T\5T\u01e3")
        buf.write("\nT\3T\7T\u01e6\nT\fT\16T\u01e9\13T\3T\7T\u01ec\nT\fT")
        buf.write("\16T\u01ef\13T\3T\3T\5T\u01f3\nT\3T\6T\u01f6\nT\rT\16")
        buf.write("T\u01f7\5T\u01fa\nT\3T\7T\u01fd\nT\fT\16T\u0200\13T\3")
        buf.write("T\5T\u0203\nT\3T\6T\u0206\nT\rT\16T\u0207\3T\3T\5T\u020c")
        buf.write("\nT\3T\6T\u020f\nT\rT\16T\u0210\5T\u0213\nT\5T\u0215\n")
        buf.write("T\3U\3U\3U\3U\7U\u021b\nU\fU\16U\u021e\13U\3U\3U\3U\3")
        buf.write("V\3V\5V\u0225\nV\3V\3V\3W\3W\5W\u022b\nW\3X\3X\3X\3X\7")
        buf.write("X\u0231\nX\fX\16X\u0234\13X\3X\3X\3X\3Y\3Y\7Y\u023b\n")
        buf.write("Y\fY\16Y\u023e\13Y\3Y\3Y\3Z\3Z\3Z\3Z\7Z\u0246\nZ\fZ\16")
        buf.write("Z\u0249\13Z\3[\3[\3[\5[\u024e\n[\3[\7[\u0251\n[\f[\16")
        buf.write("[\u0254\13[\3[\3[\3\\\3\\\3\\\3\\\7\\\u025c\n\\\f\\\16")
        buf.write("\\\u025f\13\\\3\\\3\\\3\\\3\\\3]\3]\3]\4\u0232\u023c\2")
        buf.write("^\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31")
        buf.write("\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O")
        buf.write(")Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\2m\2o\2q\2")
        buf.write("s\2u\2w\2y\2{\2}\2\177\2\u0081\2\u0083\2\u0085\2\u0087")
        buf.write("\2\u0089\2\u008b\2\u008d\2\u008f\2\u0091\2\u0093\2\u0095")
        buf.write("\2\u0097\2\u0099\2\u009b\2\u009d\2\u009f\2\u00a1\67\u00a3")
        buf.write("8\u00a59\u00a7:\u00a9;\u00ab<\u00ad=\u00af>\u00b1?\u00b3")
        buf.write("@\u00b5A\u00b7B\u00b9C\3\2$\4\2CCcc\4\2DDdd\4\2EEee\4")
        buf.write("\2FFff\4\2GGgg\4\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4\2LLl")
        buf.write("l\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2")
        buf.write("SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4")
        buf.write("\2ZZzz\4\2[[{{\4\2\\\\||\3\2\62;\5\2\13\f\17\17\"\"\5")
        buf.write("\2C\\aac|\6\2\62;C\\aac|\n\2$$))^^ddhhppttvv\7\2\n\f\16")
        buf.write("\17$$))^^\4\2\f\f\17\17\7\2\13\f\16\17$$))^^\2\u0268\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%")
        buf.write("\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5")
        buf.write("\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2")
        buf.write("\2\2\u00ad\3\2\2\2\2\u00af\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3")
        buf.write("\3\2\2\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2\2\2\u00b9\3\2\2")
        buf.write("\2\3\u00bb\3\2\2\2\5\u00bd\3\2\2\2\7\u00bf\3\2\2\2\t\u00c1")
        buf.write("\3\2\2\2\13\u00c3\3\2\2\2\r\u00c5\3\2\2\2\17\u00c7\3\2")
        buf.write("\2\2\21\u00c9\3\2\2\2\23\u00cb\3\2\2\2\25\u00cd\3\2\2")
        buf.write("\2\27\u00cf\3\2\2\2\31\u00d2\3\2\2\2\33\u00d4\3\2\2\2")
        buf.write("\35\u00d6\3\2\2\2\37\u00d9\3\2\2\2!\u00db\3\2\2\2#\u00de")
        buf.write("\3\2\2\2%\u00e0\3\2\2\2\'\u00e2\3\2\2\2)\u00e4\3\2\2\2")
        buf.write("+\u00e7\3\2\2\2-\u00ec\3\2\2\2/\u00ee\3\2\2\2\61\u00f4")
        buf.write("\3\2\2\2\63\u00fd\3\2\2\2\65\u0101\3\2\2\2\67\u0104\3")
        buf.write("\2\2\29\u010b\3\2\2\2;\u010e\3\2\2\2=\u0111\3\2\2\2?\u0116")
        buf.write("\3\2\2\2A\u011b\3\2\2\2C\u0122\3\2\2\2E\u0128\3\2\2\2")
        buf.write("G\u012e\3\2\2\2I\u0132\3\2\2\2K\u013b\3\2\2\2M\u0145\3")
        buf.write("\2\2\2O\u0149\3\2\2\2Q\u014e\3\2\2\2S\u0154\3\2\2\2U\u015a")
        buf.write("\3\2\2\2W\u015d\3\2\2\2Y\u0162\3\2\2\2[\u016a\3\2\2\2")
        buf.write("]\u0172\3\2\2\2_\u0179\3\2\2\2a\u017d\3\2\2\2c\u0181\3")
        buf.write("\2\2\2e\u0184\3\2\2\2g\u0188\3\2\2\2i\u018c\3\2\2\2k\u0191")
        buf.write("\3\2\2\2m\u0193\3\2\2\2o\u0195\3\2\2\2q\u0197\3\2\2\2")
        buf.write("s\u0199\3\2\2\2u\u019b\3\2\2\2w\u019d\3\2\2\2y\u019f\3")
        buf.write("\2\2\2{\u01a1\3\2\2\2}\u01a3\3\2\2\2\177\u01a5\3\2\2\2")
        buf.write("\u0081\u01a7\3\2\2\2\u0083\u01a9\3\2\2\2\u0085\u01ab\3")
        buf.write("\2\2\2\u0087\u01ad\3\2\2\2\u0089\u01af\3\2\2\2\u008b\u01b1")
        buf.write("\3\2\2\2\u008d\u01b3\3\2\2\2\u008f\u01b5\3\2\2\2\u0091")
        buf.write("\u01b7\3\2\2\2\u0093\u01b9\3\2\2\2\u0095\u01bb\3\2\2\2")
        buf.write("\u0097\u01bd\3\2\2\2\u0099\u01bf\3\2\2\2\u009b\u01c1\3")
        buf.write("\2\2\2\u009d\u01c3\3\2\2\2\u009f\u01c5\3\2\2\2\u00a1\u01c8")
        buf.write("\3\2\2\2\u00a3\u01cf\3\2\2\2\u00a5\u01d8\3\2\2\2\u00a7")
        buf.write("\u0214\3\2\2\2\u00a9\u0216\3\2\2\2\u00ab\u0224\3\2\2\2")
        buf.write("\u00ad\u022a\3\2\2\2\u00af\u022c\3\2\2\2\u00b1\u0238\3")
        buf.write("\2\2\2\u00b3\u0241\3\2\2\2\u00b5\u024a\3\2\2\2\u00b7\u0257")
        buf.write("\3\2\2\2\u00b9\u0264\3\2\2\2\u00bb\u00bc\7*\2\2\u00bc")
        buf.write("\4\3\2\2\2\u00bd\u00be\7+\2\2\u00be\6\3\2\2\2\u00bf\u00c0")
        buf.write("\7}\2\2\u00c0\b\3\2\2\2\u00c1\u00c2\7\177\2\2\u00c2\n")
        buf.write("\3\2\2\2\u00c3\u00c4\7]\2\2\u00c4\f\3\2\2\2\u00c5\u00c6")
        buf.write("\7_\2\2\u00c6\16\3\2\2\2\u00c7\u00c8\7=\2\2\u00c8\20\3")
        buf.write("\2\2\2\u00c9\u00ca\7.\2\2\u00ca\22\3\2\2\2\u00cb\u00cc")
        buf.write("\7?\2\2\u00cc\24\3\2\2\2\u00cd\u00ce\7<\2\2\u00ce\26\3")
        buf.write("\2\2\2\u00cf\u00d0\7\60\2\2\u00d0\u00d1\7\60\2\2\u00d1")
        buf.write("\30\3\2\2\2\u00d2\u00d3\7-\2\2\u00d3\32\3\2\2\2\u00d4")
        buf.write("\u00d5\7,\2\2\u00d5\34\3\2\2\2\u00d6\u00d7\7>\2\2\u00d7")
        buf.write("\u00d8\7@\2\2\u00d8\36\3\2\2\2\u00d9\u00da\7>\2\2\u00da")
        buf.write(" \3\2\2\2\u00db\u00dc\7>\2\2\u00dc\u00dd\7?\2\2\u00dd")
        buf.write("\"\3\2\2\2\u00de\u00df\7/\2\2\u00df$\3\2\2\2\u00e0\u00e1")
        buf.write("\7\61\2\2\u00e1&\3\2\2\2\u00e2\u00e3\7@\2\2\u00e3(\3\2")
        buf.write("\2\2\u00e4\u00e5\7@\2\2\u00e5\u00e6\7?\2\2\u00e6*\3\2")
        buf.write("\2\2\u00e7\u00e8\7<\2\2\u00e8\u00e9\7?\2\2\u00e9,\3\2")
        buf.write("\2\2\u00ea\u00ed\5O(\2\u00eb\u00ed\5Q)\2\u00ec\u00ea\3")
        buf.write("\2\2\2\u00ec\u00eb\3\2\2\2\u00ed.\3\2\2\2\u00ee\u00ef")
        buf.write("\5m\67\2\u00ef\u00f0\5\u008dG\2\u00f0\u00f1\5s:\2\u00f1")
        buf.write("\u00f2\5k\66\2\u00f2\u00f3\5\177@\2\u00f3\60\3\2\2\2\u00f4")
        buf.write("\u00f5\5o8\2\u00f5\u00f6\5\u0087D\2\u00f6\u00f7\5\u0085")
        buf.write("C\2\u00f7\u00f8\5\u0091I\2\u00f8\u00f9\5{>\2\u00f9\u00fa")
        buf.write("\5\u0085C\2\u00fa\u00fb\5\u0093J\2\u00fb\u00fc\5s:\2\u00fc")
        buf.write("\62\3\2\2\2\u00fd\u00fe\5u;\2\u00fe\u00ff\5\u0087D\2\u00ff")
        buf.write("\u0100\5\u008dG\2\u0100\64\3\2\2\2\u0101\u0102\5\u0091")
        buf.write("I\2\u0102\u0103\5\u0087D\2\u0103\66\3\2\2\2\u0104\u0105")
        buf.write("\5q9\2\u0105\u0106\5\u0087D\2\u0106\u0107\5\u0097L\2\u0107")
        buf.write("\u0108\5\u0085C\2\u0108\u0109\5\u0091I\2\u0109\u010a\5")
        buf.write("\u0087D\2\u010a8\3\2\2\2\u010b\u010c\5q9\2\u010c\u010d")
        buf.write("\5\u0087D\2\u010d:\3\2\2\2\u010e\u010f\5{>\2\u010f\u0110")
        buf.write("\5u;\2\u0110<\3\2\2\2\u0111\u0112\5\u0091I\2\u0112\u0113")
        buf.write("\5y=\2\u0113\u0114\5s:\2\u0114\u0115\5\u0085C\2\u0115")
        buf.write(">\3\2\2\2\u0116\u0117\5s:\2\u0117\u0118\5\u0081A\2\u0118")
        buf.write("\u0119\5\u008fH\2\u0119\u011a\5s:\2\u011a@\3\2\2\2\u011b")
        buf.write("\u011c\5\u008dG\2\u011c\u011d\5s:\2\u011d\u011e\5\u0091")
        buf.write("I\2\u011e\u011f\5\u0093J\2\u011f\u0120\5\u008dG\2\u0120")
        buf.write("\u0121\5\u0085C\2\u0121B\3\2\2\2\u0122\u0123\5\u0097L")
        buf.write("\2\u0123\u0124\5y=\2\u0124\u0125\5{>\2\u0125\u0126\5\u0081")
        buf.write("A\2\u0126\u0127\5s:\2\u0127D\3\2\2\2\u0128\u0129\5m\67")
        buf.write("\2\u0129\u012a\5s:\2\u012a\u012b\5w<\2\u012b\u012c\5{")
        buf.write(">\2\u012c\u012d\5\u0085C\2\u012dF\3\2\2\2\u012e\u012f")
        buf.write("\5s:\2\u012f\u0130\5\u0085C\2\u0130\u0131\5q9\2\u0131")
        buf.write("H\3\2\2\2\u0132\u0133\5u;\2\u0133\u0134\5\u0093J\2\u0134")
        buf.write("\u0135\5\u0085C\2\u0135\u0136\5o8\2\u0136\u0137\5\u0091")
        buf.write("I\2\u0137\u0138\5{>\2\u0138\u0139\5\u0087D\2\u0139\u013a")
        buf.write("\5\u0085C\2\u013aJ\3\2\2\2\u013b\u013c\5\u0089E\2\u013c")
        buf.write("\u013d\5\u008dG\2\u013d\u013e\5\u0087D\2\u013e\u013f\5")
        buf.write("o8\2\u013f\u0140\5s:\2\u0140\u0141\5q9\2\u0141\u0142\5")
        buf.write("\u0093J\2\u0142\u0143\5\u008dG\2\u0143\u0144\5s:\2\u0144")
        buf.write("L\3\2\2\2\u0145\u0146\5\u0095K\2\u0146\u0147\5k\66\2\u0147")
        buf.write("\u0148\5\u008dG\2\u0148N\3\2\2\2\u0149\u014a\5\u0091I")
        buf.write("\2\u014a\u014b\5\u008dG\2\u014b\u014c\5\u0093J\2\u014c")
        buf.write("\u014d\5s:\2\u014dP\3\2\2\2\u014e\u014f\5u;\2\u014f\u0150")
        buf.write("\5k\66\2\u0150\u0151\5\u0081A\2\u0151\u0152\5\u008fH\2")
        buf.write("\u0152\u0153\5s:\2\u0153R\3\2\2\2\u0154\u0155\5k\66\2")
        buf.write("\u0155\u0156\5\u008dG\2\u0156\u0157\5\u008dG\2\u0157\u0158")
        buf.write("\5k\66\2\u0158\u0159\5\u009bN\2\u0159T\3\2\2\2\u015a\u015b")
        buf.write("\5\u0087D\2\u015b\u015c\5u;\2\u015cV\3\2\2\2\u015d\u015e")
        buf.write("\5\u008dG\2\u015e\u015f\5s:\2\u015f\u0160\5k\66\2\u0160")
        buf.write("\u0161\5\u0081A\2\u0161X\3\2\2\2\u0162\u0163\5m\67\2\u0163")
        buf.write("\u0164\5\u0087D\2\u0164\u0165\5\u0087D\2\u0165\u0166\5")
        buf.write("\u0081A\2\u0166\u0167\5s:\2\u0167\u0168\5k\66\2\u0168")
        buf.write("\u0169\5\u0085C\2\u0169Z\3\2\2\2\u016a\u016b\5{>\2\u016b")
        buf.write("\u016c\5\u0085C\2\u016c\u016d\5\u0091I\2\u016d\u016e\5")
        buf.write("s:\2\u016e\u016f\5w<\2\u016f\u0170\5s:\2\u0170\u0171\5")
        buf.write("\u008dG\2\u0171\\\3\2\2\2\u0172\u0173\5\u008fH\2\u0173")
        buf.write("\u0174\5\u0091I\2\u0174\u0175\5\u008dG\2\u0175\u0176\5")
        buf.write("{>\2\u0176\u0177\5\u0085C\2\u0177\u0178\5w<\2\u0178^\3")
        buf.write("\2\2\2\u0179\u017a\5\u0085C\2\u017a\u017b\5\u0087D\2\u017b")
        buf.write("\u017c\5\u0091I\2\u017c`\3\2\2\2\u017d\u017e\5k\66\2\u017e")
        buf.write("\u017f\5\u0085C\2\u017f\u0180\5q9\2\u0180b\3\2\2\2\u0181")
        buf.write("\u0182\5\u0087D\2\u0182\u0183\5\u008dG\2\u0183d\3\2\2")
        buf.write("\2\u0184\u0185\5q9\2\u0185\u0186\5{>\2\u0186\u0187\5\u0095")
        buf.write("K\2\u0187f\3\2\2\2\u0188\u0189\5\u0083B\2\u0189\u018a")
        buf.write("\5\u0087D\2\u018a\u018b\5q9\2\u018bh\3\2\2\2\u018c\u018d")
        buf.write("\5\u0097L\2\u018d\u018e\5{>\2\u018e\u018f\5\u0091I\2\u018f")
        buf.write("\u0190\5y=\2\u0190j\3\2\2\2\u0191\u0192\t\2\2\2\u0192")
        buf.write("l\3\2\2\2\u0193\u0194\t\3\2\2\u0194n\3\2\2\2\u0195\u0196")
        buf.write("\t\4\2\2\u0196p\3\2\2\2\u0197\u0198\t\5\2\2\u0198r\3\2")
        buf.write("\2\2\u0199\u019a\t\6\2\2\u019at\3\2\2\2\u019b\u019c\t")
        buf.write("\7\2\2\u019cv\3\2\2\2\u019d\u019e\t\b\2\2\u019ex\3\2\2")
        buf.write("\2\u019f\u01a0\t\t\2\2\u01a0z\3\2\2\2\u01a1\u01a2\t\n")
        buf.write("\2\2\u01a2|\3\2\2\2\u01a3\u01a4\t\13\2\2\u01a4~\3\2\2")
        buf.write("\2\u01a5\u01a6\t\f\2\2\u01a6\u0080\3\2\2\2\u01a7\u01a8")
        buf.write("\t\r\2\2\u01a8\u0082\3\2\2\2\u01a9\u01aa\t\16\2\2\u01aa")
        buf.write("\u0084\3\2\2\2\u01ab\u01ac\t\17\2\2\u01ac\u0086\3\2\2")
        buf.write("\2\u01ad\u01ae\t\20\2\2\u01ae\u0088\3\2\2\2\u01af\u01b0")
        buf.write("\t\21\2\2\u01b0\u008a\3\2\2\2\u01b1\u01b2\t\22\2\2\u01b2")
        buf.write("\u008c\3\2\2\2\u01b3\u01b4\t\23\2\2\u01b4\u008e\3\2\2")
        buf.write("\2\u01b5\u01b6\t\24\2\2\u01b6\u0090\3\2\2\2\u01b7\u01b8")
        buf.write("\t\25\2\2\u01b8\u0092\3\2\2\2\u01b9\u01ba\t\26\2\2\u01ba")
        buf.write("\u0094\3\2\2\2\u01bb\u01bc\t\27\2\2\u01bc\u0096\3\2\2")
        buf.write("\2\u01bd\u01be\t\30\2\2\u01be\u0098\3\2\2\2\u01bf\u01c0")
        buf.write("\t\31\2\2\u01c0\u009a\3\2\2\2\u01c1\u01c2\t\32\2\2\u01c2")
        buf.write("\u009c\3\2\2\2\u01c3\u01c4\t\33\2\2\u01c4\u009e\3\2\2")
        buf.write("\2\u01c5\u01c6\t\34\2\2\u01c6\u00a0\3\2\2\2\u01c7\u01c9")
        buf.write("\t\35\2\2\u01c8\u01c7\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca")
        buf.write("\u01c8\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb\u01cc\3\2\2\2")
        buf.write("\u01cc\u01cd\bQ\2\2\u01cd\u00a2\3\2\2\2\u01ce\u01d0\t")
        buf.write("\36\2\2\u01cf\u01ce\3\2\2\2\u01d0\u01d4\3\2\2\2\u01d1")
        buf.write("\u01d3\t\37\2\2\u01d2\u01d1\3\2\2\2\u01d3\u01d6\3\2\2")
        buf.write("\2\u01d4\u01d2\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5\u00a4")
        buf.write("\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d7\u01d9\t\34\2\2\u01d8")
        buf.write("\u01d7\3\2\2\2\u01d9\u01da\3\2\2\2\u01da\u01d8\3\2\2\2")
        buf.write("\u01da\u01db\3\2\2\2\u01db\u00a6\3\2\2\2\u01dc\u01de\t")
        buf.write("\34\2\2\u01dd\u01dc\3\2\2\2\u01de\u01df\3\2\2\2\u01df")
        buf.write("\u01dd\3\2\2\2\u01df\u01e0\3\2\2\2\u01e0\u01e2\3\2\2\2")
        buf.write("\u01e1\u01e3\7\60\2\2\u01e2\u01e1\3\2\2\2\u01e2\u01e3")
        buf.write("\3\2\2\2\u01e3\u01e7\3\2\2\2\u01e4\u01e6\t\34\2\2\u01e5")
        buf.write("\u01e4\3\2\2\2\u01e6\u01e9\3\2\2\2\u01e7\u01e5\3\2\2\2")
        buf.write("\u01e7\u01e8\3\2\2\2\u01e8\u01f9\3\2\2\2\u01e9\u01e7\3")
        buf.write("\2\2\2\u01ea\u01ec\t\34\2\2\u01eb\u01ea\3\2\2\2\u01ec")
        buf.write("\u01ef\3\2\2\2\u01ed\u01eb\3\2\2\2\u01ed\u01ee\3\2\2\2")
        buf.write("\u01ee\u01f0\3\2\2\2\u01ef\u01ed\3\2\2\2\u01f0\u01f2\t")
        buf.write("\6\2\2\u01f1\u01f3\7/\2\2\u01f2\u01f1\3\2\2\2\u01f2\u01f3")
        buf.write("\3\2\2\2\u01f3\u01f5\3\2\2\2\u01f4\u01f6\t\34\2\2\u01f5")
        buf.write("\u01f4\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7\u01f5\3\2\2\2")
        buf.write("\u01f7\u01f8\3\2\2\2\u01f8\u01fa\3\2\2\2\u01f9\u01ed\3")
        buf.write("\2\2\2\u01f9\u01fa\3\2\2\2\u01fa\u0215\3\2\2\2\u01fb\u01fd")
        buf.write("\t\34\2\2\u01fc\u01fb\3\2\2\2\u01fd\u0200\3\2\2\2\u01fe")
        buf.write("\u01fc\3\2\2\2\u01fe\u01ff\3\2\2\2\u01ff\u0202\3\2\2\2")
        buf.write("\u0200\u01fe\3\2\2\2\u0201\u0203\7\60\2\2\u0202\u0201")
        buf.write("\3\2\2\2\u0202\u0203\3\2\2\2\u0203\u0205\3\2\2\2\u0204")
        buf.write("\u0206\t\34\2\2\u0205\u0204\3\2\2\2\u0206\u0207\3\2\2")
        buf.write("\2\u0207\u0205\3\2\2\2\u0207\u0208\3\2\2\2\u0208\u0212")
        buf.write("\3\2\2\2\u0209\u020b\t\6\2\2\u020a\u020c\7/\2\2\u020b")
        buf.write("\u020a\3\2\2\2\u020b\u020c\3\2\2\2\u020c\u020e\3\2\2\2")
        buf.write("\u020d\u020f\t\34\2\2\u020e\u020d\3\2\2\2\u020f\u0210")
        buf.write("\3\2\2\2\u0210\u020e\3\2\2\2\u0210\u0211\3\2\2\2\u0211")
        buf.write("\u0213\3\2\2\2\u0212\u0209\3\2\2\2\u0212\u0213\3\2\2\2")
        buf.write("\u0213\u0215\3\2\2\2\u0214\u01dd\3\2\2\2\u0214\u01fe\3")
        buf.write("\2\2\2\u0215\u00a8\3\2\2\2\u0216\u021c\7$\2\2\u0217\u0218")
        buf.write("\7^\2\2\u0218\u021b\t \2\2\u0219\u021b\n!\2\2\u021a\u0217")
        buf.write("\3\2\2\2\u021a\u0219\3\2\2\2\u021b\u021e\3\2\2\2\u021c")
        buf.write("\u021a\3\2\2\2\u021c\u021d\3\2\2\2\u021d\u021f\3\2\2\2")
        buf.write("\u021e\u021c\3\2\2\2\u021f\u0220\7$\2\2\u0220\u0221\b")
        buf.write("U\3\2\u0221\u00aa\3\2\2\2\u0222\u0225\5\u00adW\2\u0223")
        buf.write("\u0225\5\u00b3Z\2\u0224\u0222\3\2\2\2\u0224\u0223\3\2")
        buf.write("\2\2\u0225\u0226\3\2\2\2\u0226\u0227\bV\2\2\u0227\u00ac")
        buf.write("\3\2\2\2\u0228\u022b\5\u00afX\2\u0229\u022b\5\u00b1Y\2")
        buf.write("\u022a\u0228\3\2\2\2\u022a\u0229\3\2\2\2\u022b\u00ae\3")
        buf.write("\2\2\2\u022c\u022d\7*\2\2\u022d\u022e\7,\2\2\u022e\u0232")
        buf.write("\3\2\2\2\u022f\u0231\13\2\2\2\u0230\u022f\3\2\2\2\u0231")
        buf.write("\u0234\3\2\2\2\u0232\u0233\3\2\2\2\u0232\u0230\3\2\2\2")
        buf.write("\u0233\u0235\3\2\2\2\u0234\u0232\3\2\2\2\u0235\u0236\7")
        buf.write(",\2\2\u0236\u0237\7+\2\2\u0237\u00b0\3\2\2\2\u0238\u023c")
        buf.write("\7}\2\2\u0239\u023b\13\2\2\2\u023a\u0239\3\2\2\2\u023b")
        buf.write("\u023e\3\2\2\2\u023c\u023d\3\2\2\2\u023c\u023a\3\2\2\2")
        buf.write("\u023d\u023f\3\2\2\2\u023e\u023c\3\2\2\2\u023f\u0240\7")
        buf.write("\177\2\2\u0240\u00b2\3\2\2\2\u0241\u0242\7\61\2\2\u0242")
        buf.write("\u0243\7\61\2\2\u0243\u0247\3\2\2\2\u0244\u0246\n\"\2")
        buf.write("\2\u0245\u0244\3\2\2\2\u0246\u0249\3\2\2\2\u0247\u0245")
        buf.write("\3\2\2\2\u0247\u0248\3\2\2\2\u0248\u00b4\3\2\2\2\u0249")
        buf.write("\u0247\3\2\2\2\u024a\u0252\7$\2\2\u024b\u024d\7^\2\2\u024c")
        buf.write("\u024e\t \2\2\u024d\u024c\3\2\2\2\u024e\u0251\3\2\2\2")
        buf.write("\u024f\u0251\n!\2\2\u0250\u024b\3\2\2\2\u0250\u024f\3")
        buf.write("\2\2\2\u0251\u0254\3\2\2\2\u0252\u0250\3\2\2\2\u0252\u0253")
        buf.write("\3\2\2\2\u0253\u0255\3\2\2\2\u0254\u0252\3\2\2\2\u0255")
        buf.write("\u0256\b[\4\2\u0256\u00b6\3\2\2\2\u0257\u025d\7$\2\2\u0258")
        buf.write("\u025c\n#\2\2\u0259\u025a\7^\2\2\u025a\u025c\t \2\2\u025b")
        buf.write("\u0258\3\2\2\2\u025b\u0259\3\2\2\2\u025c\u025f\3\2\2\2")
        buf.write("\u025d\u025b\3\2\2\2\u025d\u025e\3\2\2\2\u025e\u0260\3")
        buf.write("\2\2\2\u025f\u025d\3\2\2\2\u0260\u0261\7^\2\2\u0261\u0262")
        buf.write("\n \2\2\u0262\u0263\b\\\5\2\u0263\u00b8\3\2\2\2\u0264")
        buf.write("\u0265\13\2\2\2\u0265\u0266\b]\6\2\u0266\u00ba\3\2\2\2")
        buf.write("#\2\u00ec\u01ca\u01cf\u01d2\u01d4\u01da\u01df\u01e2\u01e7")
        buf.write("\u01ed\u01f2\u01f7\u01f9\u01fe\u0202\u0207\u020b\u0210")
        buf.write("\u0212\u0214\u021a\u021c\u0224\u022a\u0232\u023c\u0247")
        buf.write("\u024d\u0250\u0252\u025b\u025d\7\b\2\2\3U\2\3[\3\3\\\4")
        buf.write("\3]\5")
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
    BOOLLIT = 22
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
    WITH = 52
    WS = 53
    ID = 54
    INTLIT = 55
    REALLIT = 56
    STRINGLIT = 57
    CMT = 58
    BLKCMT = 59
    TRACMT = 60
    BLCMT = 61
    LINECMT = 62
    UNCLOSE_STRING = 63
    ILLEGAL_ESCAPE = 64
    ERROR_CHAR = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "','", "'='", 
            "':'", "'..'", "'+'", "'*'", "'<>'", "'<'", "'<='", "'-'", "'/'", 
            "'>'", "'>='", "':='" ]

    symbolicNames = [ "<INVALID>",
            "LB", "RB", "LP", "RP", "LQ", "RQ", "SEMI", "CM", "EQ", "COL", 
            "DD", "ADD", "MUL", "NOTEQ", "LESSTN", "LESSEQ", "SUBNE", "DIVSI", 
            "GRETN", "GREEQ", "ASSI", "BOOLLIT", "BREAK", "CONTINUE", "FOR", 
            "TO", "DOWNTO", "DO", "IF", "THEN", "ELSE", "RETURN", "WHILE", 
            "BEGIN", "END", "FUNCTION", "PROCEDURE", "VAR", "TRUE", "FALSE", 
            "ARRAY", "OF", "REAL", "BOOLEAN", "INTEGER", "STRING", "NOT", 
            "AND", "OR", "DIV", "MOD", "WITH", "WS", "ID", "INTLIT", "REALLIT", 
            "STRINGLIT", "CMT", "BLKCMT", "TRACMT", "BLCMT", "LINECMT", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "LB", "RB", "LP", "RP", "LQ", "RQ", "SEMI", "CM", "EQ", 
                  "COL", "DD", "ADD", "MUL", "NOTEQ", "LESSTN", "LESSEQ", 
                  "SUBNE", "DIVSI", "GRETN", "GREEQ", "ASSI", "BOOLLIT", 
                  "BREAK", "CONTINUE", "FOR", "TO", "DOWNTO", "DO", "IF", 
                  "THEN", "ELSE", "RETURN", "WHILE", "BEGIN", "END", "FUNCTION", 
                  "PROCEDURE", "VAR", "TRUE", "FALSE", "ARRAY", "OF", "REAL", 
                  "BOOLEAN", "INTEGER", "STRING", "NOT", "AND", "OR", "DIV", 
                  "MOD", "WITH", "A", "B", "C", "D", "E", "F", "G", "H", 
                  "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", 
                  "T", "U", "V", "W", "X", "Y", "Z", "NUM", "WS", "ID", 
                  "INTLIT", "REALLIT", "STRINGLIT", "CMT", "BLKCMT", "TRACMT", 
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
            actions[89] = self.UNCLOSE_STRING_action 
            actions[90] = self.ILLEGAL_ESCAPE_action 
            actions[91] = self.ERROR_CHAR_action 
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
     


