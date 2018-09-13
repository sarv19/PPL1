import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_var_dec_1(self):
        self.assertTrue(TestParser.test("var i: real;", "successful", 201))

    def test_var_dec_2(self):
        self.assertTrue(TestParser.test("var a, c, d: integer;", "successful", 202))

    def test_var_dec_3(self):
        self.assertTrue(TestParser.test("var new_id: boolean;", "successful", 203))

    def test_var_dec_4(self):
        self.assertTrue(TestParser.test("var : real;", "Error on line 1 col 4: :", 204))

    def test_var_dec_5(self):
        self.assertTrue(TestParser.test("var arr: array [1 .. 10] of string;", "successful", 205))

    def test_var_dec_6(self):
        self.assertTrue(TestParser.test("var 1293: boolean;", "Error on line 1 col 4: 1293", 206))

    def test_var_dec_7(self):
        self.assertTrue(TestParser.test("var str: string", "Error on line 1 col 15: <EOF>", 207))

    def test_var_dec_8(self):
        self.assertTrue(TestParser.test("var a,b,c: integer;\n e,f: real;", "successful", 208))

    def test_var_dec_9(self):
        self.assertTrue(TestParser.test("var a: boolean; var b,c: integer;", "successful", 209))

    def test_var_dec_10(self):
        self.assertTrue(TestParser.test("var may: integer; em, fM: real;\n var vector: array [1 .. 20] of real;", "successful", 210))

    def test_var_dec_11(self):
        self.assertTrue(TestParser.test("var ieee: real; red, blue, green: integer;", "successful", 211))

    def test_var_dec_12(self):
        self.assertTrue(TestParser.test("var b d e f: integer", "Error on line 1 col 6: d", 212))

    def test_var_dec_13(self):
        self.assertTrue(TestParser.test("var __init__: float;", "Error on line 1 col 14: float", 213))

    def test_var_dec_14(self):
        self.assertTrue(TestParser.test("var rl, im: real; x_axis, y_axis: array [1 .. 200] of real;", "successful", 214))

    def test_var_dec_15(self):
        self.assertTrue(TestParser.test("var polygon;", "Error on line 1 col 11: ;", 215))

    def test_proc_dec_1(self):
        self.assertTrue(TestParser.test("procedure main(); begin end", "successful", 216))

    def test_proc_dec_2(self):
        self.assertTrue(TestParser.test("procedure sum(vector: array [1 .. 10] of real); begin end", "successful", 217))

    def test_proc_dec_3(self):
        self.assertTrue(TestParser.test("procedure foobar; begin end", "Error on line 1 col 16: ;", 218))

    def test_proc_dec_4(self):
        self.assertTrue(TestParser.test("procedure fibonacci(n: integer;); begin end", "Error on line 1 col 31: )", 219))

    def tets_proc_dec_5(self):
        self.assertTrue(TestParser.test("procedure id10t(); var loc_var: real; begin end", "successful", 220))

    def test_proc_dec_6(self):
        self.assertTrue(TestParser.test("procedure main(); var a,b,c: integer; e,f: real; begin end", "successful", 221))

    def test_proc_dec_7(self):
            self.assertTrue(TestParser.test("procedure sin(x: real): real; begin end", "Error on line 1 col 22: :", 222))

    def test_proc_dec_8(self):
        self.assertTrue(TestParser.test("procedure printFilter(filter_str: string);", "Error on line 1 col 42: <EOF>", 223))

    def test_proc_dec_9(self):
        self.assertTrue(TestParser.test("procedure 1234(); begin end", "Error on line 1 col 10: 1234", 224))

    def test_proc_dec_10(self):
        self.assertTrue(TestParser.test("procedure printCmd(mode: integer; pprint: boolean; cmdList: array [1 .. 10] of string); begin end", "successful", 225))

    def test_func_dec_1(self):
        self.assertTrue(TestParser.test("function cos(x: real): real; begin end", "successful", 226))

    def test_func_dec_2(self):
        self.assertTrue(TestParser.test("function main(argc: integer; argv: array [1 .. 10] of string): integer; begin end", "successful", 227))

    def test_func_dec_3(self):
        self.assertTrue(TestParser.test("function zeroVector(): array [1 .. 50] of real; begin end", "successful", 228))

    def test_func_dec_4(self):
        self.assertTrue(TestParser.test("function missReturn(); begin end", "Error on line 1 col 21: ;", 229))

    def test_func_dec_5(self):
        self.assertTrue(TestParser.test("function wrongParam(i: integer;): real; begin end", "Error on line 1 col 31: )", 230))

    def test_func_dec_6(self):
        self.assertTrue(TestParser.test("function 1llega1_name(): boolean; begin end", "Error on line 1 col 9: 1", 231))

    def test_func_dec_7(self):
        self.assertTrue(TestParser.test("function missParam: real; begin end", "Error on line 1 col 18: :", 232))

    def test_func_dec_8(self):
        self.assertTrue(TestParser.test("function wrongType(): int; begin end", "Error on line 1 col 22: int", 233))

    def test_func_dec_9(self):
        self.assertTrue(TestParser.test("noKeyword(): string; begin end", "Error on line 1 col 0: noKeyword", 234))

    def test_func_dec_10(self):
        self.assertTrue(TestParser.test("function noBody(): integer;", "Error on line 1 col 27: <EOF>", 235))

    def test_assignment_stmt_1(self):
        self.assertTrue(TestParser.test("""
            procedure main(); var i: integer; var flag: boolean;
            begin
                i := 100;
                flag := true;
            end
        """, "successful", 236))

    def test_assignment_stmt_2(self):
        self.assertTrue(TestParser.test("""
            procedure main(); var vector: array [1 .. 3] of integer;
            begin
                vector[1] := vector[2] := vector[3] := 0;
            end
        """, "successful", 237))

    def test_assignment_stmt_3(self):
        self.assertTrue(TestParser.test("""
            procedure missSemi(); var temp: real;
            begin
                temp := 0
            end
        """, "Error on line 5 col 12: end", 238))

    def test_assignment_stmt_4(self):
        self.assertTrue(TestParser.test("""
            procedure wrongAssign(); var j: string;
            begin
                j = "a string";
            end
        """, "Error on line 4 col 18: =", 239))

    def test_assignment_stmt_5(self):
        self.assertTrue(TestParser.test("""
            procedure composition(x: real); var i, j: integer; vector: array [1 .. 3] of real;
            begin
                i := j := vector[2] := foo()[1] := x;
            end
        """, "successful", 240))

    def test_for_stmt_1(self):
        self.assertTrue(TestParser.test("""
            procedure main(); var i: integer;
            begin
                for i := 1 to 10 do
                begin
                    putString("Count: ");
                    putIntLn(i);
                end
            end
        """, "successful", 241))

    def test_for_stmt_2(self):
        self.assertTrue(TestParser.test("""
            procedure count(n: integer); var i: integer;
            begin
                for i := n downto 1 do
                begin
                    putString("Countdown: ");
                    putIntLn(i);
                end
            end
        """, "successful", 242))

    def test_for_stmt_3(self):
        self.assertTrue(TestParser.test("""
            procedure incrementByN(x,n,count: integer); var i: integer;
            begin
                for i := 1 to count do
                begin
                    x := x + n;
                end
            end
        """, "successful", 243))

    def test_for_stmt_4(self):
        self.assertTrue(TestParser.test("""
            procedure wrongSyntax(); var i: integer;
            begin
                for i := 0; i < 10; i++ do
                begin
                end
            end
        """, "Error on line 4 col 26: ;", 244))

    def test_for_stmt_5(self):
        self.assertTrue(TestParser.test("""
            procedure missDo(); var i: integer;
            begin
                for i := 1 to 5
                begin
                end
            end
        """, "Error on line 5 col 16: begin", 245))

    def test_if_stmt_1(self):
        self.assertTrue(TestParser.test("""
            procedure main(); var i: integer;
            begin
                for i := 0 to 10 do
                begin
                    if (i mod 2 = 0) then
                        putIntLn(i);
                end
            end
        """, "successful", 246))

    def test_if_stmt_2(self):
        self.assertTrue(TestParser.test("""
            procedure compoundIf(a,b: integer);
            begin
                if (a < 0) then
                begin
                    a := -a;
                    b := 100;
                end
            end
        """, "successful", 247))

    def test_if_stmt_3(self):
        self.assertTrue(TestParser.test("""
            procedure compareGreater(a,b: real);
            begin
                if (a > b) then
                    putStringLn("a is greater than b");
                else
                    putStringLn("b is greater or equal to a");
            end
        """, "successful", 248))

    def test_if_stmt_4(self):
        self.assertTrue(TestParser.test("""
            procedure main();
            var a,b: real;
            begin
                if (a) then if (b) then putStringLn("nested");
                else putRealLn(a);
            end
        """, "successful", 249))

    def test_if_stmt_5(self):
        self.assertTrue(TestParser.test("""
            procedure quadraticDelta(delta: real);
            begin
                if (delta > 0)
                    putStringLn("2 solutions");
                else
                begin
                    if (delta < 0) putStringLn("No solution");
                    else putStringLn("1 solution");
                end
            end
        """, "Error on line 5 col 20: putStringLn", 250))

    def test_if_stmt_6(self):
        self.assertTrue(TestParser.test("""
            function max(vector: array [1 .. 10] of integer): integer;
            var i, max: integer;
            begin
                max := vector[1];
                for i := 2 to 10 do
                begin
                    if (vector[i] > max) then max := vector[i];
                end

                return max;
            end
        """, "successful", 251))

    def test_while_stmt_1(self):
        self.assertTrue(TestParser.test("""
            procedure main();
            var i: integer;
            begin
                i := 0;
                while i < 10 do i := i + 1;
            end
        """, "successful", 252))

    def test_while_stmt_2(self):
        self.assertTrue(TestParser.test("""
            function fibonacci(n: integer): integer;
            var prev, val, tmp: integer;
            begin
                prev := val := 1;
                while (true) do
                begin
                    tmp := val;
                    val := val + prev;
                    prev := tmp;
                    if (val >= n) then break;
                end

                return val;
            end
        """, "successful", 253))

    def test_while_stmt_3(self):
        self.assertTrue(TestParser.test("""
            procedure findPrime();
            var i,j: integer;
            begin
                i := 2;
                while (i < 100) do
                begin
                    j := 2;
                    while (j <= (i div j)) do
                    begin
                        if (i mod j <> 0) then break;
                        j := j + 1;
                    end
                    if (j > (i div j)) then
                    begin
                        putInt(i);
                        putStringLn(" is prime");
                        i := i + 1;
                    end
                end
            end
        """, "successful", 254))

    def test_while_stmt_4(self):
        self.assertTrue(TestParser.test("""
            procedure main();
            begin
                while true
                begin
                    break;
                end
            end
        """, "Error on line 5 col 16: begin", 255))

    def test_while_stmt_5(self):
        self.assertTrue(TestParser.test("""
            procedure wrongKeyword();
            var i,j,val: integer;
            begin
                val := 2;
                for i := 1 to 3 do
                begin
                    j := 0;
                    whil j < 10 do
                    begin
                        val := val*2;
                        j := j + 1;
                    end
                end
            end
        """, "Error on line 9 col 25: j", 256))

    def test_with_stmt_1(self):
        self.assertTrue(TestParser.test("""
            procedure main();
            begin
                with a,b: integer; c: array [1 .. 2] of real; do
                    d := c[a] + b;
            end
        """, "successful", 257))

    def test_with_stmt_2(self):
        self.assertTrue(TestParser.test("""
            procedure main();
            var flag: integer;
            begin
                flag := 200;
                with flag: integer; do
                    flag := 100;
                putIntLn(flag);
            end
        """, "successful", 258))

    def test_with_stmt_3(self):
        self.assertTrue(TestParser.test("""
            procedure main();
            begin
                wth a: real; do
            end
        """, "Error on line 4 col 20: a", 259))

    def test_with_stmt_4(self):
        self.assertTrue(TestParser.test("""
            procedure main();
            begin
                with do
            end
        """, "Error on line 4 col 21: do", 260))

    def test_with_stmt_5(self):
        self.assertTrue(TestParser.test("""
            procedure main();
            var vector: array [1 .. 3] of integer;
            begin
                with a,b,c: integer; do
                begin
                    a := vector[1];
                    b := vector[2];
                    c := vector[3];
                end
            end
        """, "successful", 261))

    def test_expr_1(self):
        self.assertTrue(TestParser.test("""
            procedure main();
            var a,b,c,d,e: integer;
            begin
                a := b := c := d := e := 5;
            end
        """, "successful", 262))

    def test_expr_2(self):
        self.assertTrue(TestParser.test("""
            function quadraticEq(a,b,c,x: real): real;
            begin
                return a*x*x + b*x + c;
            end
        """, "successful", 263))

    def test_expr_3(self):
        self.assertTrue(TestParser.test("""
            procedure main();
            var val: integer;
            begin
                val := 100 / 2 + 5 * 10 mod 3;
            end
        """, "successful", 264))

    def test_expr_4(self):
        self.assertTrue(TestParser.test("""
            procedure invalidOp();
            var i: real;
            begin
                i := 1.5;
                i += 7.5;
            end
        """, "Error on line 6 col 18: +", 265))

    def test_expr_5(self):
        self.assertTrue(TestParser.test("""
            procedure relationOp();
            var a,b,c: integer;
            begin
                if (a > b) then c := 100;
                else c := 200;
            end
        """, "successful", 266))

    def test_expr_6(self):
        self.assertTrue(TestParser.test("""
            function nonAssocRelation(a,b,c: integer): boolean;
            begin
                return a > b > c;
            end
        """, "Error on line 4 col 29: >", 267))

    def test_expr_7(self):
        self.assertTrue(TestParser.test("""
            function AndOr(andFLag: boolean; a,b: integer): integer;
            begin
                if (andFlag= true) then
                    return a and b;
                else
                    return a or b;
            end
        """, "successful", 268))

    def test_expr_8(self):
        self.assertTrue(TestParser.test("""
            function XorOp(a,b: boolean): boolean;
            begin
                return a and not b or not a and b;
            end
        """, "successful", 269))

    def test_expr_9(self):
        self.assertTrue(TestParser.test("""
            function shortCircuitAnd(a,b,c: boolean): boolean;
            begin
                return a and then b and then c;
            end
            function shortCircuitOr(a,b,c: boolean): boolean;
            begin
                return a or else b or else c;
            end
        """, "successful", 270))

    def test_expr_10(self):
        self.assertTrue(TestParser.test("""
            procedure indexExpr();
            begin
                foo(2)[3+x] := a[b[2]] + 3;
            end
        """, "successful", 271))

    def test_var_dec_16(self):
        self.assertTrue(TestParser.test("""
            procedure multiDimArray();
            var i: array [1 .. 2 ,3 .. 4] of integer;
            begin
            end
        """, "Error on line 3 col 33: ,", 272))

    def test_return_stmt_1(self):
        self.assertTrue(TestParser.test("""
            function tan(x: real): real;
            begin
                return sin(x)/cos(x);
            end
        """, "successful", 273))

    def test_return_stmt_2(self):
        self.assertTrue(TestParser.test("""
            procedure main();
            var a: integer;
            begin
                a := 10;
                while true do
                begin
                    if a = 0 then return;
                    a := a - 1;
                end
            end
        """, "successful", 274))

    def test_return_stmt_3(self):
        self.assertTrue(TestParser.test("""
            procedure wrongKeyword();
            begin
                retun 1;
            end
        """, "Error on line 4 col 22: 1", 275))

    def test_break_cont_1(self):
        self.assertTrue(TestParser.test("""
            procedure main();
            var i,a: integer;
            begin
                for i := 0 to 6 do
                    if i = 3 then break;
                    else continue;
            end
        """, "successful", 276))

    def test_break_cont_2(self):
        self.assertTrue(TestParser.test("""
            procedure wrongBreak();
            begin
                brek;
            end
        """, "Error on line 4 col 20: ;", 277))

    def test_break_cont_3(self):
        self.assertTrue(TestParser.test("""
            procedure wrongCont();
            begin
                continu;
            end
        """, "Error on line 4 col 23: ;", 278))

    def test_compound_1(self):
        self.assertTrue(TestParser.test("""
            function missBegin(): integer;
                return 10;
            end
        """, "Error on line 3 col 16: return", 279))

    def test_compound_2(self):
        self.assertTrue(TestParser.test("""
            function missEnd(): real;
            begin
                return 9.6;
        """, "Error on line 5 col 8: <EOF>", 280))

    def test_compound_3(self):
        self.assertTrue(TestParser.test("""
            procedure nestedCompound();
            begin
                callThis();
                begin
                    begin
                        begin
                            callThat();
                        end
                        callThese();
                    end
                    callThose();
                end
            end
        """, "successful", 281))

    # From this location, the test will concentrate on creating functions, programs, etc,...
    # Not just testing individual expression, statement anymore
    # These tests is a conversion from programs written in another language
    # These tests MUST be successful.

    def test_program_1(self):
        self.assertTrue(TestParser.test("""
            {* Project Euler problem number 1 *}
            { Find the sum of the multiples of 3 or 5 below 1000 }
            function proj_euler_1(): integer;
            var sum, i: integer;
            begin
                sum := 0;
                for i := 0 to 999 do
                    if (i mod 3 = 0) or (i mod 5 = 0) then sum := sum + i;
            end
        """, "successful", 282))

    def test_program_2(self):
        self.assertTrue(TestParser.test("""
            {* Project Euler problem number 2 *}
            { Find the sum of even numbers in Fibonacci sequence
              The maximum Fibonacci number do not exceed 4 million }
            function sumFibo(): integer;
            var prev, curr, tmp, sum: integer;
            begin
                sum := 0;
                curr := prev := 1;
                while (curr < 4000000) do
                begin
                    if (curr mod 2 = 0) then sum := sum + curr;
                    // Advancing the Fibonacci number
                    tmp := curr;
                    curr := curr + prev;
                    prev := tmp;
                end
            end
        """, "successful", 283))

    def test_program_3(self):
        self.assertTrue(TestParser.test("""
            {* Sorting program: Integer insertion sort *}
            { Sort array of integer of size 1000
              in ascending order and return the sorted array }
            function InsertionSort(arr: array [1 .. 1000] of integer): array [1 .. 1000] of integer;
            var i, j, key: integer;
            begin
                for i := 2 to 1000 do
                begin
                    key := arr[i];
                    j := i - 1;
                    while (j >= 0) and (arr[j] > key) do
                    begin
                        arr[j + 1] := arr[j];
                        j := j - 1;
                    end
                    arr[j + 1] := key;
                end

                return arr;
            end
        """, "successful", 284))

    def test_program_4(self):
        self.assertTrue(TestParser.test("""
            {* Sorting program: Selection sort *}
            { Sort an array of 50000 of integer in ascending order then return the array }
            function SelectionSort(arr: array [1 .. 50000] of integer): array [1 .. 50000] of integer;
            var i, j, minIndex, tmp: integer;
            begin
                for i := 1 to 49999 do
                begin
                    minIndex := i;
                    for j := i + 1 to 50000 do
                        if (arr[j] < arr[minIndex]) then minIndex := j;
                    if (minIndex <> i) then
                    begin
                        // Swap the value
                        tmp := arr[i];
                        arr[i] := arr[minIndex];
                        arr[minIndex] := tmp;
                    end
                end

                return arr;
            end
        """, "successful", 285))

    def test_program_5(self):
        self.assertTrue(TestParser.test("""
            {* Sorting program: Bubble sort *}
            { Sort an integer array of 10000 in ascending order then return the array }
            function BubbleSort(arr: array [1 .. 10000] of integer): array [1 .. 10000] of integer;
            var i, j, tmp: integer; swapped: boolean;
            begin
                swapped := true;
                while (swapped) do
                begin
                    swapped := false;
                    for i := 1 to 9999 do
                    begin
                        for j := i to 999 do
                            if (arr[j] > arr[j + 1]) then
                            begin
                                tmp := arr[j];
                                arr[j] := arr[j + 1];
                                arr[j + 1] := tmp;
                                swapped := true;
                            end
                    end
                end

                return arr;
            end
        """, "successful", 286))

    def test_program_6(self):
        self.assertTrue(TestParser.test("""
            {* Binary search *}
            { Given an integer array of size 100, find if there is an existing number in that array}
            function BinarySearch(list: array [1 .. 100] of integer; number: integer): boolean;
            var left, right, mid: integer;
            begin
                left := 1;
                right := 100;
                while (left <= right) do
                begin
                    // We assume that div function is a floor function
                    mid := (left + right) div 2;
                    if (list[mid] < number) then
                        left := mid + 1;
                    else if (list[mid] > number) then
                        right := mid - 1;
                    else return true;
                end

                return false;
            end
        """, "successful", 287))

    def test_program_7(self):
        self.assertTrue(TestParser.test("""
            {* Psuedo-random number generator *}
            { This implementation is a conversion from C' PRNG
              that generates 32-bit numbers }

            var seed: integer;

            procedure srand(x: integer);
            begin
                seed := x;
            end
            function rand(): integer;
            begin
                seed := (seed * 1103515245 + 12345) mod RAND_MAX;
            end
        """, "successful", 288))

    def test_program_8(self):
        self.assertTrue(TestParser.test("""
            {* Qadratic Eq. calculator *}
            { This program takes input of coefficients a,b,c and calculate x }
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
                    begin
                        // Assume we have square root function in MP
                        x1 := (-b + sqrt(delta))/(2*a);
                        x2 := (-b - sqrt(delta))/(2*a);
                        putString("The equation has 2 solutions x1 = ");
                        putFloat(x1);
                        putString(" and x2 = ");
                        putFloatLn(x2);
                    end
                end
            end
        """, "successful", 289))

    def test_program_9(self):
        self.assertTrue(TestParser.test("""
            {* Fibonacci value generator *}
            { Generate Fibonacci nth number }
            function Fibonacci(n: integer): integer;
            var f, a, b, i: integer;
            begin
                if (n < 2) then return 1;

                f := 0; a := b := 1;
                for i := 2 to n do
                begin
                    f := a + b;
                    a := b;
                    b := f;
                end

                return f;
            end
        """, "successful", 290))

    def test_program_10(self):
        self.assertTrue(TestParser.test("""
            {* Factorial generator *}
            { Generate factorial of N }
            function TailCallFac(accumulator, n: integer): integer;
            begin
                if (n < 2) then return acc;

                return TailCallFac(n*accumulator, n - 1);
            end
            function Factorial(N: integer): integer;
            begin
                return TailCallFac(1, N);
            end
        """, "successful", 291))

    def test_program_11(self):
        self.assertTrue(TestParser.test("""
            {* Math library - Power of *}
            { Return the nth power of x }
            function pow(x: real; exp: integer): real;
            var i: integer;
            begin
                if (exp = 0) then return 1.0;

                for i := 2 to exp do
                    x := x * x;

                return x;
            end
        """, "successful", 292))

    def test_program_12(self):
        self.assertTrue(TestParser.test("""
            {* Linear Eq. calculator *}
            { Calculate x given coefficients a,b }
            procedure LinearEq(a,b: real);
            var a,b,x: real;
            begin
                putString("Enter coefficient a: ");
                a := getFloat();
                putString("Enter coefficient b: ");
                b := getFloat();

                if (a = 0) then
                begin
                    if (b = 0) then putStringLn("There are infinite solutions");
                    else putStringLn("There is no solution.");
                end
                else
                begin
                    x := -b/a;
                    putString("The solution is x = ");
                    putFloatLn(x);
                end
            end
        """, "successful", 293))

    def test_program_13(self):
        self.assertTrue(TestParser.test("""
            {* Simple hello world program *}
            procedure main();
            begin
                putStringLn("Hello, World!");
            end
        """, "successful", 294))

    def test_program_14(self):
        self.assertTrue(TestParser.test("""
            {* Interactive adder *}
            procedure main();
            var a,b,x: real;
            begin
                putString("Enter first number: ");
                a := getFloat();
                putString("Enter second number: ");
                b := getFloat();

                putString("The sum of 2 numbers: ");
                x := a + b;
                putFloatLn(x);
            end
        """, "successful", 295))

    def test_program_15(self):
        self.assertTrue(TestParser.test("""
            {* Math library - Return absolute value *}
            function abs(x: real): real;
            begin
                if (x < 0) then return -x;
                else return x;
            end
        """, "successful", 296))

    def test_program_16(self):
        self.assertTrue(TestParser.test("""
            {* Math library - return sine value given radian *}
            { The program use Taylor MacLaurin approximation }
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
        """, "successful", 297))

    def test_program_17(self):
        self.assertTrue(TestParser.test("""
            {* Math library - return cosine value given radian *}
            { The program use Taylor MacLaurin approximation }
            function cosine(x: real): real;
            var result, element, EPSILON: real; i: integer;
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
        """, "successful", 298))

    def test_program_18(self):
        self.assertTrue(TestParser.test("""
            {* Math library - return natural logarithm value given value x *}
            { The program use Taylor MacLaurin approximation }
            function ln(x: real): real;
            var result, element, EPSILON: real; i: integer;
            begin
                EPSILON := 1e-6;
                result := 0; element := x;
                i := 1;

                while (abs(element) > EPSILON) do
                begin
                    result := result + element;
                    element := element*(-x*i/(i + 1));
                end

                return result;
            end
        """, "successful", 299))

    def test_program_19(self):
        self.assertTrue(TestParser.test("""
            {* Data structure - Stack *}
            { Implementing float 'stack operation (push, pop, top, size, empty) with limited size (100,000) }
            var g_stack: array [1 .. 100000] of real;
            var sp, size: integer;

            { Stack initialization
              MUST be called before doing any stack operations }
            procedure s_init();
            begin
                sp := 1;
                size := 100000;
            end
            { Push an element into stack
              Return 0 when succeeded, -1 otherwise (stack overflow) }
            function s_push(x: real): integer;
            begin
                if (sp > size) then return -1;

                g_stack[sp] := x;
                sp := sp + 1;
                return 0;
            end
            { Pop an element out of the stack
              Return 0 when succeeded, -1 otherwise (stack underflow) }
            function s_pop(): integer;
            begin
                if (sp < 1) then return -1;

                sp := sp - 1;
                return 0;
            end
            { Get the top element of the stack
              Only call when the stack is not empty - otherwise can cause runtime error }
            function s_top(): real;
            begin
                return g_stack[sp - 1];
            end
            { Check the stack size }
            function s_size(): integer;
            begin
                return size;
            end
            { Check if the stack is empty }
            function s_empty(): boolean;
            begin
                if (sp > 1) and then (sp <= size) then return false;
                else return true;
            end
        """, "successful", 300))

    def test_program_20(self):
        self.assertTrue(TestParser.test("""
            {* MP test progarm - example in MP specification *}
            var i: integer;
            function f(): integer;
            begin
                return 200;
            end
            procedure main();
            var
                main: integer;
            begin
                main := f();
                putIntLn(main);
                with
                    i: integer;
                    main: integer;
                    f: integer;
                do begin
                    main := f := i := 100;
                    putIntLn(i);
                    putIntLn(main);
                    putIntLn(f);
                end
                putIntLn(main);
            end
            var g: real;
        """, "successful", 301))
