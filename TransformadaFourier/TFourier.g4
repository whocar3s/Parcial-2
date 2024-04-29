grammar TFourier;

//grammar
prog: stat+;

stat: expr NEWLINE                #print
    | ID '=' expr NEWLINE         #assign
    | NEWLINE                     #blank
    ;

expr: '(' expr ')'                   #parens
    | expr op=(' * ' |' / ') expr  # MulDiv
    | expr op=(' + '|' - ') expr  # AddSub
    | INT                            #int
    | FLOAT                          #float
    | 'pi'                           #pi
    | SIN '(' expr ')'               #Sin
    | COS '(' expr ')'               #Cos
    | TAN '(' expr ')'               #Tan
    | F '(' arglist ')'              # FourierTransform
    | BOOLEAN                        #Boolean
    | BOOL_NEG expr                  #BoolNegacion
    | ID                             #id
    | expr '++'                      #Incremento
    | expr '--'                      #Decremento
    | '-' expr                       #Negativo
    | '+' expr                       #Positivo
    | ',' expr                         #lista
    ;


MUL    :  ' * ';
ADD    :  ' + ';
DIV    :  ' / ';
SUB    :  ' - ';
BOOLEAN : 'true' | 'false';
SIN: 'Sin';
COS: 'Cos';
TAN: 'Tan';
F: 'F';
BOOL_NEG : '!';
ID     :  [a-zA-Z]+;
INT    :  ('-' | '+')? [0-9]+;
FLOAT  :  ('-' | '+')? [0-9]+ '.'[0-9]+;
NEWLINE:  '\r'?'\n';
WS     :  [\t]+ -> skip;
arglist: expr (',' expr)*;