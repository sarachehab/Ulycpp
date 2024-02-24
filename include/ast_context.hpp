#ifndef AST_CONTEXT_HPP
#define AST_CONTEXT_HPP

// An object of class Context is passed between AST nodes during compilation.
// This can be used to pass around information about what's currently being
// compiled (e.g. function scope and variable names).
class Context
{

private:

    int used_registers[32] = {
        1,                              // zero
        1,                              // return address ra
        1,                              // stack pointer sp
        1,                              // global pointer gp
        1,                              // thread pointer tp
        0, 0, 0,                        // temporaries t0-2
        1,                              // saved register s0 / frame pointer fp
        1,                              // saved register s1
        1, 1,                           // function arguments and return values a0-1
        1, 1, 1, 1, 1, 1,               // function arguments a2-7
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1,   // saved register s2-11
        0, 0, 0, 0                      // saved registers t3-6
    };

public:

    ~ Context(){}
    Context(){}

    void useRegister(int i);
    void freeUpRegister(int i);
    int allocateRegister();
    
};

#endif
