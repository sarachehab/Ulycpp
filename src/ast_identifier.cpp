#include "ast_identifier.hpp"

std::string Identifier::getIdentifier() const {
    return identifier_;
};

void Identifier::EmitRISC(std::ostream &stream, int destReg, Context &context) const
{
    stream << identifier_;
}

void Identifier::Print(std::ostream &stream) const
{
    stream << identifier_;
};
