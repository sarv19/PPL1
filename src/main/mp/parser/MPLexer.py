# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u026c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\6\27\u00ed\n\27\r\27\16\27\u00ee\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3!\3!\3!\3!\3")
        buf.write("!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3$\3")
        buf.write("$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3")
        buf.write("&\3&\3&\3&\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3)\3)\3)\3)")
        buf.write("\3)\3)\3*\3*\3*\3*\3*\3*\3+\3+\3+\3,\3,\3,\3,\3,\3-\3")
        buf.write("-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u0174\n-\3.\3.\3")
        buf.write(".\3.\3.\3.\3.\3.\3.\3.\3.\3.\5.\u0182\n.\3/\3/\3/\3/\3")
        buf.write("/\3/\3/\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\62\3")
        buf.write("\62\3\62\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\65")
        buf.write("\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3")
        buf.write("<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3")
        buf.write("E\3F\3F\3G\3G\3H\3H\3I\3I\3J\3J\3K\3K\3L\3L\3M\3M\3N\3")
        buf.write("N\3O\3O\3P\6P\u01d5\nP\rP\16P\u01d6\3Q\5Q\u01da\nQ\3Q")
        buf.write("\7Q\u01dd\nQ\fQ\16Q\u01e0\13Q\3R\6R\u01e3\nR\rR\16R\u01e4")
        buf.write("\3S\6S\u01e8\nS\rS\16S\u01e9\3S\5S\u01ed\nS\3S\7S\u01f0")
        buf.write("\nS\fS\16S\u01f3\13S\3S\6S\u01f6\nS\rS\16S\u01f7\3S\3")
        buf.write("S\5S\u01fc\nS\3S\6S\u01ff\nS\rS\16S\u0200\5S\u0203\nS")
        buf.write("\3S\7S\u0206\nS\fS\16S\u0209\13S\3S\5S\u020c\nS\3S\6S")
        buf.write("\u020f\nS\rS\16S\u0210\3S\3S\5S\u0215\nS\3S\6S\u0218\n")
        buf.write("S\rS\16S\u0219\5S\u021c\nS\5S\u021e\nS\3T\3T\3T\3T\3T")
        buf.write("\3T\3T\3T\3T\5T\u0229\nT\3U\3U\3U\3U\7U\u022f\nU\fU\16")
        buf.write("U\u0232\13U\3U\3U\3V\3V\3V\3V\3V\5V\u023b\nV\3W\3W\5W")
        buf.write("\u023f\nW\3X\3X\5X\u0243\nX\3Y\3Y\3Y\3Y\7Y\u0249\nY\f")
        buf.write("Y\16Y\u024c\13Y\3Y\3Y\3Y\3Y\3Y\3Z\3Z\7Z\u0255\nZ\fZ\16")
        buf.write("Z\u0258\13Z\3Z\3Z\3Z\3Z\3[\3[\3[\3[\7[\u0262\n[\f[\16")
        buf.write("[\u0265\13[\3\\\3\\\3]\3]\3^\3^\4\u024a\u0256\2_\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33")
        buf.write("\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32")
        buf.write("\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U")
        buf.write(",W-Y.[/]\60_\61a\62c\63e\64g\65i\2k\2m\2o\2q\2s\2u\2w")
        buf.write("\2y\2{\2}\2\177\2\u0081\2\u0083\2\u0085\2\u0087\2\u0089")
        buf.write("\2\u008b\2\u008d\2\u008f\2\u0091\2\u0093\2\u0095\2\u0097")
        buf.write("\2\u0099\2\u009b\2\u009d\2\u009f\66\u00a1\67\u00a38\u00a5")
        buf.write("9\u00a7:\u00a9;\u00ab<\u00ad=\u00af>\u00b1?\u00b3@\u00b5")
        buf.write("A\u00b7B\u00b9C\u00bbD\3\2#\5\2\13\f\17\17\"\"\4\2CCc")
        buf.write("c\4\2DDdd\4\2EEee\4\2FFff\4\2GGgg\4\2HHhh\4\2IIii\4\2")
        buf.write("JJjj\4\2KKkk\4\2LLll\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4")
        buf.write("\2QQqq\4\2RRrr\4\2SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2WWw")
        buf.write("w\4\2XXxx\4\2YYyy\4\2ZZzz\4\2[[{{\4\2\\\\||\3\2\62;\5")
        buf.write("\2C\\aac|\6\2\62;C\\aac|\n\2$$))^^ddhhppttvv\7\2\n\f\16")
        buf.write("\17$$))^^\4\2\f\f\17\17\2\u0270\2\3\3\2\2\2\2\5\3\2\2")
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
        buf.write("\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2\u009f\3\2\2")
        buf.write("\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7")
        buf.write("\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2")
        buf.write("\2\2\u00af\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2\2\2\u00b5")
        buf.write("\3\2\2\2\2\u00b7\3\2\2\2\2\u00b9\3\2\2\2\2\u00bb\3\2\2")
        buf.write("\2\3\u00bd\3\2\2\2\5\u00bf\3\2\2\2\7\u00c1\3\2\2\2\t\u00c3")
        buf.write("\3\2\2\2\13\u00c5\3\2\2\2\r\u00c7\3\2\2\2\17\u00c9\3\2")
        buf.write("\2\2\21\u00cb\3\2\2\2\23\u00cd\3\2\2\2\25\u00cf\3\2\2")
        buf.write("\2\27\u00d1\3\2\2\2\31\u00d4\3\2\2\2\33\u00d6\3\2\2\2")
        buf.write("\35\u00d8\3\2\2\2\37\u00db\3\2\2\2!\u00dd\3\2\2\2#\u00e0")
        buf.write("\3\2\2\2%\u00e2\3\2\2\2\'\u00e4\3\2\2\2)\u00e6\3\2\2\2")
        buf.write("+\u00e9\3\2\2\2-\u00ec\3\2\2\2/\u00f2\3\2\2\2\61\u00f8")
        buf.write("\3\2\2\2\63\u0101\3\2\2\2\65\u0105\3\2\2\2\67\u0108\3")
        buf.write("\2\2\29\u010f\3\2\2\2;\u0112\3\2\2\2=\u0115\3\2\2\2?\u011a")
        buf.write("\3\2\2\2A\u011f\3\2\2\2C\u0126\3\2\2\2E\u012c\3\2\2\2")
        buf.write("G\u0132\3\2\2\2I\u0136\3\2\2\2K\u013f\3\2\2\2M\u0149\3")
        buf.write("\2\2\2O\u014d\3\2\2\2Q\u0152\3\2\2\2S\u0158\3\2\2\2U\u015e")
        buf.write("\3\2\2\2W\u0161\3\2\2\2Y\u0173\3\2\2\2[\u0181\3\2\2\2")
        buf.write("]\u0183\3\2\2\2_\u018a\3\2\2\2a\u018e\3\2\2\2c\u0192\3")
        buf.write("\2\2\2e\u0195\3\2\2\2g\u0199\3\2\2\2i\u019d\3\2\2\2k\u019f")
        buf.write("\3\2\2\2m\u01a1\3\2\2\2o\u01a3\3\2\2\2q\u01a5\3\2\2\2")
        buf.write("s\u01a7\3\2\2\2u\u01a9\3\2\2\2w\u01ab\3\2\2\2y\u01ad\3")
        buf.write("\2\2\2{\u01af\3\2\2\2}\u01b1\3\2\2\2\177\u01b3\3\2\2\2")
        buf.write("\u0081\u01b5\3\2\2\2\u0083\u01b7\3\2\2\2\u0085\u01b9\3")
        buf.write("\2\2\2\u0087\u01bb\3\2\2\2\u0089\u01bd\3\2\2\2\u008b\u01bf")
        buf.write("\3\2\2\2\u008d\u01c1\3\2\2\2\u008f\u01c3\3\2\2\2\u0091")
        buf.write("\u01c5\3\2\2\2\u0093\u01c7\3\2\2\2\u0095\u01c9\3\2\2\2")
        buf.write("\u0097\u01cb\3\2\2\2\u0099\u01cd\3\2\2\2\u009b\u01cf\3")
        buf.write("\2\2\2\u009d\u01d1\3\2\2\2\u009f\u01d4\3\2\2\2\u00a1\u01d9")
        buf.write("\3\2\2\2\u00a3\u01e2\3\2\2\2\u00a5\u021d\3\2\2\2\u00a7")
        buf.write("\u0228\3\2\2\2\u00a9\u022a\3\2\2\2\u00ab\u023a\3\2\2\2")
        buf.write("\u00ad\u023e\3\2\2\2\u00af\u0242\3\2\2\2\u00b1\u0244\3")
        buf.write("\2\2\2\u00b3\u0252\3\2\2\2\u00b5\u025d\3\2\2\2\u00b7\u0266")
        buf.write("\3\2\2\2\u00b9\u0268\3\2\2\2\u00bb\u026a\3\2\2\2\u00bd")
        buf.write("\u00be\7*\2\2\u00be\4\3\2\2\2\u00bf\u00c0\7+\2\2\u00c0")
        buf.write("\6\3\2\2\2\u00c1\u00c2\7}\2\2\u00c2\b\3\2\2\2\u00c3\u00c4")
        buf.write("\7\177\2\2\u00c4\n\3\2\2\2\u00c5\u00c6\7]\2\2\u00c6\f")
        buf.write("\3\2\2\2\u00c7\u00c8\7_\2\2\u00c8\16\3\2\2\2\u00c9\u00ca")
        buf.write("\7=\2\2\u00ca\20\3\2\2\2\u00cb\u00cc\7.\2\2\u00cc\22\3")
        buf.write("\2\2\2\u00cd\u00ce\7?\2\2\u00ce\24\3\2\2\2\u00cf\u00d0")
        buf.write("\7<\2\2\u00d0\26\3\2\2\2\u00d1\u00d2\7\60\2\2\u00d2\u00d3")
        buf.write("\7\60\2\2\u00d3\30\3\2\2\2\u00d4\u00d5\7-\2\2\u00d5\32")
        buf.write("\3\2\2\2\u00d6\u00d7\7,\2\2\u00d7\34\3\2\2\2\u00d8\u00d9")
        buf.write("\7>\2\2\u00d9\u00da\7@\2\2\u00da\36\3\2\2\2\u00db\u00dc")
        buf.write("\7>\2\2\u00dc \3\2\2\2\u00dd\u00de\7>\2\2\u00de\u00df")
        buf.write("\7?\2\2\u00df\"\3\2\2\2\u00e0\u00e1\7/\2\2\u00e1$\3\2")
        buf.write("\2\2\u00e2\u00e3\7\61\2\2\u00e3&\3\2\2\2\u00e4\u00e5\7")
        buf.write("@\2\2\u00e5(\3\2\2\2\u00e6\u00e7\7@\2\2\u00e7\u00e8\7")
        buf.write("?\2\2\u00e8*\3\2\2\2\u00e9\u00ea\7\"\2\2\u00ea,\3\2\2")
        buf.write("\2\u00eb\u00ed\t\2\2\2\u00ec\u00eb\3\2\2\2\u00ed\u00ee")
        buf.write("\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef")
        buf.write("\u00f0\3\2\2\2\u00f0\u00f1\b\27\2\2\u00f1.\3\2\2\2\u00f2")
        buf.write("\u00f3\5k\66\2\u00f3\u00f4\5\u008bF\2\u00f4\u00f5\5q9")
        buf.write("\2\u00f5\u00f6\5i\65\2\u00f6\u00f7\5}?\2\u00f7\60\3\2")
        buf.write("\2\2\u00f8\u00f9\5m\67\2\u00f9\u00fa\5\u0085C\2\u00fa")
        buf.write("\u00fb\5\u0083B\2\u00fb\u00fc\5\u008fH\2\u00fc\u00fd\5")
        buf.write("y=\2\u00fd\u00fe\5\u0083B\2\u00fe\u00ff\5\u0091I\2\u00ff")
        buf.write("\u0100\5q9\2\u0100\62\3\2\2\2\u0101\u0102\5s:\2\u0102")
        buf.write("\u0103\5\u0085C\2\u0103\u0104\5\u008bF\2\u0104\64\3\2")
        buf.write("\2\2\u0105\u0106\5\u008fH\2\u0106\u0107\5\u0085C\2\u0107")
        buf.write("\66\3\2\2\2\u0108\u0109\5o8\2\u0109\u010a\5\u0085C\2\u010a")
        buf.write("\u010b\5\u0095K\2\u010b\u010c\5\u0083B\2\u010c\u010d\5")
        buf.write("\u008fH\2\u010d\u010e\5\u0085C\2\u010e8\3\2\2\2\u010f")
        buf.write("\u0110\5o8\2\u0110\u0111\5\u0085C\2\u0111:\3\2\2\2\u0112")
        buf.write("\u0113\5y=\2\u0113\u0114\5s:\2\u0114<\3\2\2\2\u0115\u0116")
        buf.write("\5\u008fH\2\u0116\u0117\5w<\2\u0117\u0118\5q9\2\u0118")
        buf.write("\u0119\5\u0083B\2\u0119>\3\2\2\2\u011a\u011b\5q9\2\u011b")
        buf.write("\u011c\5\177@\2\u011c\u011d\5\u008dG\2\u011d\u011e\5q")
        buf.write("9\2\u011e@\3\2\2\2\u011f\u0120\5\u008bF\2\u0120\u0121")
        buf.write("\5q9\2\u0121\u0122\5\u008fH\2\u0122\u0123\5\u0091I\2\u0123")
        buf.write("\u0124\5\u008bF\2\u0124\u0125\5\u0083B\2\u0125B\3\2\2")
        buf.write("\2\u0126\u0127\5\u0095K\2\u0127\u0128\5w<\2\u0128\u0129")
        buf.write("\5y=\2\u0129\u012a\5\177@\2\u012a\u012b\5q9\2\u012bD\3")
        buf.write("\2\2\2\u012c\u012d\5k\66\2\u012d\u012e\5q9\2\u012e\u012f")
        buf.write("\5u;\2\u012f\u0130\5y=\2\u0130\u0131\5\u0083B\2\u0131")
        buf.write("F\3\2\2\2\u0132\u0133\5q9\2\u0133\u0134\5\u0083B\2\u0134")
        buf.write("\u0135\5o8\2\u0135H\3\2\2\2\u0136\u0137\5s:\2\u0137\u0138")
        buf.write("\5\u0091I\2\u0138\u0139\5m\67\2\u0139\u013a\5\u0083B\2")
        buf.write("\u013a\u013b\5\u008fH\2\u013b\u013c\5y=\2\u013c\u013d")
        buf.write("\5\u0085C\2\u013d\u013e\5\u0083B\2\u013eJ\3\2\2\2\u013f")
        buf.write("\u0140\5\u0087D\2\u0140\u0141\5\u008bF\2\u0141\u0142\5")
        buf.write("\u0085C\2\u0142\u0143\5m\67\2\u0143\u0144\5q9\2\u0144")
        buf.write("\u0145\5o8\2\u0145\u0146\5\u0091I\2\u0146\u0147\5\u008b")
        buf.write("F\2\u0147\u0148\5q9\2\u0148L\3\2\2\2\u0149\u014a\5\u0093")
        buf.write("J\2\u014a\u014b\5i\65\2\u014b\u014c\5\u008bF\2\u014cN")
        buf.write("\3\2\2\2\u014d\u014e\5\u008fH\2\u014e\u014f\5\u008bF\2")
        buf.write("\u014f\u0150\5\u0091I\2\u0150\u0151\5q9\2\u0151P\3\2\2")
        buf.write("\2\u0152\u0153\5s:\2\u0153\u0154\5i\65\2\u0154\u0155\5")
        buf.write("\177@\2\u0155\u0156\5\u008dG\2\u0156\u0157\5q9\2\u0157")
        buf.write("R\3\2\2\2\u0158\u0159\5i\65\2\u0159\u015a\5\u008bF\2\u015a")
        buf.write("\u015b\5\u008bF\2\u015b\u015c\5i\65\2\u015c\u015d\5\u0099")
        buf.write("M\2\u015dT\3\2\2\2\u015e\u015f\5\u0085C\2\u015f\u0160")
        buf.write("\5s:\2\u0160V\3\2\2\2\u0161\u0162\5\u008bF\2\u0162\u0163")
        buf.write("\5q9\2\u0163\u0164\5i\65\2\u0164\u0165\5\177@\2\u0165")
        buf.write("X\3\2\2\2\u0166\u0167\5k\66\2\u0167\u0168\5\u0085C\2\u0168")
        buf.write("\u0169\5\u0085C\2\u0169\u016a\5\177@\2\u016a\u016b\5q")
        buf.write("9\2\u016b\u016c\5i\65\2\u016c\u016d\5\u0083B\2\u016d\u0174")
        buf.write("\3\2\2\2\u016e\u016f\5k\66\2\u016f\u0170\5\u0085C\2\u0170")
        buf.write("\u0171\5\u0085C\2\u0171\u0172\5\177@\2\u0172\u0174\3\2")
        buf.write("\2\2\u0173\u0166\3\2\2\2\u0173\u016e\3\2\2\2\u0174Z\3")
        buf.write("\2\2\2\u0175\u0176\5y=\2\u0176\u0177\5\u0083B\2\u0177")
        buf.write("\u0178\5\u008fH\2\u0178\u0179\5q9\2\u0179\u017a\5u;\2")
        buf.write("\u017a\u017b\5q9\2\u017b\u017c\5\u008bF\2\u017c\u0182")
        buf.write("\3\2\2\2\u017d\u017e\5y=\2\u017e\u017f\5\u0083B\2\u017f")
        buf.write("\u0180\5\u008fH\2\u0180\u0182\3\2\2\2\u0181\u0175\3\2")
        buf.write("\2\2\u0181\u017d\3\2\2\2\u0182\\\3\2\2\2\u0183\u0184\5")
        buf.write("\u008dG\2\u0184\u0185\5\u008fH\2\u0185\u0186\5\u008bF")
        buf.write("\2\u0186\u0187\5y=\2\u0187\u0188\5\u0083B\2\u0188\u0189")
        buf.write("\5u;\2\u0189^\3\2\2\2\u018a\u018b\5\u0083B\2\u018b\u018c")
        buf.write("\5\u0085C\2\u018c\u018d\5\u008fH\2\u018d`\3\2\2\2\u018e")
        buf.write("\u018f\5i\65\2\u018f\u0190\5\u0083B\2\u0190\u0191\5o8")
        buf.write("\2\u0191b\3\2\2\2\u0192\u0193\5\u0085C\2\u0193\u0194\5")
        buf.write("\u008bF\2\u0194d\3\2\2\2\u0195\u0196\5o8\2\u0196\u0197")
        buf.write("\5y=\2\u0197\u0198\5\u0093J\2\u0198f\3\2\2\2\u0199\u019a")
        buf.write("\5\u0081A\2\u019a\u019b\5\u0085C\2\u019b\u019c\5o8\2\u019c")
        buf.write("h\3\2\2\2\u019d\u019e\t\3\2\2\u019ej\3\2\2\2\u019f\u01a0")
        buf.write("\t\4\2\2\u01a0l\3\2\2\2\u01a1\u01a2\t\5\2\2\u01a2n\3\2")
        buf.write("\2\2\u01a3\u01a4\t\6\2\2\u01a4p\3\2\2\2\u01a5\u01a6\t")
        buf.write("\7\2\2\u01a6r\3\2\2\2\u01a7\u01a8\t\b\2\2\u01a8t\3\2\2")
        buf.write("\2\u01a9\u01aa\t\t\2\2\u01aav\3\2\2\2\u01ab\u01ac\t\n")
        buf.write("\2\2\u01acx\3\2\2\2\u01ad\u01ae\t\13\2\2\u01aez\3\2\2")
        buf.write("\2\u01af\u01b0\t\f\2\2\u01b0|\3\2\2\2\u01b1\u01b2\t\r")
        buf.write("\2\2\u01b2~\3\2\2\2\u01b3\u01b4\t\16\2\2\u01b4\u0080\3")
        buf.write("\2\2\2\u01b5\u01b6\t\17\2\2\u01b6\u0082\3\2\2\2\u01b7")
        buf.write("\u01b8\t\20\2\2\u01b8\u0084\3\2\2\2\u01b9\u01ba\t\21\2")
        buf.write("\2\u01ba\u0086\3\2\2\2\u01bb\u01bc\t\22\2\2\u01bc\u0088")
        buf.write("\3\2\2\2\u01bd\u01be\t\23\2\2\u01be\u008a\3\2\2\2\u01bf")
        buf.write("\u01c0\t\24\2\2\u01c0\u008c\3\2\2\2\u01c1\u01c2\t\25\2")
        buf.write("\2\u01c2\u008e\3\2\2\2\u01c3\u01c4\t\26\2\2\u01c4\u0090")
        buf.write("\3\2\2\2\u01c5\u01c6\t\27\2\2\u01c6\u0092\3\2\2\2\u01c7")
        buf.write("\u01c8\t\30\2\2\u01c8\u0094\3\2\2\2\u01c9\u01ca\t\31\2")
        buf.write("\2\u01ca\u0096\3\2\2\2\u01cb\u01cc\t\32\2\2\u01cc\u0098")
        buf.write("\3\2\2\2\u01cd\u01ce\t\33\2\2\u01ce\u009a\3\2\2\2\u01cf")
        buf.write("\u01d0\t\34\2\2\u01d0\u009c\3\2\2\2\u01d1\u01d2\t\35\2")
        buf.write("\2\u01d2\u009e\3\2\2\2\u01d3\u01d5\5\u009dO\2\u01d4\u01d3")
        buf.write("\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d6")
        buf.write("\u01d7\3\2\2\2\u01d7\u00a0\3\2\2\2\u01d8\u01da\t\36\2")
        buf.write("\2\u01d9\u01d8\3\2\2\2\u01da\u01de\3\2\2\2\u01db\u01dd")
        buf.write("\t\37\2\2\u01dc\u01db\3\2\2\2\u01dd\u01e0\3\2\2\2\u01de")
        buf.write("\u01dc\3\2\2\2\u01de\u01df\3\2\2\2\u01df\u00a2\3\2\2\2")
        buf.write("\u01e0\u01de\3\2\2\2\u01e1\u01e3\t\35\2\2\u01e2\u01e1")
        buf.write("\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e4")
        buf.write("\u01e5\3\2\2\2\u01e5\u00a4\3\2\2\2\u01e6\u01e8\t\35\2")
        buf.write("\2\u01e7\u01e6\3\2\2\2\u01e8\u01e9\3\2\2\2\u01e9\u01e7")
        buf.write("\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea\u01ec\3\2\2\2\u01eb")
        buf.write("\u01ed\7\60\2\2\u01ec\u01eb\3\2\2\2\u01ec\u01ed\3\2\2")
        buf.write("\2\u01ed\u01f1\3\2\2\2\u01ee\u01f0\t\35\2\2\u01ef\u01ee")
        buf.write("\3\2\2\2\u01f0\u01f3\3\2\2\2\u01f1\u01ef\3\2\2\2\u01f1")
        buf.write("\u01f2\3\2\2\2\u01f2\u0202\3\2\2\2\u01f3\u01f1\3\2\2\2")
        buf.write("\u01f4\u01f6\t\35\2\2\u01f5\u01f4\3\2\2\2\u01f6\u01f7")
        buf.write("\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f7\u01f8\3\2\2\2\u01f8")
        buf.write("\u01f9\3\2\2\2\u01f9\u01fb\t\7\2\2\u01fa\u01fc\7/\2\2")
        buf.write("\u01fb\u01fa\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc\u01fe\3")
        buf.write("\2\2\2\u01fd\u01ff\t\35\2\2\u01fe\u01fd\3\2\2\2\u01ff")
        buf.write("\u0200\3\2\2\2\u0200\u01fe\3\2\2\2\u0200\u0201\3\2\2\2")
        buf.write("\u0201\u0203\3\2\2\2\u0202\u01f5\3\2\2\2\u0202\u0203\3")
        buf.write("\2\2\2\u0203\u021e\3\2\2\2\u0204\u0206\t\35\2\2\u0205")
        buf.write("\u0204\3\2\2\2\u0206\u0209\3\2\2\2\u0207\u0205\3\2\2\2")
        buf.write("\u0207\u0208\3\2\2\2\u0208\u020b\3\2\2\2\u0209\u0207\3")
        buf.write("\2\2\2\u020a\u020c\7\60\2\2\u020b\u020a\3\2\2\2\u020b")
        buf.write("\u020c\3\2\2\2\u020c\u020e\3\2\2\2\u020d\u020f\t\35\2")
        buf.write("\2\u020e\u020d\3\2\2\2\u020f\u0210\3\2\2\2\u0210\u020e")
        buf.write("\3\2\2\2\u0210\u0211\3\2\2\2\u0211\u021b\3\2\2\2\u0212")
        buf.write("\u0214\t\7\2\2\u0213\u0215\7/\2\2\u0214\u0213\3\2\2\2")
        buf.write("\u0214\u0215\3\2\2\2\u0215\u0217\3\2\2\2\u0216\u0218\t")
        buf.write("\35\2\2\u0217\u0216\3\2\2\2\u0218\u0219\3\2\2\2\u0219")
        buf.write("\u0217\3\2\2\2\u0219\u021a\3\2\2\2\u021a\u021c\3\2\2\2")
        buf.write("\u021b\u0212\3\2\2\2\u021b\u021c\3\2\2\2\u021c\u021e\3")
        buf.write("\2\2\2\u021d\u01e7\3\2\2\2\u021d\u0207\3\2\2\2\u021e\u00a6")
        buf.write("\3\2\2\2\u021f\u0220\7v\2\2\u0220\u0221\7t\2\2\u0221\u0222")
        buf.write("\7w\2\2\u0222\u0229\7g\2\2\u0223\u0224\7h\2\2\u0224\u0225")
        buf.write("\7c\2\2\u0225\u0226\7n\2\2\u0226\u0227\7u\2\2\u0227\u0229")
        buf.write("\7g\2\2\u0228\u021f\3\2\2\2\u0228\u0223\3\2\2\2\u0229")
        buf.write("\u00a8\3\2\2\2\u022a\u0230\7$\2\2\u022b\u022c\7^\2\2\u022c")
        buf.write("\u022f\t \2\2\u022d\u022f\n!\2\2\u022e\u022b\3\2\2\2\u022e")
        buf.write("\u022d\3\2\2\2\u022f\u0232\3\2\2\2\u0230\u022e\3\2\2\2")
        buf.write("\u0230\u0231\3\2\2\2\u0231\u0233\3\2\2\2\u0232\u0230\3")
        buf.write("\2\2\2\u0233\u0234\7$\2\2\u0234\u00aa\3\2\2\2\u0235\u023b")
        buf.write("\5Y-\2\u0236\u023b\5[.\2\u0237\u023b\5W,\2\u0238\u023b")
        buf.write("\5]/\2\u0239\u023b\5S*\2\u023a\u0235\3\2\2\2\u023a\u0236")
        buf.write("\3\2\2\2\u023a\u0237\3\2\2\2\u023a\u0238\3\2\2\2\u023a")
        buf.write("\u0239\3\2\2\2\u023b\u00ac\3\2\2\2\u023c\u023f\5\u00af")
        buf.write("X\2\u023d\u023f\5\u00b5[\2\u023e\u023c\3\2\2\2\u023e\u023d")
        buf.write("\3\2\2\2\u023f\u00ae\3\2\2\2\u0240\u0243\5\u00b1Y\2\u0241")
        buf.write("\u0243\5\u00b3Z\2\u0242\u0240\3\2\2\2\u0242\u0241\3\2")
        buf.write("\2\2\u0243\u00b0\3\2\2\2\u0244\u0245\7*\2\2\u0245\u0246")
        buf.write("\7,\2\2\u0246\u024a\3\2\2\2\u0247\u0249\13\2\2\2\u0248")
        buf.write("\u0247\3\2\2\2\u0249\u024c\3\2\2\2\u024a\u024b\3\2\2\2")
        buf.write("\u024a\u0248\3\2\2\2\u024b\u024d\3\2\2\2\u024c\u024a\3")
        buf.write("\2\2\2\u024d\u024e\7,\2\2\u024e\u024f\7+\2\2\u024f\u0250")
        buf.write("\3\2\2\2\u0250\u0251\bY\2\2\u0251\u00b2\3\2\2\2\u0252")
        buf.write("\u0256\7}\2\2\u0253\u0255\13\2\2\2\u0254\u0253\3\2\2\2")
        buf.write("\u0255\u0258\3\2\2\2\u0256\u0257\3\2\2\2\u0256\u0254\3")
        buf.write("\2\2\2\u0257\u0259\3\2\2\2\u0258\u0256\3\2\2\2\u0259\u025a")
        buf.write("\7\177\2\2\u025a\u025b\3\2\2\2\u025b\u025c\bZ\2\2\u025c")
        buf.write("\u00b4\3\2\2\2\u025d\u025e\7\61\2\2\u025e\u025f\7\61\2")
        buf.write("\2\u025f\u0263\3\2\2\2\u0260\u0262\n\"\2\2\u0261\u0260")
        buf.write("\3\2\2\2\u0262\u0265\3\2\2\2\u0263\u0261\3\2\2\2\u0263")
        buf.write("\u0264\3\2\2\2\u0264\u00b6\3\2\2\2\u0265\u0263\3\2\2\2")
        buf.write("\u0266\u0267\13\2\2\2\u0267\u00b8\3\2\2\2\u0268\u0269")
        buf.write("\13\2\2\2\u0269\u00ba\3\2\2\2\u026a\u026b\13\2\2\2\u026b")
        buf.write("\u00bc\3\2\2\2\"\2\u00ee\u0173\u0181\u01d6\u01d9\u01dc")
        buf.write("\u01de\u01e4\u01e9\u01ec\u01f1\u01f7\u01fb\u0200\u0202")
        buf.write("\u0207\u020b\u0210\u0214\u0219\u021b\u021d\u0228\u022e")
        buf.write("\u0230\u023a\u023e\u0242\u024a\u0256\u0263\3\b\2\2")
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
    WS = 22
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

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "','", "'='", 
            "':'", "'..'", "'+'", "'*'", "'<>'", "'<'", "'<='", "'-'", "'/'", 
            "'>'", "'>='", "' '" ]

    symbolicNames = [ "<INVALID>",
            "LB", "RB", "LP", "RP", "LQ", "RQ", "SEMI", "CM", "EQ", "COL", 
            "DD", "ADD", "MUL", "NOTEQ", "LESSTN", "LESSEQ", "SUBNE", "DIVSI", 
            "GRETN", "GREEQ", "SP", "WS", "BREAK", "CONTINUE", "FOR", "TO", 
            "DOWNTO", "DO", "IF", "THEN", "ELSE", "RETURN", "WHILE", "BEGIN", 
            "END", "FUNCTION", "PROCEDURE", "VAR", "TRUE", "FALSE", "ARRAY", 
            "OF", "REAL", "BOOLEAN", "INTEGER", "STRING", "NOT", "AND", 
            "OR", "DIV", "MOD", "ManyNum", "ID", "INTLIT", "REALLIT", "BOOLLIT", 
            "STRINGLIT", "TYPE", "CMT", "BLKCMT", "TRACMT", "BLCMT", "LINECMT", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "LB", "RB", "LP", "RP", "LQ", "RQ", "SEMI", "CM", "EQ", 
                  "COL", "DD", "ADD", "MUL", "NOTEQ", "LESSTN", "LESSEQ", 
                  "SUBNE", "DIVSI", "GRETN", "GREEQ", "SP", "WS", "BREAK", 
                  "CONTINUE", "FOR", "TO", "DOWNTO", "DO", "IF", "THEN", 
                  "ELSE", "RETURN", "WHILE", "BEGIN", "END", "FUNCTION", 
                  "PROCEDURE", "VAR", "TRUE", "FALSE", "ARRAY", "OF", "REAL", 
                  "BOOLEAN", "INTEGER", "STRING", "NOT", "AND", "OR", "DIV", 
                  "MOD", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", 
                  "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", 
                  "V", "W", "X", "Y", "Z", "NUM", "ManyNum", "ID", "INTLIT", 
                  "REALLIT", "BOOLLIT", "STRINGLIT", "TYPE", "CMT", "BLKCMT", 
                  "TRACMT", "BLCMT", "LINECMT", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


