// JF Conditionals Notes

#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main(){
    bool is_programming = true;
    
    int grade = 75;
    if (grade >= 90) {
        printf("Your grade is %d percent, that is an A!\n", grade);
    } else if (grade >= 80) {
        printf("Your grade is %d percent, that is a B.\n", grade);
    } else if (grade >= 70) {
        printf("Your grade is %d percent, that is a C.\n", grade);
    } else if (grade >= 60) {
        printf("Your grade is %d percent, that is a D.\n", grade);
    } else {
        printf("Your grade is %d percent, that means you are failing.\n", grade);
    }

    int num = -442;
    if (num < 10 && num > -10) {
        printf("Your number is %d, which is a single digit number.\n", num);
    } else if (num < 100 && num > -100) {
        printf("Your number is %d, which is a double digit number.\n", num);
    } else if (num < 1000 && num > -1000) {
        printf("Your number is %d, which is a triple digit number.\n", num);
    } else {
        printf("Your number is %d, that's a pretty big number!\n", num);
    }

    char name[] = "Andrew";
    if (strcmp(name, "Andrew") == 0) {
        printf("Welcome Admin!\n");
    } else {
        printf("Welcome %s!\n", name);
    }

    return 0;
}