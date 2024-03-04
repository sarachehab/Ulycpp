#include "ast_direct_declarator.hpp"

std::string DirectDeclarator::getIdentifier() const {
    return identifier_->getIdentifier();
}

void DirectDeclarator::EmitRISC(std::ostream &stream, int destReg, Context &context) const
{
    identifier_->EmitRISC(stream, destReg, context);
    stream << ":" << std::endl;
    if (parameter_list_ != nullptr) {
        parameter_list_->EmitRISC(stream, destReg, context);
    }
}

void DirectDeclarator::Print(std::ostream &stream) const
{
    identifier_->Print(stream);
    stream << "(";
    if (parameter_list_ != nullptr) {
        parameter_list_->Print(stream);
    }
    stream << ")";
}
