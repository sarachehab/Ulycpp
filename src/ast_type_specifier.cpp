#include "ast_type_specifier.hpp"

Specifier TypeSpecifier::getType(Context& context) const {
    return type_;
}

void TypeSpecifier::EmitRISC(std::ostream &stream, int destReg, Context &context) const {}

void TypeSpecifier::Print(std::ostream &stream) const
{
    switch (type_){
        case Specifier::_int:
            stream << "int" << std::endl;
            break;
        case Specifier::_unsigned:
            stream << "unsigned" << std::endl;
            break;
        case Specifier::_float:
            stream << "float" << std::endl;
            break;
        case Specifier::_double:
            stream << "double" << std::endl;
            break;
        case Specifier::_char:
            stream << "char" << std::endl;
            break;
        default:
            throw std::runtime_error("Type not defined yet (ast_type_specifier)");
    }
}
