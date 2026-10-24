#include <stdio.h>

int main() {
    char ism[100];
    FILE *file;

    printf("Ismingizni kiriting: ");
    scanf("%s", ism);

    file = fopen("ism.txt", "w");

    if (file == NULL) {
        printf("Faylni ochib bo'lmadi!\n");
        return 1;
    }

    fprintf(file, "%s", ism);

    fclose(file);

    printf("Ism 'ism.txt' fayliga yozildi.\n");

    return 0;
}