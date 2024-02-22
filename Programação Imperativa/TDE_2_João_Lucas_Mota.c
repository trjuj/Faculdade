// João Lucas Mota Nogueira da Costa
#include <stdio.h>
#include <conio.h>
#include <time.h>
#include <stdlib.h>

// O programa serve para aleatorizar um entre varios jogos dispostos, para quando não consegue decidir o que jogar
enum jogos {Minecraft = 1, Call_of_Duty, Inscryption, Dark_Souls_III, Terraria, Subanutica, Gunfire_Reborn,
Aragami};
// Aqui e usado o comando enum para atribuir um valor numerico para cada um dos jogos na lista

int main(){
    
    int x;
// Aqui é feita uma lista apenas para poder imprimir os nomes dos jogos como strings
    char lista[8][15] = {{"Minecraft"}, {"Call of Duty"}, {"Inscryption"}, {"Dark Souls III"}, {"Terraria"}, {"Subanutica"}, {"Gunfire Reborn"},
    {"Aragami"}};
// Comando de aleatorizacao baseada no tempo do sistema
    srand(time(NULL));
    x = rand()%8;

    printf("Tecle enter para aleatorizar o jogo\n\n");
    getch();

    printf("O numero e o jogo sorteado foram: ");
// Todos os casos de jogos possiveis em cases (normalmente divididos em numeros)
    switch(x){

        case(Minecraft):
        printf("%d - %s", x, lista[x]);
        break;

        case(Call_of_Duty):
        printf("%d - %s", x, lista[x]);
        break;

        case(Inscryption):
        printf("%d - %s", x, lista[x]);
        break;

        case(Dark_Souls_III):
        printf("%d - %s", x, lista[x]);
        break;

        case(Terraria):
        printf("%d - %s", x, lista[x]);
        break;

        case(Subanutica):
        printf("%d - %s", x, lista[x]);
        break;

        case(Gunfire_Reborn):
        printf("%d - %s", x, lista[x]);
        break;

        case(Aragami):
        printf("%d - %s", x, lista[x]);
        break;
    }

    return 0;
}

''' o enum possibilita usar palavras inteiras com valores numericos, como se fossem variaveis, isso pode auxiliar 
    em algum algoritmo que necessite de um numero grande de variaveis para seu funcionamento '''