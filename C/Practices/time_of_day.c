//JF Time of Day

#include <stdio.h>
#include <time.h>

int main() {
    time_t seconds = time(NULL); // Get current time in seconds
    struct tm *t = localtime(&seconds); // Convert to local time structure
    int hour = t->tm_hour;
    
    if(hour<6){printf("WHY ARE YOU AWAKE RIGHT NOW?!");}
    else if(hour<9){printf("Good morning!");}
    else if(hour<12){printf("Good day to you!");}
    else if(hour<20){printf("Good afternoon!");}
    else{printf("Good night!");}

    return 0;
}