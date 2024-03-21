#include <stdio.h>
int f();

int main()
{   
    printf("Function returns %d \n", f());
    return !(f()==92);
}
