import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    #########     test identifier   ##############
    def test_identifier(self):
        self.assertTrue(TestLexer.test("abc","abc,<EOF>",101))
    def test_identifier2(self):
        self.assertTrue(TestLexer.test("aCBbdc","aCBbdc,<EOF>",102))
    def test_identifier3(self):
        self.assertTrue(TestLexer.test("aAsVN","aAsVN,<EOF>",103))
    def test_identifier4(self):
        self.assertTrue(TestLexer.test("_aAsVN","_aAsVN,<EOF>",104))
    def test_identifier5(self):
        self.assertTrue(TestLexer.test("A_sVN","A_sVN,<EOF>",105))
    def test_identifier6(self):
        self.assertTrue(TestLexer.test("5aAsVN","5,aAsVN,<EOF>",106))
    def test_identifier7(self):
        self.assertTrue(TestLexer.test("_","_,<EOF>",107))
    def test_identifier8(self):
        self.assertTrue(TestLexer.test("_789","_789,<EOF>",108))
    def test_identifier9(self):
        self.assertTrue(TestLexer.test("break","break,<EOF>",109))

#############    test real    #############
    def test_real1(self):
        self.assertTrue(TestLexer.test("0.1e5","0.1e5,<EOF>",201))
    def test_real2(self):
        self.assertTrue(TestLexer.test("1.2","1.2,<EOF>",202))
    def test_real3(self):
        self.assertTrue(TestLexer.test("1.","1.,<EOF>",203))
    def test_real4(self):
        self.assertTrue(TestLexer.test("1e2","1e2,<EOF>",204))
    def test_real5(self):
        self.assertTrue(TestLexer.test("1.2e-4","1.2e-4,<EOF>",205))
    def test_real6(self):
        self.assertTrue(TestLexer.test(".1E2",".1E2,<EOF>",206))
    def test_real7(self):
        self.assertTrue(TestLexer.test("12e8","12e8,<EOF>",207))
    def test_real8(self):
        self.assertTrue(TestLexer.test("128e-42","128e-42,<EOF>",208))
    def test_real9(self):
        self.assertTrue(TestLexer.test("e-12","e,-,12,<EOF>",209))
    def test_real10(self):
        self.assertTrue(TestLexer.test("143e","143,e,<EOF>",210))
    def test_real11(self):
        self.assertTrue(TestLexer.test("0e12.5e16","0e12,.5e16,<EOF>",211))
    def test_real12(self):
        self.assertTrue(TestLexer.test(".",".,<EOF>",212))
    def test_real13(self):
        self.assertTrue(TestLexer.test("-.5","-,.5,<EOF>",213))
    def test_real14(self):
        self.assertTrue(TestLexer.test("1e5","1e5,<EOF>",214))

#######      test boolean           #########
    def test_boolean1(self):
        self.assertTrue(TestLexer.test("true","true,<EOF>",301))
    def test_boolean2(self):
        self.assertTrue(TestLexer.test("false","false,<EOF>",302))
    def test_boolean3(self):
        self.assertTrue(TestLexer.test("faLSe","faLSe,<EOF>",303))
    def test_boolean4(self):
        self.assertTrue(TestLexer.test("TruE","TruE,<EOF>",304))

#######      test string          ###########
    def test_string1(self):
        self.assertTrue(TestLexer.test('"abcd"','"abcd",<EOF>',401))
    def test_string2(self):
        self.assertTrue(TestLexer.test('"@#$%^&"','"@#$%^&",<EOF>',402))
    def test_string3(self):
        self.assertTrue(TestLexer.test('"ab*&*)_cd12AD"','"ab*&*)_cd12AD",<EOF>',403))
    def test_string4(self):
        self.assertTrue(TestLexer.test('"ab\\ncd"','"ab\\ncd",<EOF>',404))
    def test_string5(self):
        self.assertTrue(TestLexer.test('"ab\\tcd"','"ab\\tcd",<EOF>',405))
    def test_string6(self):
        self.assertTrue(TestLexer.test('"ab\\fcd"','"ab\\fcd",<EOF>',406))
    def test_string7(self):
        self.assertTrue(TestLexer.test('"ab \\" cd"','"ab \\" cd",<EOF>',407))
    def test_unclosed(self):
        self.assertTrue(TestLexer.test('"abh','Unclosed String: ',408))
    def test_ilegal1(self):
       self.assertTrue(TestLexer.test('"a\\c"','Illegal Escape In String: ',409))
    def test_ilegal2(self):
       self.assertTrue(TestLexer.test('"a\fc','Illegal Escape In String: ',410))
