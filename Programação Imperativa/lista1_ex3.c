#include <stdio.h>

int main () {
    int a, b, soma, con;
    float media;
    printf("Digite um numero inteiro: ");
    scanf("%d",&a);
    con = 1;
    soma = a;
    while(con<3){
        printf("Digite um numero inteiro: ");
        scanf("%d",&b);
        if (a < b) {
            con++;
            soma += b;
        } else { 
            con = 1;
            soma = b;
        }
        a = b;
    }
    media = (float)soma / 3;
    printf("Soma: %d\n", soma);
    printf("Media:  %.2f\n", media);

    return 0;
}