grammar MP;

@lexer::header {
from lexererr import *
}  //commnent out this

options{
	language=Python3; //=Java
	//language=Java;
}
program: manydeclares;
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
SP: ' ';
ASSI: ':=';



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
/*KEYWORD: BREAK|CONTINUE|FOR|TO|DOWNTO|DO|IF|THEN|ELSE|RETURN|WHILE|BEGIN|END
|FUNCTION|PROCEDURE|VAR|TRUE|FALSE|ARRAY|OF|REAL|BOOLEAN|INTEGER|STRING
|NOT|AND|OR|DIV|MOD;*/
ANDTHEN: AND SP THEN;
ORELSE: OR SP ELSE;
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
ManyNum: NUM+;


//////    bigger tokens      //////
ID: ('_'|[a-z]|[A-Z])([a-z]|[A-Z]|[0-9]|'_')*;
INTLIT: [0-9]+;
REALLIT: ([0-9]+ ('.')? [0-9]*([0-9]+[eE]'-'?[0-9]+)?)
				| ([0-9]* ('.')? [0-9]+([eE]'-'?[0-9]+)?);
BOOLLIT: 'true'|'false';
STRINGLIT: '"'('\\'[bfrnt'"\\]|~[\b\n\f\r\t'"\\])*'"'{self.text = self.text[1:len(self.text) - 1]};
//fragment QUOTE: '"' -> skip;
//STRINGLIT:  QUOTE ('\\'[bfrnt'"\\]|~[\b\n\f\r\t'"\\])* QUOTE;
TYPE:  BOOLEAN | INTEGER | REAL | STRING | ARRAY;
primtype: BOOLEAN | INTEGER | REAL | STRING;

////////   array         //////////
arrtype: ARRAY SP? LQ ManyNum SP DD SP ManyNum RQ SP* OF SP+ primtype;


////////   commnent      //////////
CMT: (BLKCMT | LINECMT) ->skip;
BLKCMT: TRACMT | BLCMT;
TRACMT: '(*'.*?'*)' ;
BLCMT: '{'.*?'}'  ;
LINECMT: '//'~[\r\n]* ;


////////   precedence    /////////
/*expr1: (expr2(ANDTHEN|ORELSE))*expr2;
expr2: (expr3(EQ|NOTEQ|LESSTN|LESSEQ|GREEQ|GRETN)expr3)+;
expr3: (expr4(ADD|SUBNE|OR))*expr4;
expr4: (expr5(DIVSI|MOD|AND))*expr5;
expr5: (SUBNE|NOT)*expr6;
expr6: LB expr7 RB;
expr7: ID | ManyNum;*/
expr: 	    LB expr RB
			|	<assoc=right> (NOT | SUBNE) expr
			| expr SP* (DIVSI|MUL|(SP+MOD SP+)) SP* expr
			|	expr SP* (ADD|SUBNE|(SP+ OR SP+)) SP* expr
			| expr SP* (EQ|NOTEQ|LESSTN|LESSEQ|GREEQ|GRETN) SP* expr
			| expr  (SP+ ANDTHEN|ORELSE SP+) expr
			| ID
			| ManyNum
			;
//expr1: expr1 (EQ|NOTEQ|LESSEQ|LESSTN|GREEQ|GRETN) expr1;
////////   declaration       ////////
varde: VAR SP+ (idlist SP* COL SP* vartype SP* SEMI)+;
vartype: primtype | arrtype;
idlist: ID (CM ID)*;

funcde: funcde1 varde? compostate;
funcde1: FUNCTION SP+ ID SP* paralist SP* COL SP* vartype SP* SEMI;
paralist: LB SP* parade SP* RB;
parade: ((idlist SP* COL SP* vartype) (SEMI SP* idlist SP* COL SP* vartype)*)*;   // WRONG
compostate: BEGIN SP* statelist? SP* END;
statelist: ManyNum;

procede: procede1 varde? compostate;
procede1: PROCEDURE SP+ ID SP* paralist SP* SEMI;



UNCLOSE_STRING:'"'(('\\'[bfrnt'"\\])|~[\n\f\r\t'"\\])*
								{
									raise UncloseString(self.text[1:len(self.text)])}
								;
ILLEGAL_ESCAPE1: '"'('\\'[bfrnt'"\\]|~[\b\n\f\r\t'"\\])*[\n\f\r\t'"\\]+
							.*?'"'
							{raise IllegalEscape(self.text[1:len(self.text) - 1])};
ILLEGAL_ESCAPE2: '"'('\\'[bfrnt'"\\]|~[\b\n\f\r\t'"\\])*[\n\f\r\t'"\\]+
							(~'"')*
							{raise IllegalEscape(self.text[1:len(self.text)])};
ERROR_CHAR: .;// {raise Erroroken(self.text)} .;
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
