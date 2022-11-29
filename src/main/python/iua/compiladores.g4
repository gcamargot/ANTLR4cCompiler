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
SUMARUNO: '++';
MENOS: '-';
RESTARUNO: '--';
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
ELSE : 'else';
FOR : 'for';
WHILE : 'while';
DO : 'do';
INT : 'int';
FLOAT : 'float';
RETURN: 'return';
FLOTANTES : DIGITO PUNTO DIGITO;
FLOTANTESNEGATIVOS : '-' DIGITO PUNTO DIGITO;
HEXADECIMALES : '0''x' ([a-f]|[A-Z]|DIGITO)+;
NUMERO : DIGITO+ ;
ID : (LETRA | '_')(LETRA | DIGITO | '_')* ;


WS : [ \t\n\r] -> skip;
OTRO : . ;


//Verifico que todos los parentesis se abran y se cierren fragment
//Arbol sintactico descendente

program : instructions EOF | PUNTOYCOMA;

instructions : instruction instructions
              | instruction PUNTOYCOMA
              | returnInstruction
              | 
              ;

instruction : doWhileInstruction
            
            | whileInstruction
            | ifInstruction
            | forInstruction
            | declaration
            | asignation
            | asignationF
            | comparison
            | operation
            | instructionBlock
            
            
            ;

returnInstruction: RETURN instructions;

doWhileInstruction : DO instructionBlock WHILE PARENTESISABRE instruction PARENTESISCIERRA
                    ;

whileInstruction : WHILE PARENTESISABRE instruction PARENTESISCIERRA instruction
                  ;

ifInstruction : IF PARENTESISABRE comparison PARENTESISCIERRA instructionIf elseInstruction
                
                ;

instructionIf : instruction;

elseInstruction : ELSE instruction 
                  |  
                  ;


forInstruction : FOR PARENTESISABRE instruction instruction PUNTOYCOMA instruction PARENTESISCIERRA instructionBlock
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

operation : expression 
            | incremento
            | decremento;

expression : lor logicOr ;

logicOr : land logicAnd;

lor:OR logicOr lor
    |
    ;

logicAnd: term t;

land :  AND land logicAnd
        |
        ;

term : factor f ;

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


declaration: tipo declarationM PUNTOYCOMA | tipo declaracionF ;

declaracionF: ID PARENTESISABRE parameters PARENTESISCIERRA instructionBlock;

declarationM : ID 
             | ID COMA declarationM 
             | init 
             | init COMA declarationM;

asignation: ID ASIGNACION itop PUNTOYCOMA;
asignationF: ID ASIGNACION ID PARENTESISABRE parametrosF PARENTESISCIERRA PUNTOYCOMA;

parametrosF: ID COMA parametrosF
            | NUMERO COMA parametrosF
            | ID | NUMERO
            ;

parameter: tipo ID ;

parameters: parameter  COMA parameters 
          | parameter 
          | ;

init: ID ASIGNACION itop;

tipo: INT | FLOAT;

incremento: ID SUMARUNO;

decremento: ID RESTARUNO;