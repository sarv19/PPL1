grammar MP;

@lexer::header {
from lexererr import *
}  //commnent out this

options{
	language=Python3; //=Java
	//language=Java;
}
program: manydeclares+ EOF;
manydeclares: varde | funcde | procede;

//          recognizer                   ///
/*program  : mptype 'main' LB RB LP body? RP EOF ;
mptype: INTTYPE  VOIDTYPE ;
body: funcall SEMI;
exp: funcall  INTLIT ;
funcall: ID LB exp? RB ;*/

////         small tokens        ////////

LB: '(' ;
RB: ')' ;
LP: '{';
RP: '}';
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
BOOLEAN: B O O L E A N | B O O L;
INTEGER: I N T E G E R | I N T;
STRING: S T R I N G;
NOT: N O T;
AND: A N D;
OR: O R;
DIV: D I V;
MOD: M O D;
MAIN: M A I N;
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
BOOLLIT: 'true'|'false';
STRINGLIT: '"'('\\'[bfrnt'"\\]|~[\b\n\f\r\t'"\\])*'"'{self.text = self.text[1:len(self.text) - 1]};
//fragment QUOTE: '"' -> skip;
//STRINGLIT:  QUOTE ('\\'[bfrnt'"\\]|~[\b\n\f\r\t'"\\])* QUOTE;
TYPE:  BOOLEAN | INTEGER | REAL | STRING | ARRAY;
primtype: BOOLEAN | INTEGER | REAL | STRING;
////////   array         //////////
arrtype: ARRAY LQ INTLIT DD INTLIT RQ OF primtype;


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
       exp3 GREEQ exp3 | exp3;
exp3: exp3 ADD exp4 | exp3 SUBNE exp4
       | exp3 OR exp4 | exp4;
exp4: exp4 DIVSI exp5 | exp4 MUL exp5
       | exp4 MOD exp5 | exp4 AND exp5
			 | exp4 DIV exp5 | exp5;
exp5: NOT exp5| SUBNE exp5
       | exp6;
exp6:  LB exp1 RB
       | ID
       | INTLIT
       | BOOLLIT
       | REALLIT
       | STRINGLIT;


////////   declaration       ////////
varde: VAR (idlist COL vartype SEMI)+;
vartype: primtype | arrtype;
idlist: ID (CM ID)*;

funcde: funcde1 varde? compostate;
funcde1: FUNCTION ID paralist COL vartype SEMI;
paralist: LB parade? RB;
parade: idlist COL vartype (SEMI idlist COL vartype )*;   // WRONG
compostate: BEGIN statelist? END;
statelist: INTLIT;

procede: procede1 varde? compostate;
procede1: PROCEDURE ID paralist SEMI;


expression: indexexpre | invoexpre | exp1;

indexexpre: ID (LB expression? RB)? LQ expindex RQ;

expindex: expi+;
expi: expi (ADD|SUBNE) expi1
			| expi1;
expi1: expi1 (DIVSI|MUL|MOD|DIV) expi2
			| expi2;
expi2: SUBNE expi2
			| expi3;
expi3: expi4 LQ expi4 RQ
			| expi4;
expi4: LB expi RB | ID | INTLIT | indexexpre;

invoexpre: ID LB exprlist* RB;
exprlist: expression (SEMI expression)*;

////////      statement       ////////////////

manystatements: statement+;
statement: semistatement;// | nomistatement;
semistatement: assignstate;// | breakstate | contstate | returnsate | callstate;
nomistatement: ifstate; //| forstate | whilestate | compostate | withstate;

assignstate: (ID | indexexpre) ASSI assignstate
             | rhs;
rhs: (ID | indexexpre) ASSI expression SEMI;

ifstate: IF exp2 THEN statement (ELSE statement)? ;

whilestate: WHILE exp2 DO statement;

forstate: FOR ID ASSI expression (TO|DOWNTO) expression DO statement;



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
