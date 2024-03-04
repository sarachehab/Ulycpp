#include <stdio.h>

int f(int x);

void test(double a)
{
    printf("Test function produced value: %f\n", (float)a + 3.2f);
}

int main()
{
    printf("Hello from RISC-V\n");

    test(5.5);
    printf("Example function returned: %d\n", f(0));

    return !(f(0) == 0);
}
