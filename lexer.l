%{
#include <stdio.h>
#include <string.h>
%}

/* Evita usar la librería yywrap */
%option noyywrap

/* Reglas Léxicas */
%%
"if"|"else"|"while"|"int"|"return"   { printf("PALABRA_RESERVADA|%s\n", yytext); }
[a-zA-Z_][a-zA-Z0-9_]* { printf("IDENTIFICADOR|%s\n", yytext); }
[0-9]+(\.[0-9]+)?                    { printf("NUMERO|%s\n", yytext); }
"+"|"-"|"*"|"/"|"="|"<"|">"          { printf("OPERADOR|%s\n", yytext); }
"{"|"}"|"("|")"|";"                  { printf("SIMBOLO|%s\n", yytext); }
[ \t\n\r]+                           { /* Ignorar espacios y saltos de línea */ }
.                                    { printf("ERROR_LEXICO|%s\n", yytext); }
%%

int main(int argc, char **argv) {
    if (argc > 1) {
        // Lee el archivo pasado por parámetro
        yyin = fopen(argv[1], "r");
        if(!yyin) {
            printf("ERROR|No se pudo abrir el archivo\n");
            return 1;
        }
    }
    yylex();
    return 0;
}