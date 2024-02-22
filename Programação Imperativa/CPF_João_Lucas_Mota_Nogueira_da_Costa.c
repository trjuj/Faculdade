#include <stdio.h>
#include <string.h>

int main(){

    int soma1 = 0, soma2 = 0, i, x1, x2, k1 = 10, k2 = 11;
    char cpf[20], dig[2], *p, asctr = 45, ascpnt = 46;

    printf("Digite o CPF (xxx.xxx.xxx-xx): ");
    scanf("%s", &cpf);

    p = &cpf[0];

    for (i=0; i < strlen(cpf)-2; i++){
        if ((*p != asctr)&&(*p != ascpnt)){
            soma1 = soma1 + ((cpf[i] - 48)*k1);
            k1--;
            p++;
        }else{
            p++;
        }
    }
    x1 = soma1%11;
    if (x1<2){
        dig[0] = 0;
    }else{
        dig[0] = 11 - x1;
    }

    p = &cpf[0];

    for (i=0; i < strlen(cpf)-1; i++){
        if ((*p != asctr)&&(*p != ascpnt)){
            soma2 = soma2 + ((cpf[i] - 48)*k2);
            k2--;
            p++;
        }else{
            p++;
        }
    }
    x2 = soma2%11;
    if (x2<2){
        dig[1] = 0;
    }else{
        dig[1] = 11 - x2;
    }

    printf("Soma 1: %d\n", soma1);
    printf("Soma 2: %d\n", soma2);
    printf("Resto 1: %d\n", x1);
    printf("Resto 2: %d\n", x2);
    printf("Digitos verificadores: %d e %d\n", dig[0], dig[1]);

    if(((cpf[12]-48)==dig[0])&&((cpf[13]-48)==dig[1])){
        printf("O CPF digitado e valido.");
    }else{
        printf("O CPF digitado e invalido.");
    }
    return 0;
}