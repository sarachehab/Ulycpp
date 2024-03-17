#include "../../include/Operations/ast_bitwise_operation.hpp"


std::string InclusiveOr::getInstruction(Specifier type) const { return "or "; }
std::string InclusiveOr::getOperation() const { return " | "; }

std::string ExclusiveOr::getInstruction(Specifier type) const { return "xor "; }
std::string ExclusiveOr::getOperation() const { return " ^ "; }

std::string And::getInstruction(Specifier type) const { return "and "; }
std::string And::getOperation() const { return " & "; }

std::string LeftShift::getInstruction(Specifier type) const { return "sll "; }
std::string LeftShift::getOperation() const { return " << "; }

std::string RightShift::getInstruction(Specifier type) const { return "sra "; }
std::string RightShift::getOperation() const { return " >> "; }

std::string OneComplement::getInstruction(Specifier type) const { return "not "; }
std::string OneComplement::getOperation() const { return " ~ "; }