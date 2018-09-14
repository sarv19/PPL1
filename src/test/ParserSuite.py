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
        input = """VAR a,b,c: integer;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1105))
    def test_declare6(self):
        input = """VAR a,b,c: integer"""
        expect = "Error on line 1 col 18: <EOF>"
        self.assertTrue(TestParser.test(input,expect,1106))
    def test_declare6(self):
        input = """VAR a,b,c: integer, d:REal """
        expect = "Error on line 1 col 18: ,"
        self.assertTrue(TestParser.test(input,expect,1106))
    def test_declare7(self):
        input = """VAR a real;"""
        expect = "Error on line 1 col 6: real"
        self.assertTrue(TestParser.test(input,expect,1107))
    def test_declare8(self):
        input = """VAR a : xyz;"""
        expect = "Error on line 1 col 8: xyz"
        self.assertTrue(TestParser.test(input,expect,1108))
    def test_declare9(self):
        self.assertTrue(TestParser.test("var 12nhj: boolean;",
                            "Error on line 1 col 4: 12", 1109))
    def test_declare10(self):
        input = """VAR TayLorSwift"""
        expect = "Error on line 1 col 15: <EOF>"
        self.assertTrue(TestParser.test(input,expect,1110))
    def test_declare11(self):
        input = """var arr : array [5*7/5+4-(b+2) .. x*x mod 4] of integer;"""
        expect = "Error on line 1 col 18: *"
        self.assertTrue(TestParser.test(input,expect,1111))


########    test function declaration     ################
    def test_funcdeclare1(self):
        input = """FUNCTION foo(a,b:integer;c:real):real;
        Begin
          End"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2101))
    def test_funcdeclare2(self):
        input = """FUNCTION foo (a,b: integer; c: real): array [1 .. 2] of real;BEGIn      END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2102))
    def test_funcdeclare3(self):
        input = """FUNCTION foo (a,b: integer; c: real): array [1 .. 2] of real;
        var x,y:real;
                BEGIN
                END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2103))
    def test_funcdeclare4(self):
        input = """FUNCTION foo(a,b:integer;c:real):real;
        Begin
          End"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2104))
    def test_funcdeclare5(self):
        input = """FUNCTION foo():integer;
        Begin
        End"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2105))
    def test_funcdeclare6(self):
        input = """FUNCTION foo(a:real);
        Begin
        End"""
        expect = "Error on line 1 col 20: ;"
        self.assertTrue(TestParser.test(input,expect,2106))
    def test_funcdeclare7(self):
        input = """FUNcTION foo(xyz: aRRaY [1 .. 6] of real):integer;
        Begin
        End"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2105))
    def test_funcdeclare8(self):
        input = """FUNCTION foo (a,b: integer; c: real): array [1 .. 2] of real;;            BEGIn      END"""
        expect = "Error on line 1 col 61: ;"
        self.assertTrue(TestParser.test(input,expect,2108))
    def test_funcdeclare9(self):
        input = """FUNCTION foo(a:real;b:string;;);
        Begin
        End"""
        expect = "Error on line 1 col 28: ;"
        self.assertTrue(TestParser.test(input,expect,2109))
    def test_funcdeclare10(self):
        input = """FUNCTION foo(a:real);

        End"""
        expect = "Error on line 1 col 20: ;"
        self.assertTrue(TestParser.test(input,expect,2110))
    def test_funcdeclare11(self):
        input = """FUNCTION foo(a:real;b :string;
        Begin
        End"""
        expect = "Error on line 1 col 29: ;"
        self.assertTrue(TestParser.test(input,expect,2111))
    def test_funcdeclare12(self):
        input = """FUNCTION real(a:real;b :string;
        Begin
        End"""
        expect = "Error on line 1 col 9: real"
        self.assertTrue(TestParser.test(input,expect,2112))
    def test_funcdeclare13(self):
        input = """FUNCTION foo(a:real;);

        End"""
        expect = "Error on line 1 col 19: ;"
        self.assertTrue(TestParser.test(input,expect,2113))

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
        input = """procedure foo(a,b:integer; c:real;d,e,f:boolean;k:integer);
        var x,y: real;
        Begin
          End"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,3104))
    def test_procedeclare5(self):
        input = """procedure foo(a,b:integer);
        Begin
            BEGIN
            End
        End"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,3105))
        def test_procedeclare6(self):
            input = """procedure foo();
            Begin
            End"""
            expect = "successful"
            self.assertTrue(TestParser.test(input,expect,3106))
        input = """procedure foo(a,b:array [2 .. 4] of real);
        Begin
            BEGIN
            End
        End"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,3107))
    def test_procedeclare8(self):
        input = """procedure foo(a,b:integer):interger;
        Begin

        End"""
        expect = "Error on line 1 col 26: :"
        self.assertTrue(TestParser.test(input,expect,3108))
    def test_procedeclare9(self):
        input = """procedure foo();
        var x,y: real;
        var a,b: string;
        Begin
        End"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,3109))
    def test_procedeclare10(self):
        input = """procedure foo();
        var x,y: real;
        var a,b: string;
        Begin
        End
        BEGIn
        end"""
        expect = "Error on line 6 col 8: BEGIn"
        self.assertTrue(TestParser.test(input,expect,3110))
    def test_procedeclare11(self):
        input = """procedure foo();
        var x,y: real;
        var a,b: string;
        Begin
        //this is just a random cmt
        End
        BEGIn
        end"""
        expect = "Error on line 7 col 8: BEGIn"
        self.assertTrue(TestParser.test(input,expect,3111))
    def test_procedeclare12(self):
        input = """procedure foo();
        var x,y: real;
        var a,b: string;
        Begin
        End
        (*BEGIn
        this is totally fine :)
        end*)"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,3112))
    def test_procedeclare13(self):
        input = """procedure integer();
        var x,y: real;
        var a,b: string;
        Begin
        End
        (*BEGIn
        this is totally fine :)
        end*)"""
        expect = "Error on line 1 col 10: integer"
        self.assertTrue(TestParser.test(input,expect,3113))
    def test_procedeclare14(self):
        self.assertTrue(TestParser.test("procedure main(); begin end",
                                                  "successful",3114))
    def test_procedeclare15(self):
        input = """procedure multidimension(a : array [1..5,1..5] of real);
                begin
                end
                """
        expect = "Error on line 1 col 36: 1."
        self.assertTrue(TestParser.test(input,expect,3115))


###########       test expression       ############
    def test_expression1(self):
        input = """
        proCeDURE foo(a:integer);
        BEGIn
        foo(2)[3+x] := a[b[2]] +3;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,4101))
    def test_expression2(self):
        input = """
        proCeDURE foo(a:integer);
        var x, y: real;
        BEGIn
        foo(2)[3+x] := a[b[2]] +3;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,4102))
    def test_expression3(self):
        input = """
        FUNcTION foo(a:integer;c,d,f: boolean): integer;
        var y, u: real;
        BEGIn
        foo(2)[3+x] := a[b[2]] +3;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,4103))
    def test_expression4(self):
        input = """
        proCeDURE foo(a:integer);
        BEGIn
        foo(x);
        fooo(y,z);
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,4104))
    def test_expression5(self):
        input = """
        proCeDURE foo(a:integer);
        var y: array [-5 .. -6] of real;
        BEGIn
        foo(x);
        fooo(y,z);
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,4105))
    def test_expression6(self):
        input = """
        proCeDURE foo(a:integer);
        var y: array [-5 .. -6] of real;
        BEGIn
        foo(x);
        fooo(y,z);
        a :=b[10]:=foo()[3]:=x:=1;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,4106))
    def test_expression7(self):
        input = """
        funcTION foo(a:integer): REal;
        var y: array [-5 .. -6] of real;
        BEGIn
        a :=b[10]:=foo()[3]:=x:=1;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,4107))
    def test_expression8(self):
        input = """
        funcTION foo(a:integer): REal;
        var y: array [-5 .. -6] of real;
        BEGIn
        a :=b[10]:=foo()[3]:=x:=1
        end
        """
        expect = "Error on line 6 col 8: end"
        self.assertTrue(TestParser.test(input,expect,4108))
    def test_expression9(self):
        input = """
        procedure main();
        begin
            vec[1] := vec[2] := vector[3] := 0;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,4109))
    def test_expression10(self):
        input = """
        procedure main();
        begin
            ohyeah="ohno";
        end
        """
        expect = "Error on line 4 col 18: ="
        self.assertTrue(TestParser.test(input,expect,4110))
    def test_expression11(self):
        input = """
        procedure main();
        var k: boolean;
        begin
            vec[1] := vec[2] := vector[3] := foo()[b] := a;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,4111))
    def test_expression12(self):
        input = """
        procedure main();
        begin
            return foo();
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,4112))
    def test_expression13(self):
        input = """
        procedure main();
        begin
            a:=b[10]:=foo()[3]:=x:=1;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,4113))
    def test_expression14(self):
        input = """
        funcTION weird(aa:real): boolean;
        var x,t: array[1 .. -6] of real;
        begin
            a:=b[10]:=foo()[3]:=x:=1;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,4114))
    def test_expression15(self):
        input = """
        funcTION weird(aa:real): boolean;
        var x,t: array[1 .. -6] of real;
        begin
            x:=getInt(stdin);
            y:=x*2;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,4115))
    def test_expression16(self):
        input = """
        procedure ex(x: string);
        begin
		      begin
                x:="you did good"; if a>b then g:=h:=foo();
                return x;
		      end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,4116))
    def test_expression17(self):
        input = """
        procedure ex(x: string);
        begin
		      begin
                if a>b then g:=h:=foo();
                return x;
		      end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,4117))
    def test_expression18(self):
        input = """
        procedure ex(x: string);
        begin
		      begin
                if a>b then g:=h:=foo();
                else h:=5;
                return x;
		      end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,4118))
    def test_expression19(self):
        input = """
        procedure ex(x: string);
        begin
		      begin
                if a := b then g:=h:=foo();
                else h:=5;
                return x;
		      end
        end
        """
        expect = "Error on line 5 col 21: :="
        self.assertTrue(TestParser.test(input,expect,4119))
    def test_expression20(self):
        input = """
        procedure foo();
           begin
             a := a[d < y(5 > 3) + 3 * n(12)] := 5[3] := 3[2] := b;
           end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,4120))
    def test_expression21(self):
        input = """
        procedure ex(x: boolean);
		      begin
                if a>b then x:= a or b or c and d;
                else h:= a mod c div c;
                return x;
		      end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,4121))
    def test_expression22(self):
        input = """
        procedure ex(x: string);
        begin
		      begin
                if a mod b then g:=h:=foo();
                else h:=5;
                return x;
		      end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,4122))
    def test_expression23(self):
        input = """
        procedure ex(x: string);
        begin
		      begin
                while (i<100) do
                    begin
	                   j:=2;
	                      while ( j<= (i div j)) do
	                         begin
		                           if (i mod j <> 0 ) then break;
		                           j:= j+1;
	                         end
                    end
		      end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,4123))
    def test_expression24(self):
        input = """
        procedure ex(x: string);
        begin
		      while a= true do a:=foo();
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,4124))
    def test_expression25(self):
        input = """
        procedure main();
            begin
	           var a,b: integer;
                    c: array [1..100] of integer;
	           c:[a]= b+100 mod 5;
            end
        """
        expect = "Error on line 4 col 12: var"
        self.assertTrue(TestParser.test(input,expect,4125))
    def test_expression26(self):
        input = """
        procedure main();
            begin
	           while a > 5 do b:=c
            end
        """
        expect = "Error on line 5 col 12: end"
        self.assertTrue(TestParser.test(input,expect,4126))
    def test_expression27(self):
        input = """
        procedure main();
            begin
	           for temp := a*b+c to temp=25
               do a:=b*c div f;
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,4127))
    def test_expression28(self):
        input = """
        function check (a,b,c : integer) : boolean;
            begin
	           return a>b<c;
            end
        """
        expect = "Error on line 4 col 22: <"
        self.assertTrue(TestParser.test(input,expect,4128))
    def test_expression29(self):
        input = """
        procedure main();
            begin
	           for temp := a*b+c downto temp=25
               do a:=b*c div f;
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,4129))
    def test_expression30(self):
        input = """
        procedure main();
            begin
	           for temp := a*b+c downto temp=25
               do a:=b*c div f;
               break;
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,4130))
    def test_expression31(self):
        input = """
        procedure main();
            begin
               COnTINue;
	           for temp := a*b+c downto temp=25
               do a:=b*c div f;
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,4131))
    def test_expression32(self):
        input = """
        procedure main();
            begin
	           while a > 5 do b:=c;
               break;
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,4132))
    def test_expression33(self):
        input = """
        procedure main();
            begin
	           while a > 5 do b:=c;
               COnTINue;
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,4133))
    def test_expression34(self):
        input = """
        procedure ex(x: string);
        begin
		      begin
                if a mod b then g:=h:=foo();
                else h:=5;
                break;
                return x;
		      end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,4134))
    def test_expression35(self):
        input = """
        procedure chaof ();
        begin
        	hello();
        	begin
        		hi();
        		begin
        			bye()
        			begin
        			end
        		end
        	end
        end
        """
        expect = "Error on line 9 col 11: begin"
        self.assertTrue(TestParser.test(input,expect,4135))
    def test_expression36(self):
        input = """
        function ln(x: real): real;
            var result, element, EPSILON: real;
             i: integer;
            begin
            EPSILON := 1e-6;
            result := 0;
             	element := x;
            i := 1;
             	while (abs(element) > EPSILON) do
            begin
            result := result + element;
            element := element*(-x*i/(i + 1));
             	end
            return result;
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,4136))
    def test_expression37(self):
        input = """
        function cosine(x: real): real;
             var result, element, EPSILON: real;
             i: integer;
             begin
             EPSILON := 1e-6;
             result := 0; element := 1;
             i := 1;
            while (abs(element) > EPSILON) do
            begin
           result := result + element;
           element := element*(-x*x/(i*(i + 1)));
           i := i + 2;
            end
           return result;
           end

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,4137))
    def test_expression38(self):
        input = """
        function sine(x: real): real;
             var result, element, EPSILON: real; i: integer;
              begin
              	EPSILON := 1e-6;
                 	result := 0; element := x;
                	i := 1;
                while (abs(element) > EPSILON) do
                 begin
                     	result := result + element;
                     	element := element * (-x*x/((i + 1)*(i + 2)));
                     	i := i + 2;
                 end
                 return result;
             end

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,4138))
    def test_expression39(self):
        input = """
        function pow(x: real; exp: integer): real;
             var i: integer;
             begin
                 	if (exp = 0) then return 1.0;
                       for i := 2 to exp do
                     	x := x * x;
                         return x;
             end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,4139))
    def test_expression40(self):
        input = """
        procedure main();
             var a, b, c, x, x1, x2, delta: real;
             begin
                 putString("Enter coefficient a: ");
                 a := getFloat();
                 putString("Enter coefficient b: ");
                 b := getFloat();
                 putString("Enter coefficient c: ");
                 c := getFloat();
                 if (a = 0) and (b = 0) then
                 begin
                     if (c = 0) then
                         putStringLn("The equation has many solution.");
                     else
                         putStringLn("The equation has no solution.");
                 end
                 else if (a = 0) then
                 begin
                     x := -c/b;
                     putString("The solution x = ");
                     putFloatLn(x);
                 end
                 else
                 begin
                     delta := b*b - 4*a*c;
                     if (delta < 0) then
                          putStringLn("The equation has no solution.");
                     else if (delta < 0) then
                     begin
                         x := -b/(2*a);
                         putString("The equation has 1 solution x = ");
                         putFloatLn(x);
                     end
                     else
                     begin                         // Assume we have square root function in MP
                         x1 := (-b + sqrt(delta))/(2*a);
                         x2 := (-b - sqrt(delta))/(2*a);
                         putString("The equation has 2 solutions x1 = ");
                         putFloat(x1);
                         putString(" and x2 = ");
                         putFloatLn(x2);
                     end
                 end
             end

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,4140))
    def test_expression41(self):
        input = """
        procedure main();
            begin
	           with a,b:integer;c:array[1 .. 2]of real;
               do d:=c[a]+b;
               COnTINue; //to where i dont know
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,4141))
    def test_expression42(self):
        input = """
        procedure main();
            begin
	           with a,b:integer;c:array[1 .. 2]of real;
               do d:=c[a]+b;
               COnTINue; //to where i dont know
               {oh wait I do know, i should call something ^^}
               foo(3,a+1,m(2));
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,4142))
    def test_expression43(self):
        input = """
        var seed: integer;
             procedure srand(x: integer);
             begin
                 seed := x;
             end
             function rand(): integer;
             begin
                 seed := (seed * 1103515245 + 12345) mod RAND_MAX;
             end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,4143))
    def test_expression44(self):
        input = """
        function ln(x: real): real;
            var result, element, EPSILON: real;
             i: integer;
            begin
            EPSILON := 1e-6;
            result := 0;
             	element := x;
            i := 1;
             	while (abs(element) > EPSILON) do
            begin
            result := result + element;
            element := element*(-x*i/(i + 1));
             	end
            return result;
        """
        expect = "Error on line 16 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,4144))
