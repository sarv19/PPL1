import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

#########     test identifier   ##############
    def test_identifier(self):
        self.assertTrue(TestLexer.test("abc_123","abc_123,<EOF>",101))
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
        self.assertTrue(TestLexer.test("rou432ndandround_","rou432ndandround_,<EOF>",109))
    def test_identifier10(self):
        self.assertTrue(TestLexer.test("____ndandrGHU890ound_","____ndandrGHU890ound_,<EOF>",110))
    def test_identifier11(self):
        self.assertTrue(TestLexer.test("thisIsWeird$%^&","thisIsWeird,Error Token $",110))
    def test_identifier12(self):
        self.assertTrue(TestLexer.test("_nhu nhu_123 n_1_2_c_4","_nhu,nhu_123,n_1_2_c_4,<EOF>",112))
    def test_identifier13(self):
        self.assertTrue(TestLexer.test("Can I write thIS &*%","Can,I,write,thIS,Error Token &",113))


#############    test integer    #############
    def test_int1(self):
        self.assertTrue(TestLexer.test("0919669999","0919669999,<EOF>",201))
    def test_int2(self):
        self.assertTrue(TestLexer.test("5","5,<EOF>",202))
    def test_int3(self):
        self.assertTrue(TestLexer.test("32432yui","32432,yui,<EOF>",203))
    def test_int4(self):
        self.assertTrue(TestLexer.test("0xEF57","0,xEF57,<EOF>",204))
    def test_int5(self):
        self.assertTrue(TestLexer.test("Long lOng one: 345678900987675434123456789009876543234567890098765432",
                                        "Long,lOng,one,:,345678900987675434123456789009876543234567890098765432,<EOF>",205))

#############    test real    #############
    def test_real1(self):
        self.assertTrue(TestLexer.test("0.1e5","0.1e5,<EOF>",301))
    def test_real2(self):
        self.assertTrue(TestLexer.test("1.2","1.2,<EOF>",302))
    def test_real3(self):
        self.assertTrue(TestLexer.test("1.","1.,<EOF>",303))
    def test_real4(self):
        self.assertTrue(TestLexer.test("1e2","1e2,<EOF>",304))
    def test_real5(self):
        self.assertTrue(TestLexer.test("1.2e-4","1.2e-4,<EOF>",305))
    def test_real6(self):
        self.assertTrue(TestLexer.test(".1E2",".1E2,<EOF>",306))
    def test_real7(self):
        self.assertTrue(TestLexer.test("12e8","12e8,<EOF>",307))
    def test_real8(self):
        self.assertTrue(TestLexer.test("128e-42","128e-42,<EOF>",308))
    def test_real9(self):
        self.assertTrue(TestLexer.test("e-12","e,-,12,<EOF>",309))
    def test_real10(self):
        self.assertTrue(TestLexer.test("143e","143,e,<EOF>",310))
    def test_real11(self):
        self.assertTrue(TestLexer.test("0e12.5e16","0e12,.5e16,<EOF>",311))
    def test_real12(self):
        self.assertTrue(TestLexer.test(".","Error Token .",312))
    def test_real13(self):
        self.assertTrue(TestLexer.test("-.5","-,.5,<EOF>",313))
    def test_real14(self):
        self.assertTrue(TestLexer.test("1e5","1e5,<EOF>",314))
    def test_real15(self):
        self.assertTrue(TestLexer.test("1.e5","1.e5,<EOF>",315))
    def test_real16(self):
        self.assertTrue(TestLexer.test("0.","0.,<EOF>",316))
    def test_real17(self):
        self.assertTrue(TestLexer.test("1.E5","1.E5,<EOF>",317))

#######      test boolean           #########
    def test_boolean1(self):
        self.assertTrue(TestLexer.test("true","true,<EOF>",401))
    def test_boolean2(self):
        self.assertTrue(TestLexer.test("false","false,<EOF>",402))
    def test_boolean3(self):
        self.assertTrue(TestLexer.test("faLSe","faLSe,<EOF>",403))

#######      test string          ###########
    def test_string1(self):
        self.assertTrue(TestLexer.test('"abcd"','abcd,<EOF>',501))
    def test_string2(self):
        self.assertTrue(TestLexer.test('"@#$%^&"','@#$%^&,<EOF>',502))
    def test_string3(self):
        self.assertTrue(TestLexer.test('"ab*&*)_cd12AD"','ab*&*)_cd12AD,<EOF>',503))
    def test_string4(self):
        self.assertTrue(TestLexer.test('"ab\\ncd"','ab\\ncd,<EOF>',504))
    def test_string5(self):
        self.assertTrue(TestLexer.test('"ab\\tcd"','ab\\tcd,<EOF>',505))
    def test_string6(self):
        self.assertTrue(TestLexer.test('"ab\\fcd"','ab\\fcd,<EOF>',506))
    def test_string7(self):
        self.assertTrue(TestLexer.test('"ab \\" cd"','ab \\" cd,<EOF>',507))
    def test_unclosed(self):
        self.assertTrue(TestLexer.test('"abh','Unclosed String: abh',508))
    def test_ilegal1(self):
       self.assertTrue(TestLexer.test('"a\\c"','Illegal Escape In String: a\\c',509))
