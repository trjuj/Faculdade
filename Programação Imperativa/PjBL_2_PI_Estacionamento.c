#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

typedef struct{
    char nomeDono[50];
    char telefoneDono[20];
    char CPFDono[15];
    char placa[10];
    time_t entrada;
    time_t saida;
} zCar;

typedef struct{
    char CNPJ[20];
    char nome[50];
    zCar vagas[100];
    int vag;
} zEst;

void Ocupa(zEst est, int x){

    int i;

    if (x == 0){
        printf("Que beleza! O estacionamento ta vazio!\n\n");
    }
    if (x == 100){
        printf("Oxi, o estacionamento ta cheio...\n\n");
    }
    if ((x != 0)&&(x != 100)){
        for (i=0; i < x; i++) {
        printf("Numero da Vaga: %d\n", i+1);
        printf("Placa: %s\n", est.vagas[i].placa);
        printf("Dono: %s\n", est.vagas[i].nomeDono);
        printf("-------------------------------------------------------------\n");
        }
    }
}

void Entra(zEst est, int x){

    char p1, p2, p3, c1;
    time_t t1;

    printf("Insira seu nome: ");
    scanf("%s", &p1);
    printf("Telefone para contato: ");
    scanf("%s", &p2);
    printf("CPF: ");
    scanf("%s", &p3);
    printf("Placa do carro: ");
    scanf("%s", &c1);
    time(&t1);

    zCar Car1 = {p1, p2, p3, c1, t1, '-'};
    est.vagas[x] = Car1;

    printf("Sua vaga esta garantida!\n");
    printf("-------------------------------------------------------------\n");
}

int main(){

    int op;

    zEst sim = {"65.121.757/0001-89", "Garotos de Programa", {}, 0};

    printf("-------------------------------------------------------------\n");
    printf("Alo, bom dia! Bem vindo ao estacionamento Garotos de Programa!\n\nEscolha sua opcao:\n\n1 - Mostrar ocupacao\n2 - Entrada de veiculo\n3 - Saida de veiculo\n4 - Cancela\n\n");
    
    do{
        printf("Opcao: ");
        scanf("%d", &op);
        printf("-------------------------------------------------------------\n");

        if (op == 1){
            Ocupa(sim, sim.vag);
            
        }

        if (op == 2){
            Entra(sim, sim.vag);
            sim.vag++;
        }

        if (op == 3){

        }

        if (op == 4){
            printf("Tenha um bom dia!\n");
        }

        if ((op != 1)&&(op != 2)&&(op != 3)&&(op != 4)){
            printf("Opcao invalida! Tente novamente!");
        }

    }while((op == 1)||(op == 2)||(op == 3));

    return 0;
}