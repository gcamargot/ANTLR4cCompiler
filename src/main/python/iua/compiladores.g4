grammar compiladores;

fragment LETRA : [A-Za-z] ;
fragment DIGITO : [0-9] ;
PUNTOYCOMA : ';';
COMA : ',';
PUNTO : '.';
LLAVEABRE : '{';
LLAVECIERRA : '}';
CORCHETEABRE : '[';
CORCHETECIERRA : ']';
PARENTESISCIERRA : ')';
PARENTESISABRE : '(';
MAS: '+';
MENOS: '-';
PRODUCTO: '*';
DIVISION: '/';
MODULO : '%';
ASIGNACION : '=';
MENOR : '<';
MENORIGUAL : '<=';
MAYOR : '>';
MAYORIGUAL : '>=';
IGUAL: '==';
DISTINTO : '!=';
NOT : '!';
AND : '&&';
OR : '||';
IF : 'if';
FOR : 'for';
WHILE : 'while';
DO : 'do';
INT : 'int';
FLOAT : 'float';
FLOTANTES : DIGITO PUNTO DIGITO;
FLOTANTESNEGATIVOS : '-' DIGITO PUNTO DIGITO;
HEXADECIMALES : '0''x' ([a-f]|[A-Z]|DIGITO)+;
NUMERO : DIGITO+ ;
ID : (LETRA | '_')(LETRA | DIGITO | '_')* ;

WS : [ \t\n\r] -> skip;
OTRO : . ;


//Verifico que todos los parentesis se abran y se cierren fragment
//Arbol sintactico descendente

program : instructions EOF || PUNTOYCOMA;

instructions : instruction instructions
              |
              ;

instruction : doWhileInstruction
            | whileInstruction
            | ifInstruction
            | forInstruction
            | asignation
            | comparison
            | instructionBlock
            | operation
            ;

doWhileInstruction : DO instructionBlock WHILE PARENTESISABRE instruction PARENTESISCIERRA PUNTOYCOMA
                    ;

whileInstruction : WHILE PARENTESISABRE instruction PARENTESISCIERRA instruction 
                  ;

ifInstruction : IF PARENTESISABRE comparison PARENTESISCIERRA instruction
                ;

forInstruction : FOR PARENTESISABRE instruction PUNTOYCOMA instruction PUNTOYCOMA instruction PARENTESISCIERRA instructionBlock
                ;

dataType :  INT
          | FLOAT
          ;

instructionBlock : LLAVEABRE instructions LLAVECIERRA;

comparison :  ID compare ID
            | ID compare NUMERO
            | NUMERO compare NUMERO
            | NUMERO compare ID
            ;

compare :   MENOR
              | MAYOR
              | IGUAL
              | DISTINTO
              ;

//2+2&&4*0

itop :  operation itop
        |
        ;

operation : expression ;

expression : lor logicOr ;

logicOr : land logicAnd;

lor:OR logicOr lor
    |
    ;

logicAnd: term t;

land :  AND land logicAnd
        |
        ;

term : f factor ;

t : MAS term t
   | MENOS term t
   |
  ;

factor : ID
       | NUMERO
       | PARENTESISABRE expression PARENTESISCIERRA
       ;

f : PRODUCTO factor f
   | DIVISION factor f
   |
  ;

asignation: tipo ID ASIGNACION itop;

tipo: INT | FLOAT;