#include "../../include/Operations/ast_unary_operation.hpp"
#include "../../include/Operations/ast_arithmetic_operation.hpp"

Specifier UnaryOperation::getType(Context& context) const { return value_->getType(context); }

void UnaryOperation::EmitRISC(std::ostream &stream, int destReg, Context &context) const {
    Specifier type = value_->getType(context);
    int srcReg = context.allocateRegister(value_->getType(context));
    value_->EmitRISC(stream, srcReg, context);
    stream << getInstruction(type) << context.getRegisterName(destReg) << ", "
        << context.getRegisterName(srcReg) << std::endl;
    context.freeUpRegister(srcReg);
}

void UnaryOperation::Print(std::ostream &stream) const {
    stream << "(";
    stream << getOperation();
    value_->Print(stream);
    stream << ")";
}
