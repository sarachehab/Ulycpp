#include "../../include/Pointers/ast_pointer.hpp"

std::string Pointer::getIdentifier() const {
    return address_->getIdentifier();
}

void Pointer::EmitRISC(std::ostream& stream, int destReg, Context& context) const {
    std::cerr << "Pointer::EmitRISC" << std::endl;
}

void Pointer::Print(std::ostream& stream) const {
    stream << "*";
    getIdentifier();
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