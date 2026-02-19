// JF Variables Notes

#include <stdio.h>

int main() {
    int age;
    printf("Tell me your age: ");
    scanf("%d", &age);

    char name[50];
    printf("Tell me your name: ");
    scanf("%s", &name);
    
    char grade = 'A'; // single character uses single quotes

    printf("Your name is %s and you are %d years old. You have an %c in programming.", name, age, grade);
    return 0;
}