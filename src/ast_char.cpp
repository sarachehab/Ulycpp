#include "../include/ast_char.hpp"

void Character::EmitRISC(std::ostream& stream, int destReg, Context& context) const {
    std::cerr << "in character" << std::endl;
    stream << "li " << context.getRegisterName(destReg) << ", 104" << std::endl;
}

void Character::Print(std::ostream& stream) const {
    stream << "test" << std::endl;
    char c = (char)value_;
    stream << c << std::endl;
}