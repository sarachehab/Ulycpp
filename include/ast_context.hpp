#ifndef AST_CONTEXT_HPP
#define AST_CONTEXT_HPP

#include <map>
#include <vector>
#include <string>
#include <unordered_map>

// An object of class Context is passed between AST nodes during compilation.
// This can be used to pass around information about what's currently being
// compiled (e.g. function scope and variable names).

struct Variable;
enum class Specifier;
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
    int current_stack_size;

public:

    ~ Context(){}
    Context() : current_stack_size(16) {}

    void useRegister(int i);
    void freeUpRegister(int i);
    int allocateRegister(std::ostream &stream);
    std::string getRegisterName(int i);

    // function to add to bindings
    void addVariable(std::string name, int memory_cells_allocated, int sp_offset, Specifier type, int reg);

    // get variable specs
    Variable getVariableSpecs(std::string name);

    // modify variable specs
    void updateVariableSpecs(std::string name, Variable variable_specs);

    // modifiy stack size when allocating memory
    int increaseCurrentStackSize(int memory_cells_allocated);

};

enum class Specifier {
    _int,
};


inline std::unordered_map <Specifier, int> SpecifierSize {
    {Specifier::_int, 4}
};

struct Variable {
    Specifier type;
    int memory_cells_allocated;
    int sp_offset;
    int reg;

    Variable() = default; // Default constructor

    Variable(Specifier _type, int _memory_cells_allocated, int _sp_offset, int _reg)
    : type(_type)
    , memory_cells_allocated(_memory_cells_allocated)
    , sp_offset(_sp_offset)
    , reg(_reg)
    {}
};

#endif
