#include <stdio.h>

int main() {
    int n, m;
    scanf("%d %d", &n, &m);

    int massiv[n][m];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%d", &massiv[i][j]);
        }
    }

    int yigindi = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            yigindi += massiv[i][j];
        }
    }

    printf("%d\n", yigindi);

    return 0;
}