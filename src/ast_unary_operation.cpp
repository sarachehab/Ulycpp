#include "ast_unary_operation.hpp"

void UnaryOperation::EmitRISC(std::ostream &stream, int destReg, Context &context) const {
    int srcReg = context.allocateRegister();
    value_->EmitRISC(stream, srcReg, context);
    stream << getInstruction() << context.getRegisterName(destReg) << ", "
        << context.getRegisterName(srcReg) << std::endl;
    context.freeUpRegister(srcReg);
}

void UnaryOperation::Print(std::ostream &stream) const {
    stream << "(";
    stream << getOperation();
    value_->Print(stream);
    stream << ")";
}
