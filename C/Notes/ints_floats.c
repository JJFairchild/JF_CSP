// JF, Integers and Floats

#include <stdio.h>
#include <math.h>

int main(){
    int people = 55;
    int apples = 64;

    printf("People: %d, Apples: %d\n", people, apples);
    printf("Each person gets %f apples.\n", (float) apples/people);

    const long double pi = 3.14159265358979323L;
    float liters = 2.4f;
    float fahrenheit = 72.8f;

    __mingw_printf("Pi = %.17Lf, Liters = %d, Fahrenheit = %.1f\n", pi, (int) round(liters), fahrenheit);
    printf("%f is 2 to the power of 3.\n", (int) pow(2,3));

    return 0;
}