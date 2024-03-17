#include "ast_constant.hpp"


Specifier IntConstant::getType(Context& context) const { return Specifier::_int; }

void IntConstant::EmitRISC(std::ostream &stream, int destReg, Context &context) const {
    stream << "li " << context.getRegisterName(destReg) << ", " << value_ << std::endl;
}

Specifier FloatConstant::getType(Context& context) const { return Specifier::_float; } // todo: or double

void FloatConstant::EmitRISC(std::ostream &stream, int destReg, Context &context) const {

    context.defineFloat(value_);

    int addrReg = context.allocateRegister(Specifier::_int);
    stream << "lui " << context.getRegisterName(addrReg) << ", %hi(.LC" << context.getFloatLabelNumber() << ")" << std::endl; // todo: change value
    stream << "fld " << context.getRegisterName(destReg) << ", %lo(.LC" << context.getFloatLabelNumber() << ")(" << context.getRegisterName(addrReg) << ")" << std::endl;
    context.freeUpRegister(addrReg);
}


void Constant::Print(std::ostream &stream) const {
    stream << value_;
}