#include "ast_context.hpp"
#include <iostream>


void Context::useRegister(int i){
    used_registers[i] = 1;
}

void Context::freeUpRegister(int i){
    used_registers[i] = 0;
}

int Context::allocateRegister(){

    // find unused temporary register
    for (int i = 5; i < 32; i++){
        if (!used_registers[i]){
            useRegister(i);
            return i;
        }
    }

    // if all registers are used up, free up a register and use it
    for (auto it = variable_bindings.begin(); it != variable_bindings.end(); it++){
        int reg = it->second.reg;
        if (reg != -1){
            freeUpRegister(reg);
            it->second.reg; // variable spilled into memory, no longer in register file
            return reg;
        }
    }

    throw std::runtime_error("All temporary registers used up! Check ast_context.cpp");

}

std::string Context::getRegisterName(int i){
    return registers_name[i];
}
