#include "ast_type_specifier.hpp"

void TypeSpecifier::EmitRISC(std::ostream &stream, int destReg, Context &context) const {}

void TypeSpecifier::Print(std::ostream &stream) const
{
    stream << type_;
}