#    def test_ilegal2(self):
#       self.assertTrue(TestLexer.test('"a\fc"','Illegal Escape In String: a\fc',410))
    def test_string11(self):
        self.assertTrue(TestLexer.test('"begin"','begin,<EOF>',511))
    def test_string12(self):
        self.assertTrue(TestLexer.test('"This sure is a motherf#$%^& string"','This sure is a motherf#$%^& string,<EOF>',512))
    def test_string13(self):
        self.assertTrue(TestLexer.test('"Test \\n \\t \\f \\b"','Test \\n \\t \\f \\b,<EOF>',513))
    def test_string14(self):
        self.assertTrue(TestLexer.test('"Is This Ok? \\\\\\\\"','Is This Ok? \\\\\\\\,<EOF>',514))
    def test_string15(self):
        self.assertTrue(TestLexer.test('?','Error Token ?',515))
    def test_string16(self):
        self.assertTrue(TestLexer.test('"fdsfsd\\tcscas','Unclosed String: fdsfsd\\tcscas',516))

#######      test separators&operator     ############
    def test_sepa_oper1(self):
        self.assertTrue(TestLexer.test("+-*/< > <> <= >=","+,-,*,/,<,>,<>,<=,>=,<EOF>",601))
    def test_sepa_oper2(self):
        self.assertTrue(TestLexer.test("NoT oR DiV mOD aND ","NoT,oR,DiV,mOD,aND,<EOF>",602))
    def test_sepa_oper3(self):
        self.assertTrue(TestLexer.test("[]:(); .. ,","[,],:,(,),;,..,,,<EOF>",603))
    def test_sepa_oper4(self):
        self.assertTrue(TestLexer.test("[]OR:(MoD);AnD .. ,","[,],OR,:,(,MoD,),;,AnD,..,,,<EOF>",604))

#######      test commnent       ############
    def test_cmt1(self):
        self.assertTrue(TestLexer.test("{fsdfjsdlfjsldkf}","<EOF>",701))
    def test_cmt2(self):
        self.assertTrue(TestLexer.test("(*fsdfjsd\\nfjsldkf*)","<EOF>",702))
    def test_cmt3(self):
        self.assertTrue(TestLexer.test("//gfvhmekfjirdgdkmflsfokdigjdkmslofij","<EOF>",703))
    def test_cmt4(self):
        self.assertTrue(TestLexer.test("//fsdfjsd{lfjsld}kf","<EOF>",704))
    def test_cmt5(self):
        self.assertTrue(TestLexer.test("//fsdfjsd(*lfjsld*)kf","<EOF>",705))
    def test_cmt6(self):
        self.assertTrue(TestLexer.test("(*fsdfjs//dlfjsldkf*)","<EOF>",706))
    def test_cmt7(self):
        self.assertTrue(TestLexer.test('"fsdfjs//dlfjsldkf"','fsdfjs//dlfjsldkf,<EOF>',707))
    def test_cmt8(self):
        self.assertTrue(TestLexer.test("(*fsdfjs//dlfjsldkf","(,*,fsdfjs,<EOF>",708))
    def test_cmt9(self):
        self.assertTrue(TestLexer.test("//fsdfjsd(*lfjsldkf","<EOF>",709))
    def test_cmt10(self):
        self.assertTrue(TestLexer.test("{fsdfjsdl\nfjsldkf}","<EOF>",710))
    def test_cmt11(self):
        self.assertTrue(TestLexer.test("(*fsd\tfjs//d'lfjs'ldkf*)","<EOF>",711))


