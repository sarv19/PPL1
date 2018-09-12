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

########    test function declaration     ################
    def test_funcdeclare1(self):
        input = """FUNCTION foo(a,b:integer;c:real):real;
        Begin
         1234
          End"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2101))
    def test_funcdeclare2(self):
        input = """FUNCTION foo (a,b: integer; c: real): array [1 .. 2] of real;BEGIn      1234 END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2102))
    def test_funcdeclare3(self):
        input = """FUNCTION foo (a,b: integer; c: real): array [1 .. 2] of real;
        var x,y:real;
                BEGIN
                1234
                END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2103))
    def test_funcdeclare4(self):
        input = """FUNCTION foo(a,b:integer;c:real):real;
        Begin
          End"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2104))


#########  test procedure declaration     #################
    def test_procedeclare1(self):
        input = """procedure foo(a,b:integer;c:real);
        Begin
          End"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,3101))
    def test_procedeclare2(self):
        input = """procedure foo(a,b:integer;c:real);
        var x,y: real;
        Begin
          End"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,3102))
    def test_procedeclare3(self):
        input = """procedure foo(a,b:integer c:real);
        var x,y: real;
        Begin
          End"""
        expect = "Error on line 1 col 26: c"
        self.assertTrue(TestParser.test(input,expect,3103))
    def test_procedeclare4(self):
        input = """procedure foo(a,b:integer; c:real;d,e,f:boolean;k:int);
        var x,y: real;
        Begin
          End"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,3104))
