#include "ast_comparaison.hpp"

void Comparaison::EmitRISC(std::ostream &stream, int destReg, Context &context) const {
    int leftReg = context.allocateRegister(stream);
    left_->EmitRISC(stream, leftReg, context);
    int rightReg = context.allocateRegister(stream);
    right_->EmitRISC(stream, rightReg, context);
    stream << "sub " << context.getRegisterName(destReg) << ", "<< context.getRegisterName(leftReg) << ", " << context.getRegisterName(rightReg) << std::endl;
    stream << getInstruction() << context.getRegisterName(destReg) << ", " << context.getRegisterName(destReg) << std::endl;
    context.freeUpRegister(leftReg);
    context.freeUpRegister(rightReg);
}

void Comparaison::Print(std::ostream &stream) const {
    stream << "(";
    left_->Print(stream);
    stream << getOperation();
    right_->Print(stream);
    stream << ")";
}
