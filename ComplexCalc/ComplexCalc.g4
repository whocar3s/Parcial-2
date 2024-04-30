grammar ComplexCalc;

prog: stat+;

stat: expr NEWLINE                #print
    | ID '=' expr NEWLINE         #assign
    | NEWLINE                     #blank
    ;

expr: expr op=(' * ' |' / ') expr      #MulDiv
    | expr op=(' + ' | ' - ') expr      #AddSub
    | INT                         #int
    | COMPLEX                     #complex
    | ID                          #id
    | FLOAT                       #float
    | '(' expr ')'                #parens
    | '-' expr                    #Negativo
    | '+' expr                    #Positivo
    ;
    
COMPLEX:  [0-9]+ 'i';
    
// Lexer rules
MUL        :  ' * ';
ADD        :  ' + ';
DIV        :  ' / ';
SUB        :  ' - ';
ID         :  [a-zA-Z]+;
INT        :  ('-' | '+')? [0-9]+;
FLOAT      :  ('-' | '+')? [0-9]+ '.' [0-9]+;
NEWLINE    :  '\r'?'\n';
WS         :  [ \t\r\n]+ -> skip;

