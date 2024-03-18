#include "../../include/Operations/ast_comparaison.hpp"

Specifier Comparaison::getType(Context& context) const { return Specifier::_int; }

void Comparaison::EmitRISC(std::ostream &stream, int destReg, Context &context) const {
    
    Specifier op_type = left_->getType(context);
    context.setOperationType(op_type);

    int leftReg = context.allocateRegister(op_type);
    left_->EmitRISC(stream, leftReg, context);

    int rightReg = context.allocateRegister(op_type);
    right_->EmitRISC(stream, rightReg, context);

    stream << getInstruction(op_type) << " " << context.getRegisterName(destReg) << ", "
        << context.getRegisterName(leftReg) << ", " << context.getRegisterName(rightReg) << std::endl;
    
    context.freeUpRegister(leftReg);
    context.freeUpRegister(rightReg);
}


void EqualCheck::EmitRISC(std::ostream &stream, int destReg, Context &context) const {
    
    Specifier op_type = left_->getType(context);
    context.setOperationType(op_type);

    int leftReg = context.allocateRegister(op_type);
    left_->EmitRISC(stream, leftReg, context);

    int rightReg = context.allocateRegister(op_type);
    right_->EmitRISC(stream, rightReg, context);

    stream << "sub " << context.getRegisterName(destReg) << ", "<< context.getRegisterName(leftReg) << ", " << context.getRegisterName(rightReg) << std::endl;
    stream << getInstruction(op_type) << " " << context.getRegisterName(destReg) << ", " << context.getRegisterName(destReg) << std::endl;
    
    context.freeUpRegister(leftReg);
    context.freeUpRegister(rightReg);
}


void CompositeComparaison::EmitRISC(std::ostream &stream, int destReg, Context &context) const {
    
    Specifier op_type = left_->getType(context);

    int leftReg = context.allocateRegister(op_type);
    left_->EmitRISC(stream, leftReg, context);

    int rightReg = context.allocateRegister(op_type);
    right_->EmitRISC(stream, rightReg, context);

    int tmpReg = context.allocateRegister(op_type);
    stream << getInstruction(op_type) << " " << context.getRegisterName(tmpReg) << ", "
        << context.getRegisterName(leftReg) << ", " << context.getRegisterName(rightReg) << std::endl;
    stream << "sub " << context.getRegisterName(leftReg) << ", "<< context.getRegisterName(leftReg) << ", " << context.getRegisterName(rightReg) << std::endl;
    stream << "seqz " << context.getRegisterName(leftReg) << ", " << context.getRegisterName(leftReg) << std::endl;
    stream << "or " << context.getRegisterName(destReg) << ", " << context.getRegisterName(tmpReg) << ", " << context.getRegisterName(leftReg) << std::endl;

    context.freeUpRegister(leftReg);
    context.freeUpRegister(rightReg);
}


std::string LessThan::getInstruction(Specifier type) const { 
    switch (type) {
        case Specifier::_int:
            return "slt";
        case Specifier::_float:
            return "flt.f";
        case Specifier::_double:
            return "flt.d";
    }
    return "ERROR, check LessThan";
}
std::string LessThan::getOperation() const { return " < "; }

std::string LessThanEqual::getInstruction(Specifier type) const {
    switch (type) {
        case Specifier::_int:
            return "slt";
        case Specifier::_float:
            return "fslt.f";
        case Specifier::_double:
            return "flt.d";
    }
    return "ERROR, check LessThan";
}
std::string LessThanEqual::getOperation() const { return " <= "; }

std::string GreaterThan::getInstruction(Specifier type) const {
    switch (type) {
        case Specifier::_int:
            return "sgt";
        case Specifier::_float:
            return "fsgt.f";
        case Specifier::_double:
            return "fgt.d";
    }
    return "ERROR, check LessThan";
}

std::string GreaterThan::getOperation() const { return " > "; }

std::string GreaterThanEqual::getInstruction(Specifier type) const {    
    switch (type) {
        case Specifier::_int:
            return "sgt";
        case Specifier::_float:
            return "fsgt.f";
        case Specifier::_double:
            return "fgt.d";
    }
    return "ERROR, check LessThan";
}
std::string GreaterThanEqual::getOperation() const { return " >= "; }

std::string Equal::getInstruction(Specifier type) const { return "seqz "; } // TODO: implement for floats
std::string Equal::getOperation() const { return " == "; }

std::string NotEqual::getInstruction(Specifier type) const { return "snez "; } // TODO: implement for floats
std::string NotEqual::getOperation() const { return " != "; }