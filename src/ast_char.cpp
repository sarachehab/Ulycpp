#include "../include/ast_char.hpp"

void Character::EmitRISC(std::ostream& stream, int destReg, Context& context) const {
    stream << "li " << context.getRegisterName(destReg) << ", " << value_ << std::endl;
}

void Character::Print(std::ostream& stream) const {
    char c = (char)value_;
    stream << c << std::endl;
}