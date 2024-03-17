#include "../../include/Functions/ast_function_call.hpp"

std::string FunctionCall::getIdentifier() const {
    return identifier_->getIdentifier();
}


void FunctionCall::EmitRISC(std::ostream &stream, int destReg, Context &context) const {
    arguments_->EmitRISC(stream, destReg, context);
    stream << "jal " << identifier_ << std::endl;
    stream << "nop " << std::endl;
}


void FunctionCall::Print(std::ostream &stream) const {
    stream << identifier_ << "(";
    arguments_->Print(stream);
    stream << ")";
}
