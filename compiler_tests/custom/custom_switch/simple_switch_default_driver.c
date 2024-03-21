#include <stdio.h>

int f(int x);

int main(){

    printf("%d\n", f(1));

    return !(f(1) == 3);
}