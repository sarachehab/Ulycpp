#include "../../include/Arrays/ast_array_index.hpp"

int ArrayIndex::fetchVariable(Context &context) const {
    Variable variable_specs = context.getVariableSpecs(identifier_->getIdentifier());

    if (variable_specs.reg == -1) {
        Specifier type = variable_specs.type;
        int allocated_register = context.allocateRegister(type);
        variable_specs.reg = allocated_register;
    }

    context.updateVariableSpecs(identifier_->getIdentifier(), variable_specs);
    return variable_specs.reg;
}

std::string ArrayIndex::getIdentifier() const {
    return identifier_->getIdentifier();
}

Specifier ArrayIndex::getType(Context &context) const {
    return context.getVariableSpecs(identifier_->getIdentifier()).type;
}

int ArrayIndex::getCurrentIndex() const {
    return index_->getValue();
}

void ArrayIndex::EmitRISC(std::ostream &stream, int destReg, Context &context) const {
    Variable variable_specs = context.getVariableSpecs(identifier_->getIdentifier());
    int tmpReg = context.allocateRegister(variable_specs.type);

    int memory_cells_allocated = SpecifierSize[variable_specs.type];
    int offset = variable_specs.memory_cells_allocated;

    index_->EmitRISC(stream, destReg, context);

    stream << "slli " <<  context.getRegisterName(destReg) << ", " << context.getRegisterName(destReg) << ", 2" << std::endl; 
    stream << "addi " << context.getRegisterName(tmpReg) << ", s0, -16" << std::endl;

    stream << "add " << context.getRegisterName(destReg) << ", " << context.getRegisterName(tmpReg) 
        << ", " << context.getRegisterName(destReg) << std::endl;

    stream << context.getLoadInstruction(variable_specs.type) << " " << context.getRegisterName(destReg) 
        << ", " << - offset - 4 << "(" << context.getRegisterName(destReg) << ")" << std::endl;

    variable_specs.reg = destReg; 

    context.updateVariableSpecs(identifier_->getIdentifier(), variable_specs);
}

void ArrayIndex::Print(std::ostream &stream) const {
    identifier_->Print(stream);
    stream << "[";
    index_->Print(stream);
    stream << "]";
}