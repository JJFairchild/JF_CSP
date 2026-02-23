// JF, Financial Calculator

#include <stdio.h>

int main(){
    float income;
    printf("What is your monthly income? $");
    scanf("%f", &income);
    printf("\n");

    float sum;
    char categories[4][15] = {"rent", "utilities", "groceries", "transportation"};
    float expenses[4];

    int i;
    for (i=0; i<4; i++) {
        printf("What is your monthly %s? $", categories[i]);
        scanf("%f", &expenses[i]);
        printf("Your %s is %.2f percent of your income.\n\n", categories[i], expenses[i]/income*100);
        sum += expenses[i];
    }

    printf("You should save $%.2f a month, that is 10 percent of your income.\n\nYou have $%.2f of spending money each month!", income/10, 0.9*income - sum);

    return 0;
}