#include "../../include/Operations/ast_arithmetic_operation.hpp"

std::string Addition::getInstruction()      const { return "add "; }
std::string Addition::getOperation()        const { return " + "; }

std::string Substraction::getInstruction()  const { return "sub "; }
std::string Substraction::getOperation()    const { return " - "; }

std::string Multiplication::getInstruction() const { return "mul "; }
std::string Multiplication::getOperation()   const { return " * "; }

std::string Division::getInstruction()      const { return "div "; }
std::string Division::getOperation()        const { return " / "; }

std::string Modulus::getInstruction()       const { return "rem "; }
std::string Modulus::getOperation()         const { return " % "; }