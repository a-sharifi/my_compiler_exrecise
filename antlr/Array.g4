// Define a grammar called Array
grammar Array;
type : simple | 
           ID | 
ARRAY OPENBRACKET simple CLOSEBRACKET  OF  type EOF;       // match keyword hello followed by an identifier

simple : INTEGER | CHAR | NUMBER DOTDOT NUMBER ;
OF :      'of'                         ;
OPENBRACKET :   '['                    ;
CLOSEBRACKET :  ']'                    ;
DIGIT    :         ('0' .. '9')        ;
NUMBER   :  MINUS ? DIGIT +            ;
MINUS    : '-'                         ;
DOTDOT   :              '..'           ;
ARRAY  : 'array';
INTEGER : 'integer' ; 
CHAR : 'char' ; 

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
ID : [a-z]+ ;             // match lower-case identifiers