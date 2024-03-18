#include "ast_constant.hpp"


Specifier IntConstant::getType(Context& context) const { return Specifier::_int; }

void IntConstant::EmitRISC(std::ostream &stream, int destReg, Context &context) const {
    stream << "li " << context.getRegisterName(destReg) << ", " << value_ << std::endl;
}

Specifier FloatConstant::getType(Context& context) const { return Specifier::_float; } // todo: or double

void FloatConstant::EmitRISC(std::ostream &stream, int destReg, Context &context) const {

    Specifier type = context.getLastOperationType();
    std::string label;
    int label_number;

    switch(type) {
        case Specifier::_double:
            context.defineDouble(value_);
            label = "LD";
            label_number = context.getDoubleLabelNumber();
            break;
        case Specifier::_float:
            context.defineFloat(float(value_));
            label = "LF";
            label_number = context.getFloatLabelNumber();
            break;
        default: throw std::runtime_error("Undefined Type in FloatConstant");
    }

    

    int addrReg = context.allocateRegister(Specifier::_int);
    stream << "lui " << context.getRegisterName(addrReg) << ", %hi(." << label << label_number << ")" << std::endl; // todo: change value
    stream << context.getLoadInstruction(type) << " " << context.getRegisterName(destReg) << ", %lo(." << label << label_number << ")(" << context.getRegisterName(addrReg) << ")" << std::endl;
    context.freeUpRegister(addrReg);
}


void IntConstant::Print(std::ostream &stream) const {
    stream << value_;
}

void FloatConstant::Print(std::ostream &stream) const {
    stream << value_;
}