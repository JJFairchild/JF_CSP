// JF, Financial Calculator

#include <stdio.h>

float get_expense(char* prompt){
    float expense;
    printf("What is your monthly %s? $", prompt);
    scanf("%f", &expense);
    return expense;
}

void calc_percent(char* category, float expense, float income){
    printf("Your %s is %.2f percent of your income.\n\n", category, expense/income*100);
}

int main(){
    float income;
    printf("What is your monthly income? $");
    scanf("%f", &income);
    printf("\n");

    float sum;
    char categories[4][15] = {"rent", "utilities", "groceries", "transportation"};

    for (int i=0; i<4; i++) {
        float expense = get_expense(categories[i]);
        calc_percent(categories[i], expense, income);
        sum += expense;
    }

    printf("You should save $%.2f a month, that is 10 percent of your income.\n\nYou have $%.2f of spending money each month!", income/10, 0.9*income - sum);

    return 0;
}