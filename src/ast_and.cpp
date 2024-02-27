#include "ast_and.hpp"

void And::EmitRISC(std::ostream &stream, int destReg, Context &context) const
{
    int leftReg = context.allocateRegister();
    left_->EmitRISC(stream, leftReg, context);
    int rightReg = context.allocateRegister();
    right_->EmitRISC(stream, rightReg, context);
    stream << "and " << context.getRegisterName(destReg) << ", "
        << context.getRegisterName(leftReg) << ", " << context.getRegisterName(rightReg) << std::endl;
    context.freeUpRegister(leftReg);
    context.freeUpRegister(rightReg);
}

void And::Print(std::ostream &stream) const
{
    stream << "(";
    left_->Print(stream);
    stream << " & ";
    right_->Print(stream);
    stream << ")";
}
