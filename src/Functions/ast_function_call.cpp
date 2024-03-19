#include "../../include/Functions/ast_function_call.hpp"

std::string FunctionCall::getIdentifier() const {
    return function_name_->getIdentifier();
}

Specifier FunctionCall::getType(Context& context) const {
    return context.getReturnType(getIdentifier());
}


void FunctionCall::createHeader(std::ostream& stream, Context& context) const {
    std::vector<int> temporary_registers = {5, 6, 7, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 60, 61, 62, 63};
    int reg;
    Specifier type;

    for (int i = 0; i < temporary_registers.size(); i++){

        reg = temporary_registers[i];
        type = context.getRegisterType(reg);

        int memory_cells_allocated = SpecifierSize[type];
        int memory_offset = context.increaseCurrentStackSize(memory_cells_allocated);

        stream << context.getStoreInstruction(type) << " " << context.getRegisterName(reg) << ", " << -memory_offset << "(s0)" << std::endl;
        
        register_mapping_type[reg] = type;
    }
}

void FunctionCall::createFooter(std::ostream& stream, Context& context) const {
    std::vector<int> temporary_registers = {5, 6, 7, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 60, 61, 62, 63};
    int reg, memory_cells_allocated, memory_offset = context.increaseCurrentStackSize(0);
    Specifier type;

    for (int i = temporary_registers.size()-1; i >= 0; i=i-1){
        std::cerr << "in loop " << i << std::endl;
        reg = temporary_registers[i];
        type = register_mapping_type[reg];
        memory_cells_allocated = SpecifierSize[type];

        stream << context.getLoadInstruction(type) << " " << context.getRegisterName(reg) << ", " << -memory_offset << "(s0)" << std::endl;
        
        // will not need temporary registers again, flush from memory
        memory_offset = context.increaseCurrentStackSize(-memory_cells_allocated);
        std::cerr << "exit loop " << i << std::endl;
    }
    memory_offset = context.increaseCurrentStackSize(memory_cells_allocated);
}



void FunctionCall::EmitRISC(std::ostream &stream, int destReg, Context &context) const {

    Specifier return_type = getType(context);

    std::cerr << "In function call print" << std::endl;
    if (arguments_ != nullptr){
        arguments_->EmitRISC(stream, destReg, context);
    }

    int returnReg;
    switch(return_type){
        case Specifier::_int:
            returnReg = 10;
            break;
        case Specifier::_double:
        case Specifier::_float:
            returnReg = 42;
            break;
        default: throw std::runtime_error("Type not recognised in FunctionCall EmitRISC");
    }

    createHeader(stream, context);
    stream << "call " << function_name_->getIdentifier() << std::endl;
    context.FlushRegisters();
    stream << "nop " << std::endl;
    createFooter(stream, context);
    stream << context.getMoveInstruction(return_type) << " " << context.getRegisterName(destReg) << ", " << context.getRegisterName(returnReg) << std::endl;
}


void FunctionCall::Print(std::ostream &stream) const {
    stream << function_name_->getIdentifier() << "(";
    if (arguments_ != nullptr){
        arguments_->Print(stream);
    }
    stream << ")";
}
