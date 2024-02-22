#include <stdio.h>

int main(){

    int x, r, i, j, aux, cont = 0;
    char n[18];

    printf("Digite o numero a ser traduzido: ");
    scanf("%d", &x);
    printf("%d em binario: ", x);

    do{
        r = x%2;
        x = x/2;
        n[cont] = r;
        cont++;
    }while(x>0);

    x--;
    cont--;

    for (i=cont; i>-1; i--){
        if(x == 1){
            printf("%d", x);
        }else{
            printf("%d ", n[cont]);
            cont--;
        }
    }
    return 0;
}