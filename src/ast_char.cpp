#include "../include/ast_char.hpp"

void Character::EmitRISC(std::ostream& stream, int destReg, Context& context) const {
    switch (name_.size()){
        case 4:
            if (name_[1] == '\\'){
                switch (name_[2]){
                    case 'n':
                        stream << "li " << context.getRegisterName(destReg) << ", " << static_cast<int>('\n') << std::endl;
                        break;
                    case 't':
                        stream << "li " << context.getRegisterName(destReg) << ", " << static_cast<int>('\t') << std::endl;
                        break;
                    case 'r':
                        stream << "li " << context.getRegisterName(destReg) << ", " << static_cast<int>('\r') << std::endl;
                        break;
                    case '0':
                        stream << "li " << context.getRegisterName(destReg) << ", " << static_cast<int>('\0') << std::endl;
                        break;
                    case '\\':
                        stream << "li " << context.getRegisterName(destReg) << ", " << static_cast<int>('\\') << std::endl;
                        break;
                    case '\'':
                        stream << "li " << context.getRegisterName(destReg) << ", " << static_cast<int>('\'') << std::endl;
                        break;
                    case '\"':
                        stream << "li " << context.getRegisterName(destReg) << ", " << static_cast<int>('\"') << std::endl;
                        break;
                    default: throw std::runtime_error("Invalid character");
                }
            } else {
                stream << "li " << context.getRegisterName(destReg) << ", " << static_cast<int>(name_[1]) << std::endl;
            }
            break;
        case 3:
            stream << "li " << context.getRegisterName(destReg) << ", " << static_cast<int>(name_[1]) << std::endl;
            break;
        default: throw std::runtime_error("Invalid character");
    }
}

void Character::Print(std::ostream& stream) const {
    stream << "test" << std::endl;
    char c = (char)value_;
    stream << c << std::endl;
}