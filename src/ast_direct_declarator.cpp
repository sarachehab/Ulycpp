#include "ast_direct_declarator.hpp"

void DirectDeclarator::EmitRISC(std::ostream &stream, int destReg, Context &context) const
{
    identifier_->EmitRISC(stream, destReg, context);
    stream << ":" << std::endl;
}

void DirectDeclarator::Print(std::ostream &stream) const
{
    identifier_->Print(stream);
}
