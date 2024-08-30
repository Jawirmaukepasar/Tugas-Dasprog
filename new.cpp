#include <stdio.h>

int main() {
    int A, T;
    double luas;

    scanf("%d %d", &A, &T);

    luas = (A * T) / 2.0;

    printf("%.2f\n", luas);

    return 0;
}