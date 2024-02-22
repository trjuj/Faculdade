#include <stdio.h>

int main () {

    int x, d = 310;
    float x1;

    x = d%90;
    x1 = (x/90.0)*60.0;

    printf("X: %d\n", x);
    printf("X1: %f", x1);

    return 0;
}