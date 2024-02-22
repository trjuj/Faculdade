#include <stdio.h>  

int x;

int menu(){
    do{
        printf("\n--- Cinemasso ---\n");
        printf("\nEscolha uma das opcoes:\n");
        printf("0 - Sair\n");
        printf("1 - Vender ingresso\n");
        printf("2 - Mostrar plateia\n");
        printf("3 - Mostrar ocupacao\n");
        printf("\nQual a sua opcao: ");
        scanf("%d",&x);
        if ((x<0) || (x>3)){
            printf("Opcao invalida!");
        }
    }while((x<0) || (x>3));
    return x;
}

int main () {
    char plateia[14][10];
    int i, j;
    char *p;

    for (i=0; i<14; i++) {
        for (j=0; j<10; j++) {
            plateia[i][j] = '-'; // livre
        }
    }
    p = &plateia[0][0];

    menu();

    while(x != 0){
        if (x==2){
            printf("\n--- Situacao da plateia ---\n\n");
            printf("%c  ", plateia[p[i]][p[j]]);
            menu();
        }
        if (x==3){
            printf("\n--- Relatorio de ocupacao ---\n\n");
            for (i=0; i<14; i++) {
                for (j=0; j<10; j++) {
                    printf("%c  ", plateia[i][j]);
                }
                printf("\n");
            }
            menu();
        }
    }
    printf("Obrigado por usar o programa!");
    return 0;  
}