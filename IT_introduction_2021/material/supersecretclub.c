#include <string.h>
#include <stdio.h>
int main(int argv, char *args[]){
  //printf("%d",argv);
  //printf("%s",args[0]);
  //printf("%s",args[1]);

  char buf[1];
  char n[1];
  n[0]='N';
  strcpy(buf,args[1]);

  if(*n=='Y')
    puts("join our club!");
  else
    puts("you shall not pass");
}
