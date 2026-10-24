#include <stdio.h>

void ikkiBarobar(int *son) {
    *son = *son * 2;
}

int main() {
    int son;
    scanf("%d", &son);

    ikkiBarobar(&son);

    printf("%d\n", son);

    return 0;
}