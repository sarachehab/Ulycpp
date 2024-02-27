#include "ast_substraction.hpp"

void Substraction::EmitRISC(std::ostream &stream, int destReg, Context &context) const
{
    int leftReg = context.allocateRegister();
    left_->EmitRISC(stream, leftReg, context);
    int rightReg = context.allocateRegister();
    right_->EmitRISC(stream, rightReg, context);
    stream << "sub " << context.getRegisterName(destReg) << ", "
        << context.getRegisterName(leftReg) << ", " << context.getRegisterName(rightReg) << std::endl;
    context.freeUpRegister(leftReg);
    context.freeUpRegister(rightReg);
}

void Substraction::Print(std::ostream &stream) const
{
    stream << "(";
    left_->Print(stream);
    stream << " - ";
    right_->Print(stream);
    stream << ")";
}
