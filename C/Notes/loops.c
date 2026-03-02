// JF Loops Notes

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

int main() {
    int i = 1;
    while (i<=10) {
        printf("%d, ", i);
        i++;
    }

    srand(time(NULL));

    int goose = rand()%10+1;
    int count = 1;
    while(count<goose){
        printf("\nDuck...");
        count++;
    }
    printf("\nGOOSE!\n");

    int num = rand()%20+1;
    while(true){
        int guess;
        printf("Guess a number between 1 and 100: ");
        scanf("%d", &guess);
        if(guess == num){
            printf("You guessed the number!\n");
            break;
        } else if(guess < num){
            printf("That's too low!\n");
        } else{
            printf("That's too high!\n");
        }
    }

    return 0;
}