##########    test keywords        ############
    def test_kw1(self):
        self.assertTrue(TestLexer.test("Break BREAK brEAK break","Break,BREAK,brEAK,break,<EOF>",801))
    def test_kw2(self):
        self.assertTrue(TestLexer.test("CONTINUE COnTINue continue COntinue","CONTINUE,COnTINue,continue,COntinue,<EOF>",802))
    def test_kw3(self):
        self.assertTrue(TestLexer.test("FOR for FoR fOr","FOR,for,FoR,fOr,<EOF>",803))
    def test_kw4(self):
        self.assertTrue(TestLexer.test("TO to To tO","TO,to,To,tO,<EOF>",804))
    def test_kw5(self):
        self.assertTrue(TestLexer.test("DOWNTO downTO DoWnTo","DOWNTO,downTO,DoWnTo,<EOF>",805))
    def test_kw6(self):
        self.assertTrue(TestLexer.test("DO do Do dO","DO,do,Do,dO,<EOF>",806))
    def test_kw7(self):
        self.assertTrue(TestLexer.test("IF if If iF","IF,if,If,iF,<EOF>",807))
    def test_kw8(self):
        self.assertTrue(TestLexer.test("THEN then ThEn thEN","THEN,then,ThEn,thEN,<EOF>",808))
    def test_kw9(self):
        self.assertTrue(TestLexer.test("ELSE else ELse elSE","ELSE,else,ELse,elSE,<EOF>",809))
    def test_kw10(self):
        self.assertTrue(TestLexer.test("RETURN reTURN REtuRN return","RETURN,reTURN,REtuRN,return,<EOF>",810))
    def test_kw11(self):
        self.assertTrue(TestLexer.test("while WHILE whILE WHIle","while,WHILE,whILE,WHIle,<EOF>",811))
    def test_kw12(self):
        self.assertTrue(TestLexer.test("FUNCTION funcTION function FUNCtion","FUNCTION,funcTION,function,FUNCtion,<EOF>",812))
    def test_kw13(self):
        self.assertTrue(TestLexer.test("Var VAR var vAR","Var,VAR,var,vAR,<EOF>",813))
    def test_kw14(self):
        self.assertTrue(TestLexer.test("BOOLEAN booLEAN boolean BOOlean","BOOLEAN,booLEAN,boolean,BOOlean,<EOF>",814))
    def test_kw15(self):
        self.assertTrue(TestLexer.test("PROCEDURE procedure ProCeduRE proCeDURE","PROCEDURE,procedure,ProCeduRE,proCeDURE,<EOF>",815))
    def test_kw16(self):
        self.assertTrue(TestLexer.test("ARRAY array ArrAY aRRaY","ARRAY,array,ArrAY,aRRaY,<EOF>",816))
    def test_kw17(self):
        self.assertTrue(TestLexer.test("STRING strING string STRing","STRING,strING,string,STRing,<EOF>",817))
    def test_kw18(self):
        self.assertTrue(TestLexer.test("REAL real REal reAL","REAL,real,REal,reAL,<EOF>",818))
    def test_kw19(self):
        self.assertTrue(TestLexer.test("INTEGER integer INteger inTEGEr","INTEGER,integer,INteger,inTEGEr,<EOF>",819))
    def test_kw20(self):
        self.assertTrue(TestLexer.test("INTEGER iinteger INtegeri inTEGEr","INTEGER,iinteger,INtegeri,inTEGEr,<EOF>",820))
    def test_kw21(self):
        self.assertTrue(TestLexer.test("WITH iwith withi with","WITH,iwith,withi,with,<EOF>",821))

#########   test mixstyle    ############
    def test_mixstyle1(self):
        self.assertTrue(TestLexer.test('"\n \t \f \b this"','Unclosed String: ',901))
    def test_mixstyle2(self):
        self.assertTrue(TestLexer.test("a<====><=====b","a,<=,=,=,=,>,<=,=,=,=,=,b,<EOF>",902))
    def test_mixstyle3(self):
        self.assertTrue(TestLexer.test("dsf:,.()^jdks","dsf,:,,,Error Token .",903))
    def test_mixstyle4(self):
        self.assertTrue(TestLexer.test("procedure foo(); begin a := b[3] := foo(3)[5] := 5;end",
                                         "procedure,foo,(,),;,begin,a,:=,b,[,3,],:=,foo,(,3,),[,5,],:=,5,;,end,<EOF>",904))
    def test_mixstyle5(self):
        self.assertTrue(TestLexer.test("VAR a,b,c: integer, d:REal ","VAR,a,,,b,,,c,:,integer,,,d,:,REal,<EOF>",905))
    def test_mixstyle6(self):
        self.assertTrue(TestLexer.test("FUNCTION foo (a,b: integer; c: real): array [1 .. 2] of real;;            BEGIn      END",
                                        "FUNCTION,foo,(,a,,,b,:,integer,;,c,:,real,),:,array,[,1,..,2,],of,real,;,;,BEGIn,END,<EOF>",906))
    def test_mixstyle7(self):
        self.assertTrue(TestLexer.test("procedure main(); begin a := b[2]  := foo();a := b := c : 1;end",
                                       "procedure,main,(,),;,begin,a,:=,b,[,2,],:=,foo,(,),;,a,:=,b,:=,c,:,1,;,end,<EOF>",907))
    def test_mixstyle8(self):
        self.assertTrue(TestLexer.test("int: 789;float: 5.0E-4,BooleAN: True","int,:,789,;,float,:,5.0E-4,,,BooleAN,:,True,<EOF>",908))
    def test_mixstyle9(self):
        self.assertTrue(TestLexer.test("tons of float:1.e7 .7 .E110 5e17 5E-8.8 5E-4.e9","tons,of,float,:,1.e7,.7,Error Token .",909))
    def test_mixstyle10(self):
        self.assertTrue(TestLexer.test("var i: integer;function f ():integer;begin return 200;end procedure main ();",
        "var,i,:,integer,;,function,f,(,),:,integer,;,begin,return,200,;,end,procedure,main,(,),;,<EOF>",910))
    def test_mixstyle11(self):
        self.assertTrue(TestLexer.test("with a,b:integer;c:array[1 .. 2]of real;do d=c[a]+b;","with,a,,,b,:,integer,;,c,:,array,[,1,..,2,],of,real,;,do,d,=,c,[,a,],+,b,;,<EOF>",911))
