#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    int massiv[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &massiv[i]);
    }

    int eng_katta = massiv[0];
    for (int i = 1; i < n; i++) {
        if (massiv[i] > eng_katta) {
            eng_katta = massiv[i];
        }
    }

    printf("%d\n", eng_katta);

    return 0;
}