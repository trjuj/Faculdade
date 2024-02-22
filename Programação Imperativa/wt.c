#include <stdio.h>
#include <math.h>

int main(){

    float xt, Mm, a, Cm;

    do{
        printf("Insira a quantidade de torres: ");
        scanf("%f", &xt);

        if (xt != 0){
            a = pow(xt,0.6);
            Mm = (4+a+15*log(1+(xt+90)/15));
            Cm = 10 + 0.6*Mm;

            printf("Magia maxima: %f", Mm);
            printf("\nCusto da magia: %f\n", Cm);
        }else{
            printf("Adeus");
        }
    }while (xt != 0);
    
    return 0;
}