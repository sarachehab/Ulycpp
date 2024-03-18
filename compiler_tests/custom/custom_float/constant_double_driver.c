#include <stdio.h>

double f();

int main()
{
    printf("Hello from RISC-V\n");
    printf("Example function returned: %f\n", f());

    double x = 3.2;
    return !(f() == x);
}
