#include "../../include/Operations/ast_bitwise_operation.hpp"


std::string InclusiveOr::getInstruction()   const { return "or "; }
std::string InclusiveOr::getOperation()     const { return " | "; }

std::string ExclusiveOr::getInstruction()   const { return "xor "; }
std::string ExclusiveOr::getOperation()     const { return " ^ "; }

std::string And::getInstruction()           const { return "and "; }
std::string And::getOperation()             const { return " & "; }

std::string LeftShift::getInstruction()     const { return "sll "; }
std::string LeftShift::getOperation()       const { return " << "; }

std::string RightShift::getInstruction()    const { return "sra "; }
std::string RightShift::getOperation()      const { return " >> "; }

std::string OneComplement::getInstruction() const { return "not "; }
std::string OneComplement::getOperation()   const { return " ~ "; }