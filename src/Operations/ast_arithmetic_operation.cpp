#include "../../include/Operations/ast_arithmetic_operation.hpp"

std::string Addition::getInstruction(Specifier type) const {
    switch (type) {
        case Specifier::_int:
            return "add";
        case Specifier::_unsigned:
            return "add";
        case Specifier::_float:
            return "fadd.s";
        case Specifier::_double:
            return "fadd.d";
    }
    return "ERROR, check ADD";
}
std::string Addition::getOperation() const { return " + "; }

std::string Substraction::getInstruction(Specifier type) const {
    switch (type) {
        case Specifier::_int:
            return "sub";
        case Specifier::_unsigned:
            return "sub";
        case Specifier::_float:
            return "fsub.s";
        case Specifier::_double:
            return "fsub.d";
    }
    return "ERROR, check SUB";
}
std::string Substraction::getOperation() const { return " - "; }

std::string Multiplication::getInstruction(Specifier type) const {
    switch (type) {
        case Specifier::_int:
            return "mul";
        case Specifier::_unsigned:
            return "mul";
        case Specifier::_float:
            return "fmul.s";
        case Specifier::_double:
            return "fmul.d";
    }
    return "ERROR, check MUL";
}
std::string Multiplication::getOperation()   const { return " * "; }

std::string Division::getInstruction(Specifier type) const {     switch (type) {
        case Specifier::_int:
            return "div";
        case Specifier::_unsigned:
            return "div";
        case Specifier::_float:
            return "fdiv.s";
        case Specifier::_double:
            return "fdiv.d";
    }
    return "ERROR, check DIV";
}
std::string Division::getOperation()        const { return " / "; }

std::string Modulus::getInstruction(Specifier type) const { return "rem "; }
std::string Modulus::getOperation() const { return " % "; }
