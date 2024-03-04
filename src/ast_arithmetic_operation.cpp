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
    return "sra ";
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


std::string OneComplement::getInstruction() const {
    return "not ";
}

std::string OneComplement::getOperation() const {
    return " ~ ";
}


std::string Negate::getInstruction() const {
    return "neg ";
}

std::string Negate::getOperation() const {
    return " - ";
}


std::string LessThan::getInstruction() const {
    return "slt ";
}

std::string LessThan::getOperation() const {
    return " < ";
}


std::string LessThanEqual::getInstruction() const {
    return "slt ";
}

std::string LessThanEqual::getOperation() const {
    return " <= ";
}


std::string GreaterThan::getInstruction() const {
    return "sgt ";
}

std::string GreaterThan::getOperation() const {
    return " > ";
}


std::string GreaterThanEqual::getInstruction() const {
    return "sgt ";
}

std::string GreaterThanEqual::getOperation() const {
    return " >= ";
}


std::string Equal::getInstruction() const {
    return "seqz ";
}

std::string Equal::getOperation() const {
    return " == ";
}


std::string NotEqual::getInstruction() const {
    return "snez ";
}

std::string NotEqual::getOperation() const {
    return " != ";
}


std::string LogicalOr::getInstruction() const {
    return "or ";
}

std::string LogicalOr::getOperation() const {
    return " || ";
}


std::string LogicalAnd::getInstruction() const {
    return "and ";
}

std::string LogicalAnd::getOperation() const {
    return " && ";
}
