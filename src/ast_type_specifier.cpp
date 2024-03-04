#include "ast_type_specifier.hpp"

Specifier TypeSpecifier::getType() const {
    if (type_ == "int") {
        return Specifier::_int;
    }
    throw std::runtime_error("Type not defined yet (ast_type_specifier)");
}

void TypeSpecifier::EmitRISC(std::ostream &stream, int destReg, Context &context) const {}

void TypeSpecifier::Print(std::ostream &stream) const
{
    stream << type_;
}
