#include "ast_context.hpp"
#include <iostream>


void Context::useRegister(int i){
    used_registers[i] = 1;
}

void Context::freeUpRegister(int i){
    used_registers[i] = 0;
}

int Context::allocateRegister(std::ostream &stream){

    // find unused temporary register
    for (int i = 5; i < 32; i++){
        if (!used_registers[i]){
            useRegister(i);
            return i;
        }
    }

    // if all registers are used up, free up a register and use it
    for (auto it = variable_bindings.begin(); it != variable_bindings.end(); it++){
        Variable variable_specs = it->second;
        int reg = variable_specs.reg;
        if (reg != -1){
            freeUpRegister(reg);
            // todo: size of store instructions depends on type
            // todo: print to stream instead of std::cout fix???????
            stream << "Missing code in allocateRegister, check ast_context" << std::endl;
            variable_specs.reg = -1; // variable spilled into memory, no longer in register file
            return reg;
        }
    }

    throw std::runtime_error("All temporary registers used up! Check ast_context.cpp");

}

std::string Context::getRegisterName(int i){
    return registers_name[i];
}


void Context::addVariable(std::string name, int memory_cells_allocated, int sp_offset, Specifier type, int reg){
    variable_bindings[name] = Variable(type, memory_cells_allocated, sp_offset, reg);
}

Variable Context::getVariableSpecs(std::string name) {
    return variable_bindings[name];
}

void Context::updateVariableSpecs(std::string name, Variable variable_specs){
    variable_bindings[name] = variable_specs;
}



int Context::increaseCurrentStackSize(int memory_cells_allocated) {
    current_stack_size += memory_cells_allocated;
    return current_stack_size;
}
