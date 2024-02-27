#include "ast_arithmetic_operation.hpp"

std::string InclusiveOr::getInstruction() const {
    return "or ";
}

std::string InclusiveOr::getOperation() const {
    return " | ";
}


std::string ExclusiveOr::getInstruction() const {
    return "xor ";
}

std::string ExclusiveOr::getOperation() const {
    return " ^ ";
}


std::string And::getInstruction() const {
    return "and ";
}

std::string And::getOperation() const {
    return " & ";
}


std::string LeftShift::getInstruction() const {
    return "sll ";
}

std::string LeftShift::getOperation() const {
    return " << ";
}


std::string RightShift::getInstruction() const {
    return "srl ";
}

std::string RightShift::getOperation() const {
    return " >> ";
}


std::string Addition::getInstruction() const {
    return "add ";
}

std::string Addition::getOperation() const {
    return " + ";
}

std::string Substraction::getInstruction() const {
    return "sub ";
}

std::string Substraction::getOperation() const {
    return " - ";
}


std::string Multiplication::getInstruction() const {
    return "mul ";
}

std::string Multiplication::getOperation() const {
    return " * ";
}


std::string Division::getInstruction() const {
    return "div ";
}

std::string Division::getOperation() const {
    return " / ";
}


std::string Modulus::getInstruction() const {
    return "rem ";
}

std::string Modulus::getOperation() const {
    return " % ";
}
