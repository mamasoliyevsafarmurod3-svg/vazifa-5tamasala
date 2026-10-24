#include <stdio.h>

int main() {
    char soz[100];
    scanf("%s", soz);

    int soni = 0;
    while (soz[soni] != '\0') {
        soni++;
    }

    printf("%d\n", soni);

    return 0;
}