import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

#######     test declaration      ##########
    def test_declare1(self):
        input = """VAR a,b,c:integer;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1101))
    def test_declare2(self):
        input = """VAR a: array[1 .. 5] of REAL;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1102))
    def test_declare3(self):
        input = """VAR a,b,c,E: array[1 .. 55] of boolean;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1103))
    def test_declare4(self):
        input = """VAR a: array[1 .. 5] of strIng;
                        d,g,i:integer;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1104))
    def test_declare5(self):
        input = """VAR a,b,c: int;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1105))
