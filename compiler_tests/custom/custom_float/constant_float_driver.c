#include <stdio.h>

float f();

int main()
{
    printf("Hello from RISC-V\n");
    printf("Example function returned: %d\n", f());

    return !(f() == 3.2);
}
