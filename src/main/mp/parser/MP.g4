grammar MP;

//1652458
@lexer::header {
from lexererr import *
}  //commnent out this

options{
	language=Python3; //=Java
	//language=Java;
}
program: manydeclares+ EOF;
manydeclares: varde | funcde | procede;


////         small tokens        ////////

LB: '(' ;
RB: ')' ;
LQ: '[';
RQ: ']';
SEMI: ';' ;
CM: ',';
EQ: '=';
COL: ':';
DD: '..';
ADD: '+';
MUL: '*';
NOTEQ: '<>';
LESSTN: '<';
LESSEQ: '<=';
SUBNE: '-';
DIVSI: '/';
GRETN: '>';
GREEQ: '>=';
ASSI: ':=';
//DDD: SP DD SP;

BOOLLIT: TRUE|FALSE;
/////////  keywords         /////
BREAK: B R E A K;
CONTINUE: C O N T I N U E;
FOR: F O R;
TO: T O;
DOWNTO: D O W N T O;
DO: D O;
IF: I F;
THEN: T H E N;
ELSE: E L S E;
RETURN: R E T U R N;
WHILE: W H I L E;
BEGIN: B E G I N;
END: E N D;
FUNCTION: F U N C T I O N;
PROCEDURE: P R O C E D U R E;
VAR: V A R;
TRUE: T R U E;
FALSE: F A L S E;
ARRAY: A R R A Y;
OF: O F;
REAL: R E A L;
BOOLEAN: B O O L E A N;
INTEGER: I N T E G E R;
STRING: S T R I N G;
NOT: N O T;
AND: A N D;
OR: O R;
DIV: D I V;
MOD: M O D;
WITH: W I T H;
/*KEYWORD: BREAK|CONTINUE|FOR|TO|DOWNTO|DO|IF|THEN|ELSE|RETURN|WHILE|BEGIN|END
|FUNCTION|PROCEDURE|VAR|TRUE|FALSE|ARRAY|OF|REAL|BOOLEAN|INTEGER|STRING
|NOT|AND|OR|DIV|MOD;*/


///////    fragments         ////
fragment A:('a'|'A');
fragment B:('b'|'B');
fragment C:('c'|'C');
fragment D:('d'|'D');
fragment E:('e'|'E');
fragment F:('f'|'F');
fragment G:('g'|'G');
fragment H:('h'|'H');
fragment I:('i'|'I');
fragment J:('j'|'J');
fragment K:('k'|'K');
fragment L:('l'|'L');
fragment M:('m'|'M');
fragment N:('n'|'N');
fragment O:('o'|'O');
fragment P:('p'|'P');
fragment Q:('q'|'Q');
fragment R:('r'|'R');
fragment S:('s'|'S');
fragment T:('t'|'T');
fragment U:('u'|'U');
fragment V:('v'|'V');
fragment W:('w'|'W');
fragment X:('x'|'X');
fragment Y:('y'|'Y');
fragment Z:('z'|'Z');

fragment NUM: [0-9];

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


//////    bigger tokens      //////
ID: ('_'|[a-z]|[A-Z])([a-z]|[A-Z]|[0-9]|'_')*;
INTLIT: [0-9]+;
REALLIT: ([0-9]+ ('.')? [0-9]*([0-9]*[eE]'-'?[0-9]+)?)
				| ([0-9]* ('.')? [0-9]+([eE]'-'?[0-9]+)?);

