#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int main(){

    int i, j, x, k, cp, cont, cont2=0, vidas=6;
    char aux [25], resp[25], letra[2], *p;
    
    char estados [27][25] = {{"RIO GRANDE DO SUL"},
                             {"SANTA CATARINA"},
                             {"PARANA"},
                             {"SAO PAULO"},
                             {"MINAS GERAIS"},
                             {"RIO DE JANEIRO"},
                             {"ESPIRITO SANTO"},
                             {"BAHIA"},
                             {"GOIAS"},
                             {"TOCANTINS"},
                             {"MARANHAO"},
                             {"CEARA"},
                             {"PARAIBA"},
                             {"RIO GRANDE DO NORTE"},
                             {"ALAGOAS"},
                             {"SERGIPE"},
                             {"PIAUI"},
                             {"AMAZONAS"},
                             {"RONDONIA"},
                             {"RORAIMA"},
                             {"PARA"},
                             {"DESTRITO FEDERAL"},
                             {"MATO GROSSO"},
                             {"MATO GROSSO DO SUL"},
                             {"ACRE"},
                             {"PERNAMBUCO"},
                             {"AMAPA"}
                             };

    srand(time(NULL));
    x = rand()%27;

    printf("----- JOGO DA FORCA -----\nTema: Estado do Brasil\n\n");
    for(i=0; i<strlen(estados[x]); i++){
        if(estados[x][i] != '\0'){
            if(estados[x][i] != ' '){
                printf("_");
                resp[i] = '_';
            }else{
                printf(" ");
                resp[i] = ' ';
            }
        }
    }
    do{
        printf("\n\nVidas atuais: %d\nEscolha uma letra: ", vidas);
        scanf("%s", &letra[0]);
        strupr(letra);
        p = &estados[x][0];
        for (j=0; j<strlen(estados[x]); j++){
            if(estados[x][j]!=' '){
                if(letra[0] == *p){
                    resp[j] = *p;
                    p++;
                    if(letra[0]!=estados[x][j]){
                        cont2++;
                    }
                }else{
                    p++;
                }
            }else{
                p++;
            }
        }
        if(cont2==(strlen(estados[x]))){
            vidas--;
            printf("\nErrado! -1 Vida\nVidas atuais: %d\n", vidas);
            cont2 = 0;
        }
        printf("\n%s\n", resp);
        cont = strlen(estados[x]);
        for(k=0; k<strlen(estados[x]); k++){
            if(resp[k]!='_'){
                cont--;
            }
        }
        if (cont==0){
            cp = 1;
        }else{
            cp = 0;
        }
    }while((cp == 0)&&(vidas>0));
    if(cp == 1){
        printf("\n---- Parabens, resposta encontrada! ----");
    }
    if(vidas<=0){
        printf("\n\nGame Over");
    }
    return 0;
}