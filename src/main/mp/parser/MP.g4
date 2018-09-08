grammar MP;

@lexer::header {
from lexererr import *
}  //commnent out this

options{
	language=Python3; //=Java
	//language=Java;
}

//          recognizer                   ///
program  : mptype 'main' LB RB LP body? RP EOF ;
mptype: INTTYPE  VOIDTYPE ;
body: funcall SEMI;
exp: funcall  INTLIT ;
funcall: ID LB exp? RB ;

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
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

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
FUNCTION: F U C N T I O N;
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

//////    bigger tokens      //////
ID: ('_'|[a-z]|[A-Z])([a-z]|[A-Z]|[0-9]|'_')*;
INTLIT: [0-9]+;
REALLIT: ([0-9]+ ('.')? [0-9]*([0-9]+[eE]'-'?[0-9]+)?)
				| ([0-9]* ('.')? [0-9]+([eE]'-'?[0-9]+)?);
/*KEYWORD: 'break'|'continue'|'for'|'to'|'downto'|'do'|'if'|'then'|'else'|'return'|'while'|'begin'|'end'
|'function'|'procedure'|'var'|'true'|'false'|'array'|'of'|'real'|'boolean'|'integer'|'string
|'not'|'and'|'or'|'div'|'mod'; */
BOOLLIT: 'true'|'false';

ERROR_CHAR: .;  //{raise Erroroken(self.text)}
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
