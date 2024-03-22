#include "../../include/Pointers/ast_pointer.hpp"

std::string Pointer::getIdentifier() const {
    return address_->getIdentifier();
}

std::string AddressOf::getIdentifier() const {
    return variable_->getIdentifier();
}

int Pointer::fetchVariable(Context &context) const {
    Variable variable_specs = context.getVariableSpecs(getIdentifier());

    if (variable_specs.reg == -1) {
        Specifier type = variable_specs.type;
        int allocated_register = context.allocateRegister(type);
        variable_specs.reg = allocated_register;
    }

    context.updateVariableSpecs(getIdentifier(), variable_specs);
    return variable_specs.reg;
}

int AddressOf::fetchVariable(Context &context) const {
    Variable variable_specs = context.getVariableSpecs(getIdentifier());

    if (variable_specs.reg == -1) {
        Specifier type = variable_specs.type;
        int allocated_register = context.allocateRegister(type);
        variable_specs.reg = allocated_register;
    }

    context.updateVariableSpecs(getIdentifier(), variable_specs);
    return variable_specs.reg;
}

void Pointer::EmitRISC(std::ostream& stream, int destReg, Context& context) const {
    std::cerr << "Pointer::EmitRISC" << std::endl;
}

void PointerDereference::EmitRISC(std::ostream& stream, int destReg, Context& context) const {
    Variable var_specs = context.getVariableSpecs(getIdentifier());

    int tmpReg = context.allocateRegister(Specifier::_int);

    stream << context.getLoadInstruction(Specifier::_int) << " " << context.getRegisterName(tmpReg) 
        << ", " << var_specs.sp_offset << "(s0)" << std::endl;

    stream << context.getLoadInstruction(var_specs.pointing_to) << " " << context.getRegisterName(destReg) 
        << ", 0(" << context.getRegisterName(tmpReg) << ")" << std::endl;

    context.freeUpRegister(tmpReg);
}

void AddressOf::EmitRISC(std::ostream& stream, int destReg, Context& context) const {
    Variable var_specs = context.getVariableSpecs(getIdentifier());

    stream << "addi " << context.getRegisterName(destReg) << ", s0, " << var_specs.sp_offset << std::endl;

    // stream << context.getLoadInstruction(Specifier::_int) << " " << context.getRegisterName(destReg) 
    //     << ", " << var_specs.sp_offset << "(s0)" << std::endl;
}


void Pointer::Print(std::ostream& stream) const {
    stream << "*";
    getIdentifier();
}

void AddressOf::Print(std::ostream& stream) const {
    stream << "&";
    getIdentifier();
}