#include <stdio.h>

int main(){

    int i, j, cont = 0, a, b, d, th;
    float tm;
    int distancias[5][5];

    for (i=0; i < 5; i++){
        for (j=0; j < 5; j++){
            if (i == j){
                distancias[i][j] = 0;
            }
        }
    }

    distancias[0][1] = distancias [1][0] = 310;
    distancias[0][2] = distancias [2][0] = 716;
    distancias[0][3] = distancias [3][0] = 408;
    distancias[0][4] = distancias [4][0] = 852;
    distancias[1][2] = distancias [2][1] = 470;
    distancias[1][3] = distancias [3][1] = 705;
    distancias[1][4] = distancias [4][1] = 1144;
    distancias[2][3] = distancias [3][2] = 1119;
    distancias[2][4] = distancias [4][2] = 1553;
    distancias[3][4] = distancias [4][3] = 429;

    printf("--------------------------------\nMatriz:\n\n");

    for (i=0; i<5; i++){
        for (j=0; j<5; j++){
            printf("%d ", distancias[i][j]);
            cont++;
            if (cont >= 5){
                printf("\n");
                cont = 0;
            }
        }
    }

    do{
        printf("--------------------------------");
        printf("\nCidades:\n(1) Curitiba\n(2) Florianopolis\n(3) Porto Alegre\n(4) Sao Paulo\n(5) Rio de Janeiro\n");
        printf("--------------------------------");
        printf("\nEscolha a cidade A: ");
        scanf("%d", &a);
        printf("\nEscolha a cidade B: ");
        scanf("%d", &b);
        a--; b--;
        d = distancias[a][b];

        if ((a > 5)||(b > 5)||(a < 0)||(b < 0)){
            printf("Alguma das opcoes é invalida.");
        }else{
            if ( a == b){
                printf("\nOpcoes iguais detectadas! Distancia = 0 km");
            }else{
            printf("\nDistancia entre as cidades A e B: %d km\n", d);
            th = d/90;
            tm = ((d%90)/90.0)*60.0;
            printf("Tempo do percurso (Media de 90 km/h): %d hrs e %.0f min\n", th, tm);
            }
        }

    }while(distancias[a][b] != 0);
    return 0;
}