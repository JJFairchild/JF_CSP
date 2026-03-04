// JF Lists Notes

#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(){
    int grades[] = {84, 74, 99, 78, 97};
    printf("%d\n", grades[2]);
    grades[2] = 85;
    printf("%d\n", grades[2]);

    float distance[] = {72.1, 66.3, 45.2, 27.45};

    char names[][20] = {"Alex", "Katie", "Andrew", "Vienna", "Tia", "Treyson", "Xavier", "Jake"};
    printf("%s\n", names[5]);

    for(int i = 20; i>=0; i--){
        printf("%d ", i);
    }
    printf("\n");

    int grade_len = sizeof(grades) / sizeof(grades[0]);
    for(int i=0; i<grade_len; i++){
        printf("%d ", grades[i]+5);
    }
    printf("\n");

    srand(time(NULL));
    int goose = rand()%15+1;
    for(int count=1; count<goose; count++){
        printf("Duck...\n");
    }
    printf("GOOSE!\n");

    return 0;
}