STRINGLIT: '"'('\\'[bfrnt'"\\]|~[\b\n\f\r\t'"\\])*'"'{self.text = self.text[1:len(self.text) - 1]};

typee:  BOOLEAN | INTEGER | REAL | STRING | ARRAY;
primtype: BOOLEAN | INTEGER | REAL | STRING;


////////   array         //////////
arrtype: ARRAY LQ expression DD expression RQ OF primtype;
//numbers: numforarray;

////////   commnent      //////////
CMT: (BLKCMT | LINECMT) ->skip;
BLKCMT: TRACMT | BLCMT;
TRACMT: '(*'.*?'*)' ;
BLCMT: '{'.*?'}'  ;
LINECMT: '//'~[\r\n]* ;


////////   precedence    /////////
exp1: exp1 (AND THEN) exp2 | exp1 (OR ELSE) exp2
      | exp2;
exp2: exp3 EQ exp3 | exp3 NOTEQ exp3 |
       exp3 LESSTN exp3 | exp3 GRETN exp3 |
       exp3 GREEQ exp3 | exp3 LESSEQ exp3
			 | exp3;
exp3: exp3 ADD exp4 | exp3 SUBNE exp4
       | exp3 OR exp4 | exp4;
exp4: exp4 DIVSI exp5 | exp4 MUL exp5
       | exp4 MOD exp5 | exp4 AND exp5
			 | exp4 DIV exp5 | exp5;
exp5: NOT exp5| SUBNE exp5
       | exp6;
exp6:  LB exp1 RB
       | ID //(paralist)? ( LQ indexexpre RQ )?
       | INTLIT
       | BOOLLIT
       | REALLIT
       | STRINGLIT
       | indexexpre
       | invoexpre
			 ;


////////   declaration       ////////
varde: VAR (idlist COL vartype SEMI)+;   //WRONG
vartype: primtype | arrtype;
idlist: ID (CM ID)*;

funcde: funcde1 varde? compostate;
funcde1: FUNCTION ID paralist COL vartype SEMI;
paralist: LB parade? RB;
parade: idlist COL vartype (SEMI idlist COL vartype )*;   // WRONG

//parade: parade2|parade1;
//parade1: idlist COL vartype ;
//parade2: (idlist COL vartype SEMI)+ idlist COL vartype;
compostate: BEGIN statement* END;

procede: procede1 varde? compostate;
procede1: PROCEDURE ID paralist SEMI;


expression: indexexpre | invoexpre | exp1;

indexexpre: ID (LB expression? RB)? (LQ expression RQ)+
            | LB expression2? RB LQ expression2 RQ;  // foo(2)[3+x] := a[b[2]] +3;
expression2: expression (CM expression)*;


expindex: expi+;
expi: expi (ADD|SUBNE) expi1
			| expi1;
expi1: expi1 (DIVSI|MUL|MOD|DIV) expi2
			| expi2;
expi2: SUBNE expi2
			| expi3;
expi3: expi4 LQ expi4 RQ
			| expi4;
expi4: LB expi RB | ID | INTLIT | indexexpre|typee;

/*numforarray: indexexpre1+;
indexexpre1: indexexpre1 (ADD|SUBNE) expin1
			| expin1;
expin1: expin1 (DIVSI|MUL|MOD|DIV) expin2
			| expin2;
expin2: SUBNE expin2
			| expin3;
expin3: expin4 LQ expin4 RQ
			| expin4;
expin4: LB indexexpre1 RB | ID | INTLIT | indexexpre | indexexpre1;*/


invoexpre: ID LB exprlist? RB;
exprlist: expression (CM expression)*;

////////      statement       ////////////////

manystatements: statement+;
statement: semistatement | nomistatement;
semistatement: assignstate | breakstate | contstate | returnsate | callstate;
nomistatement: ifstate | forstate | whilestate | compostate | withstate;

//assignstate: (ID | indexexpre) ASSI (assignstate
//             | rhs);
//rhs: ID | indexexpre ASSI expression SEMI;
assignstate: (lhs ASSI)+ expression SEMI;
lhs: ID | indexexpre;


ifstate: IF exp1 THEN statement (ELSE statement)? ;

whilestate: WHILE exp1 DO stopstate* statement stopstate*;

forstate: FOR ID ASSI expression (TO|DOWNTO) expression DO stopstate* statement stopstate*;

breakstate: BREAK SEMI;

contstate: CONTINUE SEMI;

stopstate: breakstate | contstate;

returnsate: returnexp | returnnoexp;
returnexp: RETURN expression SEMI;
returnnoexp: RETURN SEMI;

parade2: parade SEMI;
withstate: WITH parade2 DO statement;

callstate: ID LB statelist? RB SEMI;
statelist: expression (CM expression)*;


UNCLOSE_STRING: '"' ('\\' ([tbfrn] | '\'' | '"' | '\\' )
    | ~('\b' | '\f' | '\r' | '\n' | '\t' | '\'' | '"' | '\\'))*
    {raise UncloseString(self.text[1:])}
    ;
ILLEGAL_ESCAPE: '"' (~[\\"'\n\t\r\f] | '\\' [ntfrb\\'"])* '\\' ~[ntrbf'"\\]
                    {raise IllegalEscape(self.text[1:])} ;
ERROR_CHAR: . {raise ErrorToken(self.text)};// {raise Erroroken(self.text)} .;

/*'"'(('\\'[bfrnt'"\\])|~[\n\f\r\t'"\\])*
								{
									raise UncloseString(self.text[1:len(self.text)])}
								;*/
/*ILLEGAL_ESCAPE1: '"'('\\'[bfrnt'"\\]|~[\b\n\f\r\t'"\\])*[\n\f\r\t'"\\]+
							.*?'"'
							{raise IllegalEscape(self.text[1:len(self.text) - 1])};
ILLEGAL_ESCAPE2: '"'('\\'[bfrnt'"\\]|~[\b\n\f\r\t'"\\])*[\n\f\r\t'"\\]+
							(~'"')*
							{raise IllegalEscape(self.text[1:len(self.text)])};*/
