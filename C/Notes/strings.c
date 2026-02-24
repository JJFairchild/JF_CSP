// JF Strings

#include <stdio.h>
#include <string.h>

int main(){
    char subject[] = "Computer Science Principles";
    char fruit[] = "grape";

    char book[50];
    printf("What is your favorite book?: ");
    //scanf("%s", &book);
    fgets(book, sizeof(book), stdin);

    printf("%s\n%s\n%s", subject, fruit, book);

    char first[] = "Jonas";
    char last[] = "Fairchild";
    strcat(first, " ");
    strcat(first, last);
    printf("%s\n", first);

    char alpha[27];
    strcat(alpha, "abcdefghijklmnopqrstuvwxyz");
    printf("%s\n", alpha);

    printf("%ld\n", strlen(first));

    return 0;
}