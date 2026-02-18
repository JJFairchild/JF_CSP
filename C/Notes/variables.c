// JF Variables Notes

#include <stdio.h>

int main() {
    int num = 8;
    float pi = 3.14159265358979323; 
    char grade = 'A'; // single character uses single quotes
    char name[] = "Nancy"; // string uses [] after variable name

    printf("Working!\n");
    printf("%d\n", num);
    printf("The digits of pi are: %f\n", pi);
    printf("Your name is %s and you are %d years old. You have an %c in programming. Pi is %f.", name, num, grade, pi);
    return 0;
}