#include "../../include/Operations/ast_binary_operation.hpp"

Specifier BinaryOperation::getType(Context& context) const { return left_->getType(context); }

void BinaryOperation::EmitRISC(std::ostream &stream, int destReg, Context &context) const {
    
    Specifier type = context.getLastOperationType(); 

    int leftReg = context.allocateRegister(type);
    left_->EmitRISC(stream, leftReg, context);

    int rightReg = context.allocateRegister(type);
    right_->EmitRISC(stream, rightReg, context);

    stream << getInstruction(type) << " " << context.getRegisterName(destReg) << ", "
        << context.getRegisterName(leftReg) << ", " << context.getRegisterName(rightReg) << std::endl;

    context.freeUpRegister(leftReg);
    context.freeUpRegister(rightReg);
}

void BinaryOperation::Print(std::ostream &stream) const {
    stream << "(";
    left_->Print(stream);
    stream << getOperation();
    right_->Print(stream);
    stream << ")";
}
