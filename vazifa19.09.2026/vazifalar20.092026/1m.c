#include <stdio.h>

int kvadrat(int son) {
    return son * son;
}

int main() {
    int son;
    scanf("%d", &son);

    printf("%d\n", kvadrat(son));

    return 0;
}