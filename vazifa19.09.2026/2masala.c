#include <stdio.h>
int main(){
FILE*file=fopen(son.txt,"w");
if(file==EOF){
   printf("Faylni ochib bolmaydi!\n");
}
  char ism[100];
  printf("Son kiriting: ");
  scanf("%s", ism);
  fprintf(file, "%s", ism);
  fclose(file);
  printf("Son 'son.txt' fayliga yozildi.\n");
  return 0;
}
