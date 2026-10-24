#include <stdio.h>

void chiqar(int n) {
    if (n == 0) {
        return;
    }
    chiqar(n - 1);
    printf("%d ", n);
}

int main() {
    int n;
    scanf("%d", &n);

    chiqar(n);
    printf("\n");

    return 0;
}