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

void ArrayIndex::computeIndex(std::ostream& stream, int tmpReg, Context& context) const {
    Variable variable_specs = context.getVariableSpecs(getIdentifier());

    int index_reg, memory_cells_allocated = SpecifierSize[variable_specs.type];

    index_->EmitRISC(stream, tmpReg, context);
    stream << "slli " <<  context.getRegisterName(tmpReg) << ", " << context.getRegisterName(tmpReg) << ", " << SpecifierAlign[variable_specs.type] << std::endl; 

    switch (variable_specs.type_scope) {

        case VarScope::_local:
            stream << "add " << context.getRegisterName(tmpReg) << ", " << context.getRegisterName(tmpReg) << ", s0" << std::endl;
            stream << "addi " << context.getRegisterName(tmpReg) << ", " << context.getRegisterName(tmpReg) << ", " << variable_specs.sp_offset << std::endl;
            break;
        
        case VarScope::_global:
            index_reg = context.allocateRegister(Specifier::_int);
            stream << "lui " << context.getRegisterName(index_reg) << ", %hi(" << getIdentifier() << ")" << std::endl;
            stream << "addi " << context.getRegisterName(index_reg) << ", " << context.getRegisterName(index_reg) << ", %lo(" << getIdentifier() << ")" << std::endl;
            stream << "add " << context.getRegisterName(tmpReg) << ", " << context.getRegisterName(tmpReg) << ", " << context.getRegisterName(index_reg) << std::endl;
            context.freeUpRegister(index_reg);
            break;
    }
}

void ArrayIndex::EmitIndex(std::ostream &stream, int destReg, Context &context) const {
    index_->EmitRISC(stream, destReg, context);
}

void ArrayIndex::EmitRISC(std::ostream &stream, int destReg, Context &context) const {
    Variable variable_specs = context.getVariableSpecs(identifier_->getIdentifier());
    int tmpReg = context.allocateRegister(Specifier::_int), indexReg;

    switch (variable_specs.var_type) {

        case ProgramVarType::_pointer:
            indexReg = context.allocateRegister(Specifier::_int);

            stream << "#start printing get array index" << std::endl;
            stream << context.getLoadInstruction(Specifier::_int) << " " << context.getRegisterName(tmpReg) 
                    << ", " << variable_specs.sp_offset << "(s0)" << std::endl;

            EmitIndex(stream, indexReg, context);

            stream << "slli " <<  context.getRegisterName(indexReg) << ", " << context.getRegisterName(indexReg) 
                << ", " << SpecifierAlign[variable_specs.type] << std::endl;
            stream << "add " << context.getRegisterName(tmpReg) << ", " << context.getRegisterName(tmpReg) 
                << ", " << context.getRegisterName(indexReg) << std::endl;
            stream << context.getLoadInstruction(variable_specs.type) << " " << context.getRegisterName(destReg) 
                << ", 0(" << context.getRegisterName(tmpReg) << ")" << std::endl;

            context.freeUpRegister(indexReg);
            break;

        case ProgramVarType::_unique:
        case ProgramVarType::_array:
            computeIndex(stream, tmpReg, context);

            stream << context.getLoadInstruction(variable_specs.type) << " " << context.getRegisterName(destReg) 
                << ", 0(" << context.getRegisterName(tmpReg) << ")" << std::endl;

            variable_specs.reg = destReg;
            context.updateVariableSpecs(identifier_->getIdentifier(), variable_specs);
            break;

        default: throw std::runtime_error("Invalid variable type in ArrayIndex");
    }

    context.freeUpRegister(tmpReg);
}

void ArrayIndex::Print(std::ostream &stream) const {
    identifier_->Print(stream);
    stream << "[";
    index_->Print(stream);
    stream << "]";
}