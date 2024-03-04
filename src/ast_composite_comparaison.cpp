#include "ast_composite_comparaison.hpp"

void CompositeComparaison::EmitRISC(std::ostream &stream, int destReg, Context &context) const {
    int leftReg = context.allocateRegister(stream);
    left_->EmitRISC(stream, leftReg, context);
    int rightReg = context.allocateRegister(stream);
    right_->EmitRISC(stream, rightReg, context);
    int tmpReg = context.allocateRegister(stream);
    stream << getInstruction() << context.getRegisterName(tmpReg) << ", "
        << context.getRegisterName(leftReg) << ", " << context.getRegisterName(rightReg) << std::endl;
    stream << "sub " << context.getRegisterName(leftReg) << ", "<< context.getRegisterName(leftReg) << ", " << context.getRegisterName(rightReg) << std::endl;
    stream << "seqz " << context.getRegisterName(leftReg) << ", " << context.getRegisterName(leftReg) << std::endl;
    stream << "or " << context.getRegisterName(destReg) << ", " << context.getRegisterName(tmpReg) << ", " << context.getRegisterName(leftReg) << std::endl;
    context.freeUpRegister(leftReg);
    context.freeUpRegister(rightReg);
}

void CompositeComparaison::Print(std::ostream &stream) const {
    stream << "(";
    left_->Print(stream);
    stream << getOperation();
    right_->Print(stream);
    stream << ")";
}
