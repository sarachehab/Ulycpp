#include "../../include/Functions/ast_function_declarator.hpp"

std::string FunctionDeclarator::getIdentifier() const {
    return identifier_->getIdentifier();
}

void FunctionDeclarator::EmitRISC(std::ostream &stream, int destReg, Context &context) const
{
    // identifier_->EmitRISC(stream, destReg, context);
    // stream << ":" << std::endl;
    if (parameter_list_ != nullptr) {
        parameter_list_->EmitRISC(stream, destReg, context);
    }
}

void FunctionDeclarator::Print(std::ostream &stream) const
{
    identifier_->Print(stream);
    stream << "(";
    if (parameter_list_ != nullptr) {
        parameter_list_->Print(stream);
    }
    stream << ")";
}
