// JF Functions Notes

#include <stdio.h>

int x = 0;
void add(){
    x++;
}

float divide(int y, int z){
    return (float) y/z;
}

void hello(char* name){
    printf("Hello %s, welcome to my program!\n", name);
}

int main(){
    add();
    add();
    add();
    add();
    add();
    printf("%d\n", x);

    float quotient = divide(8,4);
    printf("%.2f\n", quotient);
    printf("%.2f\n", divide(75,2));

    return 0;
}