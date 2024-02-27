#ifndef AST_CONTEXT_HPP
#define AST_CONTEXT_HPP

#include <map>
#include <vector>
#include <string>

// An object of class Context is passed between AST nodes during compilation.
// This can be used to pass around information about what's currently being
// compiled (e.g. function scope and variable names).

struct Variable;
class Context{

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

    std::string registers_name[32] = {
        "zero",
        "ra",
        "sp",
        "gp",
        "tp",
        "t0", "t1", "t2",
        "s0", // or fp
        "s1",
        "a0", "a1",
        "a2", "a3", "a4", "a5", "a6", "a7",
        "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "s11",
        "t3", "t4", "t5", "t6"
    };

    std::map<std::string, Variable> variable_bindings;

public:

    ~ Context(){}
    Context(){}

    void useRegister(int i);
    void freeUpRegister(int i);
    int allocateRegister();
    std::string getRegisterName(int i);

};

enum class Specifier {
    _int,
};

struct Variable {
    Specifier type;
    int sp_offset;
    int reg;

    Variable(Specifier _type, int _sp_offset)
    : type(_type)
    , sp_offset(_sp_offset)
    {}
};

#endif
