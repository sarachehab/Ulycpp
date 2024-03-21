#ifndef AST_CONTEXT_HPP
#define AST_CONTEXT_HPP

#include <map>
#include <vector>
#include <string>
#include <unordered_map>
#include <map>
#include <stack>
#include <cstring>


// An object of class Context is passed between AST nodes during compilation.
// This can be used to pass around information about what's currently being
// compiled (e.g. function scope and variable names).

struct Variable;
struct Scope;
struct Function;
union FloatIntUnion;

enum class Specifier {
    _int,
    _unsigned,
    _float,
    _double,
    _char,
};

enum class ProgramVarType {
    _unique,
    _pointer,
    _array,
};

enum class VarScope {
    _local,
    _global,
};

enum class ExternalDeclarationType{
    _functions, 
    _global,
};

typedef std::map<std::string, Variable> VariableBindings;

class Context{

private:

    int used_registers[64] = {
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
        0, 0, 0, 0,                     // saved registers t3-6
        0, 0, 0, 0, 0, 0, 0, 0,         // float temporary registers ft1-ft7
        1, 1,                           // float saved registers fs1-fs0
        1, 1,                           // float arguments and return values fa1-0
        0, 0, 0, 0, 0, 0,               // float function arguments fa1-7
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,   // float saved register fs1-00
        1, 1, 1, 1                      // float saved registers ft3-00
    };

    std::string registers_name[64] = {
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
        "t3", "t4", "t5", "t6",
        "ft0", "ft1", "ft2", "ft3", "ft4", "ft5", "ft6", "ft7",
        "fs0", "fs1",
        "fa0", "fa1",
        "fa2", "fa3", "fa4", "fa5", "fa6", "fa7",
        "fs2", "fs3", "fs4", "fs5", "fs6", "fs7", "fs8", "fs9", "fs10", "fs11",
        "ft8", "ft9", "ft10", "ft11"
    };

    std::vector<Specifier> registers_type;

    std::vector<Scope> scopes;

    std::stack<std::string> start_labels;   // for continue
    std::stack<std::string> end_labels;     // for break
    
    std::map<std::string, Function> functions;         // for return statemetns
    Specifier current_return_type;
    std::string current_function_end_label;

    std::vector<std::string> floats_representation;
    std::vector<std::string> doubles_representation;

    Specifier last_operation_type;

public:

    ~ Context(){}
    Context() {      // Default constructor

        for (int i = 0; i < 32; i++){
            registers_type.push_back(Specifier::_int);
        }
        for (int i = 0; i < 32; i++){
            registers_type.push_back(Specifier::_float);
        }

        enterScope(0);
    }

    void useRegister(int i, Specifier type);
    void freeUpRegister(int i);
    int allocateRegister(Specifier type);
    std::string getRegisterName(int i) const;
    Specifier getRegisterType(int i) const;


    // function to enter scope
    void enterScope(int current_stack_size_);

    // function to exit scope();
    void exitScope();

    int getCurrentScopeSize();

    // function to add to bindings
    void addVariable(std::string name, int memory_cells_allocated, int sp_offset, Specifier type, VarScope type_scope, ProgramVarType var_type, int reg);

    // find variable in bindings
    int findVariableScope(std::string name) const ;

    // get variable specs
    Variable getVariableSpecs(std::string name) const ;

    // modify variable specs
    void updateVariableSpecs(std::string name, Variable variable_specs);

    // modifiy stack size when allocating memory
    int increaseCurrentStackSize(int memory_cells_allocated);

    // flush register file
    void FlushRegisters();

    // create label for jumps
    std::string createLabel(std::string name) const;

    // adjust stacks within loops
    void pushLabels(std::string start_label, std::string end_label);
    void popLabels();

    // get labels for continue and break statements
    std::string getStartLabel() const;
    std::string getEndLabel() const;


    // define function
    void enterFunction(std::string function_name, Specifier type);
    void exitFunction();
    void declareExternalFunction(std::string function_name, Specifier return_type);
    Specifier getReturnType(std::string function_name) const ;
    Specifier getReturnType() const ;

    // get end label of function for return
    std::string getFunctionEndLabel() const;

    // defining float immediates
    void defineFloat(float number);
    void defineDouble(double number);
    unsigned int getFloatLabelNumber() const;
    unsigned int getDoubleLabelNumber() const;
    void printImmediates(std::ostream& stream) const;

    std::string getStoreInstruction(Specifier type) const;
    std::string getLoadInstruction(Specifier type) const;
    std::string getMoveInstruction(Specifier type) const;

    void setOperationType(Specifier type);
    Specifier getLastOperationType() const;
};

inline std::unordered_map <Specifier, int> SpecifierSize {
    {Specifier::_int, 4},
    {Specifier::_unsigned, 4},
    {Specifier::_float, 4},
    {Specifier::_double, 8},
    {Specifier::_char, 1},
};

inline std::unordered_map <Specifier, int> SpecifierAlign {
    {Specifier::_int, 2},
    {Specifier::_float, 2},
    {Specifier::_double, 3},
};

struct Variable {
    Specifier type;
    VarScope type_scope;
    ProgramVarType var_type;
    int memory_cells_allocated;
    int sp_offset;
    int reg;

    Variable() = default; // Default constructor

    Variable(Specifier _type, VarScope _type_scope, ProgramVarType _var_type, int _memory_cells_allocated, int _sp_offset, int _reg)
        : type(_type)
        , type_scope(_type_scope)
        , var_type(_var_type)
        , memory_cells_allocated(_memory_cells_allocated)
        , sp_offset(_sp_offset)
        , reg(_reg)
    {}
};


struct Scope {
    VariableBindings variable_bindings;
    unsigned int current_scope_size;

    Scope ()
        : current_scope_size(0)
    {}
    Scope (int current_scope_size_)
        : current_scope_size(current_scope_size_)
    {}
};


struct Function {
    Specifier return_type;
    // TODO: add return type

    Function(){}

    Function (Specifier return_type_)
        : return_type(return_type_)
    {}
};

union FloatIntUnion {
    float f;
    uint32_t i;
};

union DoubleIntUnion {
    double d;
    struct {
        uint32_t lower; // Assuming little-endian
        uint32_t upper;
    } parts;
};

#endif
