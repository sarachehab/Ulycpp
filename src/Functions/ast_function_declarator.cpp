#include "../../include/Functions/ast_function_declarator.hpp"

std::string FunctionDeclarator::getIdentifier() const {
    return identifier_->getIdentifier();
}

void FunctionDeclarator::EmitRISC(std::ostream &stream, int destReg, Context &context) const
{
    if (parameter_list_ != nullptr) {
        parameter_list_->EmitRISC(stream, destReg, context);
    }
}

ExternalDeclarationType FunctionDeclarator::getExternalType() const
{
    return ExternalDeclarationType::_functions;
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
