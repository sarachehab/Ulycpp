#include "../../include/Functions/ast_function_call.hpp"

std::string FunctionCall::getIdentifier() const {
    return function_name_->getIdentifier();
}


void FunctionCall::EmitRISC(std::ostream &stream, int destReg, Context &context) const {
    std::cerr << "In function call print" << std::endl;
    if (arguments_ != nullptr){
        arguments_->EmitRISC(stream, destReg, context);
    }
    stream << "call " << function_name_->getIdentifier() << std::endl;
    stream << "nop " << std::endl;
    stream << "mv " << context.getRegisterName(destReg) << ", " << context.getRegisterName(10) << std::endl;
    std::cerr << "COMPILER: Done function call print" << std::endl;
}


void FunctionCall::Print(std::ostream &stream) const {
    stream << function_name_->getIdentifier() << "(";
    if (arguments_ != nullptr){
        arguments_->Print(stream);
    }
    stream << ")";
}
