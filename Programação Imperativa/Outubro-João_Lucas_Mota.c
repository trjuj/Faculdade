#include <stdio.h>
#include <time.h>

int main(){

    time_t t1, t2;
    double dif;

    time(&t1);
    printf("%s", strftime(t1));
    printf("Pressione enter para marcar o segundo tempo ");
    getchar();
    time(&t2);
    dif = difftime(t2,t1);
    printf("Diferenca: %.f segundos", dif);

    return 0;
}