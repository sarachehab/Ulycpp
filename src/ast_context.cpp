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

    // TODO solution if all temporary registers are used
    throw std::runtime_error("All temporary registers used up! Check ast_context.cpp");

}