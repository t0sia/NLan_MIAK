grammar nlan;

SPACE: [ \t\r\n] -> skip;
PLUS: 'dodac';
MINUS: 'odjac';
MULTIPLICATION: 'razy';
DIVIDE: 'podzielicPrzez';
POWER: 'doPotegi';

program: 'start' COMA (var_decl | arr_decl | math | print_var_exp | print_text_exp | loop_exp)* 'zakoncz';
math_sym: PLUS | MINUS | MULTIPLICATION | DIVIDE | POWER;

COMA: ',';

EQ: 'rownaSie';
DOUBLEEQ: 'jestRowne';
LESS: 'jestMniejsze';
LESSEQ: 'jestMniejszeLubRowne';
GREATER: 'jestWieksze';
GREATEREQ: 'jestWiekszeLubRowne';

compare_sym: DOUBLEEQ | LESS | LESSEQ | GREATER | GREATEREQ;

IF: 'jezeli';
FOREACH: 'dlaKazdegoElementu';
FORELEMENT: 'dlaKazdejWartosci';
FORRANGE: 'ZZakresu';
WHILE: 'dopoki';
PRINT_VAR: 'wypiszZmienna';
PRINT_TEXT: 'wypiszTekst';
VALUE: 'oWartosci';
END_LOOP: 'koniecPetli';
LEFT_BR: '[';
RIGHT_BR: ']';
OPEN: '(';
CLOSE: ')';
ARRAYAND: '&';
STARTLOOP: ':';
ARRAY: 'nalezacegoDo';

ID: [a-zA-Z][a-zA-Z0-9]*;
STRING: '"'[a-zA-Z]+'"';
NUMBER: [0-9]+;

var_decl: 'stworzZmienna' ID VALUE (STRING | NUMBER) COMA;

arr_decl: 'stworzTablice' ID VALUE LEFT_BR (STRING | NUMBER | ID) (ARRAYAND (STRING | NUMBER | ID))* RIGHT_BR COMA;

math: ID EQ (NUMBER | ID) math_sym (NUMBER | ID) (math_sym (NUMBER | ID))* COMA;

loop_exp: IF (ID | NUMBER) compare_sym (ID | NUMBER) STARTLOOP (var_decl | arr_decl | math | print_var_exp | print_text_exp)* END_LOOP COMA |
          WHILE (ID | NUMBER) compare_sym (ID| NUMBER) STARTLOOP (var_decl | arr_decl | math | print_var_exp | print_text_exp)* END_LOOP COMA |
          FOREACH ID ARRAY ID STARTLOOP (var_decl | arr_decl | math | print_var_exp | print_text_exp)* END_LOOP COMA |
          FORELEMENT ID FORRANGE OPEN NUMBER COMA NUMBER CLOSE STARTLOOP (var_decl | arr_decl | math | print_var_exp | print_text_exp)* END_LOOP COMA;

print_var_exp: PRINT_VAR OPEN ID CLOSE COMA;

print_text_exp: PRINT_TEXT OPEN STRING CLOSE COMA;

