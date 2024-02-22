#include <stdio.h>
typedef struct {
    int x;
    int y;
} sPonto;

typedef struct {
    sPonto pInicial;
    sPonto pFinal;
} sLinha;

sPonto lePonto();
void leLinha(sLinha *);

int main (){
    sLinha linha;
    leLinha (&linha);
    printf("Linha vai de (%d,%d) ate (%d,%d)", linha.pInicial.x, linha.pInicial.y, linha.pFinal.x, linha.pFinal.y);
    return 0;
}

void leLinha(sLinha *lin) {
    printf ("Ponto inicial: \n");
    lin->pInicial = lePonto();
    printf ("Ponto final: \n");
    lin->pFinal = lePonto();
}

sPonto lePonto() {
    sPonto p;
    printf ("x: ");
    scanf ("%d", &p.x);
    printf ("y: ");
    scanf ("%d", &p.y);
    return p;
}